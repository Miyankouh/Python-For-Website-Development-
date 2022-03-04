#  NORMALIZED


users = [
    {
        "username": "moo",
        "password": "1245",
        "email": "moo@gmail.com"
    },
    {
        "username": "reza",
        "password": "1245",
        "email": "reza@gmail.com"
    },
    {
        "username": "ali",
        "password": "1245",
        "email": "ali@gmail.com"
    },
    {
        "username": "iman",
        "password": "1245",
        "email": "iman@gmail.com"
    },
]

projects = [
    {
        "name": "Onlin Shop",
        "rate": 0,
        "currency": "USD",
        "department": "Develop",
    },
    {
        "name": "Pyment Gateway",
        "rate": 12,
        "currency": "USD",
        "department": "Develop",
    },
    {
        "name": "Video Streamer",
        "rate": 8.5,
        "currency": "USD",
        "department": "Develop",
    },
]

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

