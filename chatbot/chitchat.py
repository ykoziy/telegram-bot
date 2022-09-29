class ChitChatManager:
    def __init__(self):
        from chatterbot import ChatBot
        # create a new bot
        bot = ChatBot('WhizBot', database_uri='sqlite:///db.sqlite3')
        self.chitchat_bot = bot

    def generate_response(self, txt_input):
        response = self.chitchat_bot.get_response(txt_input)
        return response