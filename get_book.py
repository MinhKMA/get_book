#!/home/minhkma/environments/env36/bin/python3.6


import requests
import bs4


url = "https://www.packtpub.com/packt/offers/free-learning"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/50.0.2661.102 Safari/537.36'}

def main():
    r = requests.get(url, headers= headers)
    if r.ok:
        s = bs4.BeautifulSoup(r.content, 'lxml')
        name = s.select_one('.dotd-title h2')
        print("The free book today: {}".format(name.text.strip()))
        print('Link: https://www.packtpub.com/packt/offers/free-learning')
    else:
        print(':(')


if __name__ == '__main__':
    main()
