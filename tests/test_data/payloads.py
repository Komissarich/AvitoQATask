DEFAULT_SELLER_ID = 333447


fixture_payload = {
    "sellerId": DEFAULT_SELLER_ID,
    "name": "John Doe",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 5,
        "contacts": 1
    }
}


get_all_from_seller_payload = [{
    "sellerID": DEFAULT_SELLER_ID,
    "name": "John Doe",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 5,
        "contacts": 1
    }
},
{
    "sellerID": DEFAULT_SELLER_ID,
    "name": "Example",
    "price": 200,
    "statistics": {
        "likes": 1,
        "viewCount": 1,
        "contacts": 1
    }
},
{
    "sellerID": DEFAULT_SELLER_ID,
    "name": "Unknown",
    "price": 0,
    "statistics": {
        "likes": 5,
        "viewCount": 5,
        "contacts": 5
    }
},
]