import json, requests

INITIAL_GET_SUFFIX = '/index/index.json?q'
BERLIN_URL = 'https://www.berlin.de'
TARGET_FOLDER = 'text/'

with open('curl_urls.txt') as f:
	raw_urls = f.readlines()

urls = filter(lambda x: not x.startswith('#'), raw_urls)

for url in urls:	
	url = url.strip()
	response = requests.get(url+INITIAL_GET_SUFFIX)
	print('response', response)
	js = response.json()
	for k in js['index']:
		req_url = BERLIN_URL+k['txt']
		txt_resp = requests.get(req_url)
		with open(TARGET_FOLDER + req_url[req_url.rfind('/')+1:], 'w') as f_save:
			f_save.write(txt_resp.text)
	
	print('Done with', url)

print('Done')
