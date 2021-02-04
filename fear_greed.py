from bs4 import BeautifulSoup
import requests

url = "https://money.cnn.com/data/fear-and-greed/"
token = "Fear &amp; Greed Now: "
fear = 20
greed = 70


class get_fear_geed_index():
    def __init__(self, *args, **kwargs):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='html.parser')
        div = soup.find_all(id='needleChart')
        div = str(div[0])
        position = div.find(token)+len(token)
        self.fear_greed_index = int(div[position:position+3])


print(get_fear_geed_index().fear_greed_index)
