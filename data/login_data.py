
VALID_LOGIN = {

    "username": "admin",
    "password": "password123"
}

INVALID_LOGIN = [

    {
        "username": "user",
        "password": "pass123"
    },

    {
        "username": "admin",
        "password": "pass123"
    },

    {
        "username": "user",
        "password": "password123"
    },

    {
        "username": "randomuser"
    },

    {
        "password": "pass1234"
    },
    {
        "username": 1,
        "password": 1
    }
]