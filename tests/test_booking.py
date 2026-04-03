import pytest
from data.booking_data import (
    VALID_DATA, INVALID_DATA,
    UPDATED_VALID_DATA, UPDATED_INVALID_DATA,
    PARTIAL_UPDATE_DATA
    )
from data.login_data import VALID_LOGIN


class TestBooking:

    def test_get_booking_list(self,client):

        res = client.get("/booking")
        assert res.status_code == 200
        data = res.json()
        assert isinstance(data,list)
        assert all("bookingid" in item for item in data)


    def test_get_booking_by_id(self, client):

        res = client.get("/booking")
        data = res.json()
        booking_id = data[1]['bookingid']
        res = client.get(f"/booking/{booking_id}")
        assert res.status_code == 200
        data = res.json()
        assert isinstance(data, dict)
        assert "firstname" in data
        assert "totalprice" in data
        assert "checkin" in data['bookingdates']
        assert "checkout" in data ['bookingdates']
        assert isinstance(data['firstname'], str)
        assert isinstance(data['bookingdates'],dict)
        assert isinstance(data['depositpaid'], bool)

    def test_get_booking_invalid_id(self,client):

        res = client.get("/booking/9999")
        assert res.status_code == 404

    def test_get_booking_invalid_format(self,client):

        res = client.get("/booking/abc")
        assert res.status_code == 404

    def test_get_booking_zero_id(self,client):

        res = client.get("/booking/0")
        assert res.status_code == 404

    def test_get_booking_negative_id(self,client):

        res = client.get("/booking/-1")
        assert res.status_code == 404

    def test_create_valid_booking(self,client):

        res = client.post("/booking", VALID_DATA)
        assert res.status_code == 200
        data = res.json()
        assert "bookingid" in data
        assert "firstname" in data['booking']
        assert "totalprice" in data['booking']
        assert "depositpaid" in data['booking']
        assert "checkin" in data['booking']['bookingdates']
        assert isinstance(data, dict)
        assert isinstance(data['booking'], dict)
        assert isinstance(data['booking']['bookingdates'],dict)
        assert isinstance(data['booking']['depositpaid'], bool)
        assert isinstance(data['booking']['firstname'], str)

    @pytest.mark.parametrize("payload", INVALID_DATA,
                             ids=[
                                 "missing_firstname",
                                 "missing_lastname",
                                 "missing_totalprice",
                                 "missing_depositpaid",
                                 "missing_bookingdates",
                             ])
    def test_create_invalid_booking(self,client,payload):

        res = client.post("/booking", payload)
        assert res.status_code != 200


    def test_valid_booking_update(self, client):

        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]

        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }

        booking = client.post("/booking", VALID_DATA)
        id = booking.json()['bookingid']

        res = client.put(f"booking/{id}", UPDATED_VALID_DATA ,headers=auth_header)
        assert res.status_code == 200

        data = res.json()

        assert "firstname" in data
        assert "totalprice" in data
        assert "checkin" in data['bookingdates']
        assert "checkout" in data['bookingdates']
        assert data['firstname'] == 'John'
        assert data['lastname'] == 'Doe'
        assert data ['depositpaid'] == False
        assert data ['totalprice'] == 122
        assert isinstance(data,dict)


    @pytest.mark.parametrize("payload", UPDATED_INVALID_DATA,
                             ids=[
                                 "missing_firstname",
                                 "missing_lastname",
                                 "missing_totalprice",
                                 "missing_depositpaid",
                                 "missing_bookingdates",
                             ])
    def test_invalid_booking_update(self,client,payload):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        booking = client.post("/booking", VALID_DATA)
        id = booking.json()['bookingid']
        res = client.put(f"booking/{id}", payload, headers=auth_header)
        assert res.status_code !=200


    def test_update_booking_negative_id(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        res = client.put(f"booking/-1", UPDATED_VALID_DATA, headers=auth_header)
        assert res.status_code != 200

    def test_update_booking_zero_id(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        res = client.put(f"booking/0", UPDATED_VALID_DATA, headers=auth_header)
        assert res.status_code != 200

    def test_update_booking_without_token(self,client):

        booking = client.post("/booking", VALID_DATA)
        id = booking.json()['bookingid']
        res = client.put(f"booking/{id}", UPDATED_VALID_DATA)
        assert res.status_code !=200

    def test_update_booking_with_invalid_format(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        res = client.put(f"booking/abc", UPDATED_VALID_DATA, headers=auth_header)
        assert res.status_code != 200


    def test_partial_booking_update(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        booking = client.post("/booking", VALID_DATA)
        id = booking.json()['bookingid']
        res = client.patch(f"booking/{id}", PARTIAL_UPDATE_DATA, headers=auth_header)
        data = res.json()
        assert "firstname" in data
        assert "totalprice" in data
        assert "checkin" in data['bookingdates']
        assert "checkout" in data['bookingdates']
        assert data['firstname'] == 'John'
        assert data['depositpaid'] == False
        assert data['totalprice'] == 321
        assert isinstance(data, dict)

    def test_booking_delete(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        booking = client.post("/booking", VALID_DATA)
        id = booking.json()['bookingid']
        res = client.delete(f"booking/{id}", headers=auth_header)
        ##using status code 201 as it returns 201 status code
        assert res.status_code == 201

    def test_booking_delete_with_negative_id(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        res = client.delete("booking/-1", headers=auth_header)
        ##using status code 201 as it returns 201 status code
        assert res.status_code != 201

    def test_booking_delete_invalid_format(self,client):
        login = client.post("/auth", VALID_LOGIN)
        token = login.json()["token"]
        auth_header = {
            "Content-Type": "application/json",
            "Cookie": f"token={token}"
        }
        res = client.delete("booking/abc", headers=auth_header)
        ##using status code 201 as it returns 201 status code
        assert res.status_code != 201

    def test_booking_delete_without_token(self,client):

        res = client.delete("booking/1")
        ##using status code 201 as it returns 201 status code
        assert res.status_code != 201
