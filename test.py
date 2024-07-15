import requests

payload = {'isOverlayRequired': False,
    'apikey': 'K83554843688957',
    'language': 'eng',
    }
with open('image.jpg', 'rb') as f:
    r = requests.post('https://api.ocr.space/parse/image', files={'image.jpg': f}, data=payload)
print(r.content.decode())