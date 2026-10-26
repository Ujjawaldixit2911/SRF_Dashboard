import urllib.request
import json
import base64

try:
    req = urllib.request.Request('https://logo.clearbit.com/srf.com', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        img_data = response.read()
        b64 = base64.b64encode(img_data).decode('utf-8')
        print(f"data:image/png;base64,{b64[:50]}...")
        with open('logo_b64.txt', 'w') as f:
            f.write(f"data:image/png;base64,{b64}")
except Exception as e:
    print("Error:", e)
