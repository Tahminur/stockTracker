import requests
import json

import config as cfg


response = response = requests.get(cfg.api_url)
print(response.status_code)
