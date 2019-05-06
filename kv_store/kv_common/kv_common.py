from datetime import datetime   

def time_message(message):
    return datetime.now().strftime("!! %H:%M:%S: ") + message