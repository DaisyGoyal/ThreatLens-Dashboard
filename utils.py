import os
import subprocess
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use a supported text-only model
model = genai.GenerativeModel("gemini-2.5-flash")

def fetch_tweets(keyword, limit=5):
    command = f"snscrape --max-results {limit} twitter-search '{keyword}'"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip().split('\n')[:limit]

def analyze_with_gemini(tweet):
    prompt = f"""
Summarize the following cyber-related post and classify its severity (Low, Medium, High):

Post: {tweet}

Format:
Summary: ...
Severity: ...
"""
    try:
        response = model.generate_content(prompt)
        lines = response.text.strip().split('\n')

        # Fallbacks in case response is incomplete
        summary = lines[0].replace("Summary: ", "") if len(lines) > 0 else "No summary"
        severity = lines[1].replace("Severity: ", "") if len(lines) > 1 else "Unknown"

        return summary, severity

    except Exception as e:
        return "Error generating summary", "Error"




