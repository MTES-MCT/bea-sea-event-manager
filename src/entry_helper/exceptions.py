class FailedPushToEmcip(Exception):

    def __init__(self, status_code: int, reason: str, error: str = None):
        self.status_code = status_code
        self.reason = reason
        super().__init__(f"Push to emcip failed because '{reason}' with status code '{status_code}'")
