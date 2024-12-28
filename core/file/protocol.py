from typing import Protocol


class FileServiceProtocol(Protocol):

    def save_image(self, image: bytes) -> str:
        ...