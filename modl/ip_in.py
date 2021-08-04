# code by : nerd-ops

import requests
import yaml
def ip_api(web):
	response = requests.get(f"http://ip-api.com/json/{web}")
	val = response.json()
	if val["status"] == "success":
		return val["query"],yaml.dump(val, sort_keys=False, default_flow_style=False)
	else:
		return  "result","no info"
