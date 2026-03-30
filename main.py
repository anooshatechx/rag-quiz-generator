‎# 1. Import Libraries
‎
‎!pip install -q pymupdf
‎!pip install -q -U google-genai
‎import pymupdf
‎import pandas as pd
‎from google import genai
‎from google.genai import types
‎from typing import List
‎from google.colab import userdata
‎from pydantic import BaseModel, Field, field_validator
‎
‎# 2. THE WIFE (Pydantic Rules)
‎
‎class DBMS(BaseModel):
‎    question : str = Field(description = "A clear question about Database Management System")
‎    answer : str
‎    options : List[str]
‎    explanation : str = Field(description = "If the answer is wrong then explain why")
‎
‎# Validator
‎    @field_validator("options")
‎    @classmethod
‎    def validator(cls, v):
‎        if len(v) != 4:
‎            raise ValueError("There must be 4 options")
‎        return v
‎
‎# Collection of Questions
‎class QuizBatch(BaseModel):
‎    questions : List[DBMS]
‎
‎# 3. THE HUSBAND AND KIDS (SETUP)
‎
‎api_key = userdata.get('api_key')
‎client = genai.Client(api_key=api_key)
‎
‎# The Husband's Contract
‎generation_config = types.GenerateContentConfig(
‎    response_mime_type="application/json",
‎    response_schema=QuizBatch
‎)
‎
‎# 4. THE HOMEWORK (PDF)
‎
‎file = "/content/drive/MyDrive/CS403 Handouts.pdf"
‎extract = pymupdf.open(file)
‎
‎full_text = ""
‎for page in extract:
‎    full_text += page.get_text()
‎
‎print(f"📖 Loaded {len(extract)} pages. Total characters: {len(full_text)}")
‎
‎# THE PIPELINE
‎try:
‎    prompt = f"""
‎    Act as a Database Professor.
‎    Using the following text from the CS403 handouts, create 10 high-quality MCQs:
‎    {full_text}
‎
‎    For each MCQ, provide exactly 4 options (1 correct and 3 incorrect).
‎    In the 'explanation' field, contrast the right answer with the wrong ones.
‎    """
‎
‎    print("🧠 The Professor is analyzing the whole handout... Please wait.")
‎
‎# ONE request
‎    response = client.models.generate_content(
‎        model='gemini-2.5-flash',
‎        contents=prompt,
‎        config=generation_config
‎    )
‎
‎    # Save the Results
‎    quiz_results = response.parsed
‎    print("🎉 Done! Full Quiz generated successfully.")
‎
‎# 5. THE RESULT Display
‎
‎    for i, q in enumerate(quiz_results.questions, 1):
‎        print(f"QUESTION {i}: {q.question}")
‎        print(f"  [A] {q.options[0]}")
‎        print(f"  [B] {q.options[1]}")
‎        print(f"  [C] {q.options[2]}")
‎        print(f"  [D] {q.options[3]}")
‎        print(f"\n✅ CORRECT ANSWER: {q.answer}")
‎        print(f"💡 EXPLANATION: {q.explanation}")
‎        print("-" * 50)
‎
‎except Exception as e:
‎    print(f"🚦 Error: {e}")
‎    print("Tip: Check your API key or internet connection.")
‎
‎# Convert your results into a list of dictionaries
‎data = []
‎for q in quiz_results.questions:
‎    data.append({
‎        "Question": q.question,
‎        "Correct Answer": q.answer,
‎        "Options": ", ".join(q.options),
‎        "Pedagogical Explanation": q.explanation
‎    })
‎
‎# Create a DataFrame and save to CSV
‎df = pd.DataFrame(data)
‎df.to_csv("JSSEP_Research_Results.csv", index=False)
‎
‎print("✅ File saved! Look in the 'Files' folder on the left for JSSEP_Research_Results.csv")
‎
