import requests

BASE_URL = 'https://fragment.com/'
DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'

class Telegram:
    def __init__(self) -> None:
        pass

    def get_user(self, username: str):
        response = requests.get(BASE_URL + 'username/' + username, headers={
            'User-Agent': DEFAULT_USER_AGENT,
            'X-Aj-Referer': f'{BASE_URL}?query={username}',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Requested-With': 'XMLHttpRequest',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        })

        try:
            response_json = response.json()
        except ValueError:
            return None

        if 'h' not in response_json:
            return 'Available'
        
        h_data = response_json['h']

        status = h_data.split('tm-section-header-status')[1].split('">')[0].strip()
        status_mapping = {
            'tm-status-taken': 'Taken',
            'tm-status-avail': 'Auctioned or for sale',
            'tm-status-unavail': 'Sold'
        }

        return status_mapping.get(status, 'Unknown')
