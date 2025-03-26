import openai
from config.settings import OPENAI_API_KEY

# Initialize OpenAI API
openai.api_key = OPENAI_API_KEY

def generate_response(prompt, context):
    # Combine the basic prompt with the retrieved context
    full_prompt = f"{context}\n{prompt}"

    # Send to LLM (OpenAI or other) and return response
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=full_prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return None
