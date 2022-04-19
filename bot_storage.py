class Storage:
    INSTANCE = None

    @classmethod
    def init(cls, bot, dp):
        cls.INSTANCE = Storage(bot, dp)

    def __init__(self, bot, dp) -> None:
        if dp is None:
            raise KeyError
        if bot is None:
            raise KeyError
        self._bot = bot
        self._dp = dp

    def get_bot(self):
        return self._bot

    def get_dp(self):
        return self._dp
