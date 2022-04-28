# GET/POST запросы
import requests
import json
import os

from app.settings import settings

SERVER_URL = 'http://{server}:{port}/'.format(server=settings.server_host,
                                       port=settings.server_port)

access_token = settings.access_token

sale_id = 2

page_url = f'sales/{sale_id}'
header = {'Authorization': f'Bearer {access_token}'}

path_request = os.path.join(SERVER_URL, page_url)

r = requests.get(path_request, headers=header)

current_text = json.loads(r.text)
print(current_text)
