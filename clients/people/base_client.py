class BaseClient:
    def __init__(self):
        self.header = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }