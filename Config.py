import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15564460"))
    API_HASH = os.environ.get("API_HASH", "d77d97540f0ec3579c104f4a8068fa39")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5802622160:AAGNS3M7ue5vJWtVly3zLuOmUFrI1-3vN2M")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQC2PJ24NIAMwyvQaCVhSQgQxcwKQ9o_sSi69GeQ2zDPETQEotSLdEUKiXSlbnJ-tHWrAzUwJ5OzBqFXbGCKFo2PgxAeaHLPH2sEoqiSvmfIRodCfTf5Ls6yMGUt_2p5X4X74jeSlrw8UPhn5kr2Tw7GQBao1FsyWKCHjB1zoitS5LKCwTjG27lN0smJZaq2kL9y-G2mHnJ5idJnbRp_dR063h_jvEQVRtwFXzAg4Wiqti6Dcs1KuQR4sQpVDcbQKkw1fpIf9lrXH3J2zev5NWk2P9UWxjCZsGY68c_MjkHkI_FB2XSUQiArq-j_S_2tBOhhpNhuSH6lyRnrjZu5dQftAAAAAWFOyQYA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "AfifaSupport") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "AfifaUpdates") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/30674672cd44f8283ef14.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5927520518")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
