# Telegram Bot
Playing around with telegram and python, maybe something useful will be created.

## Getting Started

- Deploy the app on server of your choice
- Set env variables:
  - APP_URL: URL of deployed app
  - BOT_API_KEY: telegram bot token
  - BOT_NAME: telegram bot name
  - OWN_API_KEY: openWEather API key
- Build using command: pip install -r requirements.txt
- Run using command: python -m spacy link en_core_web_sm en && gunicorn app:app
- Set the telegram bot web hook (in any browser): https://api.telegram.org/bot{my_bot_token}/setWebhook?url={url_to_send_updates_to}
  - you will get a confirmation: {"ok":true,"result":true,"description":"Webhook was set"}
