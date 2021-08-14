import datetime, base64, requests, json
from Crypto.Hash import CMAC
from Crypto.Cipher import AES

def keycontrol(uuid,sk,api_key,cmd,history) :

    #cmd = 88  # 88/82/83 = toggle/lock/unlock
    #history = 'Raspberry Pi Python Control Code 88'

    # sk convert to hex
    sk_bytes = base64.b64decode(sk)
    secret_key = sk_bytes[1:17].hex()

    # history base64 encode 
    base64_history = base64.b64encode(bytes(history, 'utf-8')).decode()

    headers = {'x-api-key': api_key}

    ts = int(datetime.datetime.now().timestamp())
    message = ts.to_bytes(4, byteorder='little')
    message = message.hex()[2:8]
    cmac = CMAC.new(bytes.fromhex(secret_key), ciphermod=AES)

    cmac.update(bytes.fromhex(message))
    sign = cmac.hexdigest()

    url = 'https://app.candyhouse.co/api/sesame2/' + uuid + '/cmd'

    body = {
        'cmd': cmd,
        'history': base64_history,
        'sign': sign
    }
    res = requests.post(url, json.dumps(body), headers=headers)

    res_json = {
        'status_code' : res.status_code,
        'response_text' : res.text
    }
    return json.dumps(res_json)

