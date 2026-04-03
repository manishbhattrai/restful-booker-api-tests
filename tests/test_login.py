import pytest
from data.login_data import VALID_LOGIN, INVALID_LOGIN

class TestUserLogin:

    def test_valid_login(self,client):
        res = client.post("/auth", VALID_LOGIN)
        assert res.status_code == 200

        data = res.json()

        assert isinstance(data, dict)
        assert "token" in data
        assert isinstance(data['token'], str)


    @pytest.mark.parametrize("payload",INVALID_LOGIN,
                             ids= [
                                 "wrong_username_password",
                                 "wrong_password",
                                 "wrong_username",
                                 "missing_password",
                                 "missing_username",
                                 "invalid_username_password_format"
                             ])
    def test_invalid_login(self, client, payload):
        res = client.post("/auth", payload)

        ##using 200 code as it return status code 200 even in invalidate data
        assert res.status_code == 200

        data = res.json()
        assert "Bad credentials" in data["reason"]
