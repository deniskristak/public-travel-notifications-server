from dataclasses import dataclass


@dataclass
class UserRequestToInsert:
    request: str


@dataclass
class TokenToInsert:
    token: str


class UserRequestWriter:
    def __init__(self, user_request: UserRequestToInsert, token: TokenToInsert):
        self.user_request = user_request
        self.token = token

    def write_request_to_database(self):
        pass
