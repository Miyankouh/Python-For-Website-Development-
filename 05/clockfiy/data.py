#  NORMALIZED

user = {
    "id": "2",
    "username": "moo",
    "password": "1245",

}

invoice = {
    "id": "123654879",
    "amount": "12",
    "currency": "usd",
    "user_id": 2,

}

#   Catalog
filters = [
    {
        'category': 12,
        'items': [
            {
                "name": "camera",
                "choices": ["single module", "2 module"],
                "order_number": 1,
            }
        ]
    }
]

#   De-NORMALIZED ---> mongo


user = {
    "id": "2",
    "username": "moo",
    "password": "1245",

}

item = {
    {
        "name": "s1",
        "price": 25
    }, {
        "name": "s2",
        "price": 23,
    }, {
        "name": "s3",
        "price": 22,
    }, {
        "name": "s4",
        "price": 21,
    },
}

#   Catalog

invoice = {
    "id": "123654879",
    "total_price": 23,
    "currency": "usd",
    "user_id": {
        "username": "moo"
    },
    "item": [
        {
            "name": "52",
            "price": 2,
        }, {
            "name": "s4",
            "price": 21,
        },
    ]
}
