from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self):
        self.API_ID = int(getenv("38169419", 0))
        self.API_HASH = getenv("45141a2ea2482b07d9d5d5ecb5121be0")

        self.BOT_TOKEN = getenv("8974001322:AAEsYd7zc5T0qmMCN8YG1ZP0mw-lCGBoMxE")
        self.MONGO_URL = getenv("mongodb+srv://devilediting994:devilediting994@cluster0.tavhuwl.mongodb.net/?appName=Cluster0")

        self.LOGGER_ID = int(getenv("-5501438346", 0))
        self.OWNER_ID = int(getenv("5385377266", 0))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 14400)) * 14400
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("BQJGa0sALcrcjw28mIQglBHZAmFIg8AIrJwXYWbgt0vRANdFEwJBO_gtPW2KBYgFe5nNI8E4T0Mpi7cbtU7qg-KaklCipifkMkPS-MsKunQQIwQkSVivrrpVu6PwUX2bGnrgtSw8OxdKZLj2C8RjavBtzDglzM_pX5SXD5W4QqQmVDbA3gXSQfXX8eQpsRo1c8GY9CiX2xICsGydNF8fNDxUq1t6hldqz0XnMUvuBn8e6_ID58UfDm8_g4cRLyRueiMKLApYP1Txui2YjIaGrdlkv6fE9DeB5B4rGYLnNgQ_N9CPt_lQv0NSn0rrHkqao43fVYLr01wbCBnLNVfykrrtcvleTwAAAAGMdB-OAA", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AetherMusicUpdates")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AetherMusicSupport")

        self.API_URL = "https://teaminflex.xyz"
        self.API_KEY = "YOUR_KEY"

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "False"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "False"

        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url
            for url in getenv("COOKIES_URL", "").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv(
            "DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg"
        )
        self.PING_IMG = getenv(
            "PING_IMG",
            "https://graph.org/file/a3cc654217d68297d8538-f0ae69bbb7a360f6ae.jpg",
        )
        self.START_VIDEO = getenv(
            "START_VIDEO",
            "https://graph.org/file/ad15e8b2f052e78256339-0c87eb7568d3e947e7.mp4",
        )

    def check(self):
        missing = [
            var
            for var in [
                "38169419",
                "45141a2ea2482b07d9d5d5ecb5121be0",
                "8974001322:AAEsYd7zc5T0qmMCN8YG1ZP0mw-lCGBoMxE",
                "mongodb+srv://devilediting994:devilediting994@cluster0.tavhuwl.mongodb.net/?appName=Cluster0",
                "-5501438346",
                "5385377266",
                "BQJGa0sALcrcjw28mIQglBHZAmFIg8AIrJwXYWbgt0vRANdFEwJBO_gtPW2KBYgFe5nNI8E4T0Mpi7cbtU7qg-KaklCipifkMkPS-MsKunQQIwQkSVivrrpVu6PwUX2bGnrgtSw8OxdKZLj2C8RjavBtzDglzM_pX5SXD5W4QqQmVDbA3gXSQfXX8eQpsRo1c8GY9CiX2xICsGydNF8fNDxUq1t6hldqz0XnMUvuBn8e6_ID58UfDm8_g4cRLyRueiMKLApYP1Txui2YjIaGrdlkv6fE9DeB5B4rGYLnNgQ_N9CPt_lQv0NSn0rrHkqao43fVYLr01wbCBnLNVfykrrtcvleTwAAAAGMdB-OAA",
            ]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(
                f"Missing required environment variables: {', '.join(missing)}"
            )
