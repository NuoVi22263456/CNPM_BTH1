def get_categories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Taplet"

    }]


def get_products(kw):
    products = [{
        "id": 1,
        "name": "IPHONE 13",
        "price": 20000000,
        "image": "https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146233337_iphone_13_xanh_la_didongviet.jpg"
    },{
        "id": 2,
        "name": "IPHONE 13",
        "price": 20500000,
        "image": "https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146280935_iphone_13_trang_didongviet.jpg"
    },{
            "id": 3,
            "name": "IPHONE 13",
            "price": 20490000,
            "image": "https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146265270_iphone_13_den_didongviet.jpg"
    },{
            "id": 4,
            "name": "IPHONE 13",
            "price": 20400000,
            "image": "https://cdn-v2.didongviet.vn/files/products/2023/3/22/1/1682146244776_iphone_13_xanh_didongviet.jpg"
    },{
            "id": 5,
            "name": "SAMSUNG GALAXY S23",
            "price": 19500000,
            "image": "https://cdn.tgdd.vn/Products/Images/42/264060/samsung-galaxy-s23-xanh-1-1.jpg"
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw)>=0]

    return products
