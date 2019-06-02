import requests
import FirstBot.storeinfo as si


class GameDeal:
    def __init__(self, title, store_id, sale_price, normal_price, is_on_sale, link, store_name):
        self.store_name = store_name
        self.link = link
        self.title = title
        self.store_id = store_id
        self.sale_price = sale_price
        self.normal_price = normal_price
        self.is_on_sale = is_on_sale

    def __str__(self):
        return self.store_name + ": " + self.title + " $" + self.sale_price + "\nlink: " + self.link


store_info_list = si.read_store_info()


def look_up_game(title, price):
    resp = requests.get('http://www.cheapshark.com/api/1.0/deals?title=' + title)
    deals = []
    for data in resp.json():
        if float(data['salePrice']) < int(price) and \
                (not "expansion" in data['title'].lower()):
            link = "https://www.cheapshark.com/browse?title=" + '%20'.join(data['title'].split(' '))
            deals.append(GameDeal(data['title'],
                                  data['storeID'],
                                  data['salePrice'],
                                  data['normalPrice'],
                                  data['isOnSale'],
                                  link,
                                  store_info_list[data['storeID']]['storeName']))
    return deals
