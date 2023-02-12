import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15564460")
    API_HASH = os.environ.get("API_HASH", "d77d97540f0ec3579c104f4a8068fa39")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5802622160:AAGNS3M7ue5vJWtVly3zLuOmUFrI1-3vN2M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLABu7dcwpAJGPI7fWFJDqTTQFGwqQONwf0bo7H8u__PD5_ws8Dh6wUk1ShuNhwGpaHheZFov4ZYtQHWHXhqsS4GDy50dbXDYberW9jJccgOBIhXWcXuHWZ6zcPGtF9DZb1jLxVq-MRVFgwbNtpOZ7r-BCIRi0cdFxENnHlpxGRj8veVMwYaZYk2Lck0Q8GHRNEf9Bwh2oVnUrSxA21VNb5vgkL6jTEabzuPMnf1w3d_Oe0FUjqV4m31jDDT97NMhEoYiDgVMbRFXa_rxsQl5UaXpzX5oxIZXFNPH1UmLRY8Fc_4XZb1VPc7vWSZKZ7ZCXmvozHXdOEUtHX7_w2Q0TdtJ0A=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "AfifaAfkMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "AfifaSupport") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "AfifaUpdates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/30674672cd44f8283ef14.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5927520518")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get("AUTO_LEAVING_ASSISTANT", "True") # Change it to "True"
