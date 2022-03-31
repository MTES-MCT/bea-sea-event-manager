class SeaEventNotFoundError(Exception):
    def __init__(self, uuid: str) -> None:
        super().__init__(f"Sea event with uuid {uuid} not found.")
