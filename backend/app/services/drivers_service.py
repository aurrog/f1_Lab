from backend.app.integrations.openf1 import client


class DriverService:
    def __init__(self, config):
        self.data_client=client.OpenF1Client(
            base_url=config.openf1_api_url,
            timeout_seconds=config.timeout_seconds,
        )

    def get_drivers(self, session_key):
        # TODO in-cache condition and in-prefilled condition
        
        return self.data_client.get_drivers(session_key)
    