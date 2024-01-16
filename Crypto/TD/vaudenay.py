
from urllib import request
from urllib.error import HTTPError, URLError

PORT_NUMBER = 1234

def check(ciphertext):
    "check ciphertext by sending a request to the server"
    url = f"http://localhost:{PORT_NUMBER}/check"
    data = bytes('ciphertext=' + ciphertext.hex(), encoding="ASCII")
    req = request.Request(url, data, method="POST")
    try:
        resp = request.urlopen(req)
        code = resp.getcode()
    except HTTPError as e:
        code = e.getcode()
    except URLError as e:
        import sys
        print(f"** connection problem: {e}.")
        print(f"** Is the server running on port {PORT_NUMBER}?")
        sys.exit(2)
    assert code in (200, 599)
    return code

def crackVaudenay():
    ...

def dernier_octet():
    ...