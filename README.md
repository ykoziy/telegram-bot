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
- Set the telegram bot web hook (in any browser): {appEndpoint}/setWebhook
  - you will get a confirmation: webhook setup ok
