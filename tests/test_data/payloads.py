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
    "sellerId": DEFAULT_SELLER_ID,
    "name": "John Doe",
    "price": 100,
    "statistics": {
        "likes": 10,
        "viewCount": 5,
        "contacts": 1
    }
},
{
    "sellerId": DEFAULT_SELLER_ID,
    "name": "Example",
    "price": 200,
    "statistics": {
        "likes": 1,
        "viewCount": 1,
        "contacts": 1
    }
},
{
    "sellerId": DEFAULT_SELLER_ID,
    "name": "Unknown",
    "price": 40,
    "statistics": {
        "likes": 5,
        "viewCount": 5,
        "contacts": 5
    }
},
]


negative_create_payloads = [
    ({"sellerID": "not_a_number", "name": "John Doe", "price": 100}, 400),
    ({"sellerID": -5, "name": "John Doe", "price": 100}, 400),
    ({"sellerID": 333447, "name": "", "price": 100}, 400),
    ({"name": "John Doe", "price": 100}, 400),
    ({"sellerID": 333447, "price": 100}, 400),
    ({"sellerID": 333447, "name": "John Doe"}, 400),
    ({}, 400),
    ({"sellerID": 333447, "name": "John Doe", "price": 100, 
      "statistics": {"likes": "ten", "viewCount": "five", "contacts": "one"}}, 400),
    ({"sellerID": 333447, "name": "John Doe", "price": 100, "extra_field": "something"}, 400),
]


negative_get_obj_ids = [
    ("invalid-uuid", 400),
    ("", 404),
    ("   ", 400),
    ("aae922fd-e0e4-4803-88c1-8a8071cad2b8", 404),
    ("12345", 400),
]

negative_get_all_obj_ids = [
    ("", 405),
    ("   ", 400),
    ("abc", 400),
    ("12345", 200),
]

negative_statistic_ids_v1 = [
    ("invalid-uuid", 400),
    ("   ", 400),
    ("123", 400),
    ("", 404),
    ("e2ab0d8b-428f-4e13-a078-bfd807f1b64f", 404),
]

negative_statistic_ids_v2 = [
    ("invalid-uuid", 404),
    ("", 404),
    ("   ", 404),
    ("123", 404),
    ("e2ab0d8b-428f-4e13-a078-bfd807f1b64f", 404),
]

negative_delete_ids = [
    ("invalid-uuid", 400),
    ("", 404),
    ("   ", 400),
    ("12345", 400),
    ("00000000-0000-0000-0000-000000000000", 404),
]