import requests
import logging
import time
# import pandas as pd


logger = logging.getLogger(__name__)


class OpenF1Client:
    def __init__(self, base_url, timeout_seconds=20):
        self.BASE_URL=base_url
        self.timeout_seconds=timeout_seconds

    def api_request(self, request_name,params):
        url=f'{self.BASE_URL}/{request_name}'
        logger.info('Openf1 request started: endpoint=%s', request_name)

        start=time.perf_counter()

        try:
            response=requests.get(
                url,
                params=params,
                timeout=self.timeout_seconds,
            )
            response.raise_for_status()

            data=response.json()
        except requests.exceptions.RequestException:
            logger.exception('Openf1 request failed: endpoint=%s', request_name)
            raise

        elapsed=time.perf_counter()-start
        
        logger.info(
            "OpenF1 request completed: endpoint=%s status=%s duration=%.3fs",
            request_name,
            response.status_code,
            elapsed,
        )

        return data

    def get_races(self, year):
        params={
            'year': year,
            'session_name': 'Race'
        }
        data=self.api_request('sessions', params)

        return data


    def get_drivers(self, session_key):
        params={
            'session_key': session_key,
        }
        data=self.api_request('drivers', params)
        return data