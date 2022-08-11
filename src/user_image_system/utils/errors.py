class userNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class imageNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)