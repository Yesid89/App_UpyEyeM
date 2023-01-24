import urequests

#Bot Telegram
def bot_send_text(bot_message):
  bot_token = 'Token'
  bot_chatID = 'Chat ID'
  send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

  response = urequests.get(send_text)
  response.close()
  return response