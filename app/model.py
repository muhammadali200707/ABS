from typing import Optional
import datetime
from enums import Language


class User:
    def __init__(self,
                 user_id: str,
                 username: str,
                 password: str,
                 email: Optional[str] = None,
                 language: Optional[str] = None,
                 created_at: [str] = None,
                 is_active: bool = False) -> None:
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.language = language or Language.English.value
        self.created_at = created_at
        self.is_active = is_active

    def __repr__(self) -> str:
        return f'{self.user_id} => {self.username}'


