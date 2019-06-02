import requests


class StoreInfo:
    def __init__(self, store_id, store_name, is_active, images):
        self.store_id = store_id
        self.store_name = store_name
        self.is_active = is_active
        self.images = images

    def __str__(self):
        return "Store id: " + self.store_id + ", name: " + self.store_name


def read_store_info():
    resp = requests.get('http://www.cheapshark.com/api/1.0/stores')
    store_info = []
    for data in resp.json():
        if data['isActive']:
            store_info.append(StoreInfo(data['storeID'],
                                        data['storeName'],
                                        data['isActive'],
                                        data['images']))
    return store_info
