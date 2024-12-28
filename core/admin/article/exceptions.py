

class ArticleNotFoundError(Exception):
    def __init__(self):
        super().__init__(f"Article does not exist.")


class ValidationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)