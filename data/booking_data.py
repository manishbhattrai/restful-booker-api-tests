
VALID_DATA = {

    "firstname" : "John",
    "lastname" : "Doe",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}

INVALID_DATA = [
    {
    "lastname" : "Doe",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "John",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "John",
    "lastname" : "Brown",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "additionalneeds" : "Breakfast"
    }
]

UPDATED_VALID_DATA = {

    "firstname" : "John",
    "lastname" : "Doe",
    "totalprice" : 122,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
}
UPDATED_INVALID_DATA = [
    {
    "lastname" : "Doe",
    "totalprice" : 122,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "John",
    "totalprice" : 111,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "John",
    "lastname" : "Brown",
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Lunch"
    },

    {
    "firstname" : "Jim",
    "lastname" : "Doe",
    "totalprice" : 131,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    },

    {
    "firstname" : "Jenny",
    "lastname" : "Doe",
    "totalprice" : 111,
    "depositpaid" : False,
    "additionalneeds" : "Breakfast"
    }
]

PARTIAL_UPDATE_DATA = {

    "firstname": "John",
    "totalprice": 321,
    "depositpaid" : False
}