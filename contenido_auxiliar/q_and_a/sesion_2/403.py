import requests

def main():
    HEADERS  = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}


    base_url = "https://dle.rae.es/"
    final_url = base_url + "amarillo"
    return requests.get(final_url, headers=HEADERS), final_url


if __name__ == '__main__':
    res = main()
    print(res)