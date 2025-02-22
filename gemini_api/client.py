from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

def game_bio_generator(game_name):
    API_KEY = os.getenv("GOOGLE_API_KEY")

    # Verifica se a chave API foi encontrada
    if not API_KEY:
        raise ValueError("A chave API não foi encontrada. Defina a variável GOOGLE_API_KEY no .env")


    client = genai.Client(api_key=API_KEY)
    prompt = f"Gere uma breve descrição para o jogo: {game_name}. Resuma em apenas uma ou duas frases no máximo"

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[prompt],
        config=types.GenerateContentConfig(
            max_output_tokens=500,
            temperature=0.1
        )
    )

    if hasattr(response, 'text') and response.text:
        return response.text.strip()
    
    return "Bio não disponível."
