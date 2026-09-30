from backend.app.integrations.openf1 import client


class SeasonService():
    def __init__(self, config):
        self.data_client=client.OpenF1Client(
            base_url=config.openf1_api_url,
            timeout_seconds=config.timeout_seconds,
        )

    def get_races(self, year=2026):
        # TODO: in-cache condition

        return self.data_client.get_races(year)
