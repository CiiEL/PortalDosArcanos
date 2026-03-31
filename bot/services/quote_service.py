import json
import logging
import urllib.request
import urllib.error

logger = logging.getLogger(__name__)

def fetch_quote(api_url: str) -> str:
    try:
        with urllib.request.urlopen(api_url, timeout=10) as response:
            if response.status != 200:
                raise ValueError(f"API response {response.status}")
            data = json.load(response)
    except urllib.error.URLError as exc:
        logger.exception("Erro ao chamar API de quote")
        raise

    text = data.get("content") or data.get("quote") or data.get("text")
    author = data.get("author") or data.get("from") or "desconhecido"

    if not text:
        logger.error("API de quote retornou sem texto: %s", data)
        raise ValueError("Resposta inesperada da API")

    return f'"{text}"\n- {author}'

