import requests

def main():
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36 [ip:5.91.168.176]"
    }
    base_url = "https://dle.rae.es/"
    final_url = base_url + "calendario"
    return requests.get(final_url, headers=HEADERS), final_url


if __name__ == '__main__':
    res = main()
