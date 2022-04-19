import aioschedule
import messages

def Schedule():
    aioschedule.every().day.at("08:00").do(messages.morning_message)
    # pass