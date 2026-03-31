# BotMarcela - Telegram Bot

Automação de bot Telegram com `python-telegram-bot`.

## Requisitos

1. Python 3.11+
2. `pip install -r requirements.txt`
3. Criar bot com BotFather e obter token
4. Criar arquivo `.env`:

```env
TELEGRAM_TOKEN=seu_token_aqui
```

## Uso Python

```bash
pip install -r requirements.txt
python bot/app.py
```

## Estrutura Python

bot/
├─ app.py
├─ handlers/
│  ├─ start.py
│  ├─ help.py
│  ├─ echo.py
│  ├─ hora.py
│  ├─ quote.py
│  └─ unknown.py
├─ services/
│  └─ quote_service.py
├─ config.py

## Uso Node.js

```bash
npm init -y
npm install telegraf node-fetch dotenv
node bot.node.js
```

## Integração de API (exemplo)

Ambos os bots suportam `/quote`, que busca de `API_QUOTE_URL` no .env com fallback para `https://api.quotable.io/random`.

## Comandos do bot

- /start: Saudação
- /help: Ajuda
- /echo <texto>: Responde com o mesmo texto
- /hora: Retorna o horário atual
