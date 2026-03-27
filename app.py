import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_resume(skills, role):
    prompt = f"""
    Create a professional resume for a {role}.
    Skills: {skills}.
    Include sections: Summary, Skills, Projects.
    Keep it clean and structured.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    skills = input("Enter your skills: ")
    role = input("Enter target role: ")
    result = generate_resume(skills, role)
    print("\nGenerated Resume:\n")
    print(result)
