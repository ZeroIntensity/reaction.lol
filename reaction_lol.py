import requests

def getimage(args=None):
  if not args:
    response = requests.get('https://reaction.lol/image')
    response = response.json()
    return response.get('url')
  else:
    response = requests.get(f'https://reaction.lol/get?{args}')
    response = response.json()
    if response == 404:
      return 404
    return response.get('url')



def getall():
  response = requests.get('https://reaction.lol/all')
  response = response.json()
  response = list(response.keys())
  return response