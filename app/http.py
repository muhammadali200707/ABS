class Response:
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code or 202
