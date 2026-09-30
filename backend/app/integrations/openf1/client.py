import requests
import pandas as pd



class OpenF1Client:
    def __init__(self, base_url, timeout_seconds=20):
        self.BASE_URL=base_url
        self.timeout_seconds=timeout_seconds

    def api_request(self, request_name,params):
        response=requests.get(
            f'{self.BASE_URL}/{request_name}',
            params=params,
            timeout=self.timeout_seconds,
        )

        data=response.json()
        # data_df=pd.DataFrame(data)
        return data

    def get_races(self, year):
        params={
            'year': year,
            'session_name': 'Race'
        }
        data=self.api_request('sessions', params)

        return data

        # races['date_start']=pd.to_datetime(races['date_start']).dt.tz_localize(None)
        # races['date_end']=pd.to_datetime(races['date_end']).dt.tz_localize(None)


    def get_drivers(self, session_key):
        params={
            'session_key': session_key,
        }
        data=self.api_request('drivers', params)
        return data