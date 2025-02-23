from google import genai
from google.genai import types
import os

def game_bio_generator(game_name):
    # Defina a chave diretamente no código
    API_KEY = os.getenv('API_KEY')                        # API_KEY: Foi definida como variável de ambiente
    if not API_KEY:
     raise ValueError("API_KEY não foi encontrada! Verifique se a variável de ambiente está definida.")
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
