import urllib.request
import urllib.parse
import json

def generate(prompt):
    # This is a basic mock AI module.
    # In a real implementation, you would pass the prompt to an LLM API (like Gemini, OpenAI, etc.)
    # For now, we will return a simulated AI response.
    return "AI says: I received your prompt: '" + str(prompt) + "'"

def analyze_sentiment(text):
    text_lower = str(text).lower()
    if "good" in text_lower or "happy" in text_lower or "great" in text_lower:
        return "positive"
    elif "bad" in text_lower or "sad" in text_lower or "terrible" in text_lower:
        return "negative"
    else:
        return "neutral"
