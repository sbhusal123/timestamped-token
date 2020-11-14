from utils import (
    convert_dict_to_string,
    convert_string_to_dict,
    get_datetime_difference,
)
from fernet import FernetHelper

import datetime
from dateutil import parser


class JWT(object):
    """JWT encode decode helper"""

    def __init__(self, ttl_in_second):
        """Takes time to live in second"""
        self.fernet = FernetHelper()
        self.ttl_in_second = ttl_in_second

    def _add_expiry_time(self, data):
        """Adds expiry time to the data."""
        data_dict = {"data": data, "expiry": str(datetime.datetime.now())}
        string_data_dict = convert_dict_to_string(data_dict)
        return string_data_dict

    def get_token(self, data):
        """Returns encrypted token with the expiry date. Date also encrypted"""
        expiry_added_data = self._add_expiry_time(data)
        encrypted_data = self.fernet.encrypt(expiry_added_data)
        return encrypted_data

    def _is_token_valid(self, data_dict):
        """Accepts the dict of decrtpted data and checks if it's valid"""

        # check if data dicts contains valid keys
        data = data_dict.get("data", None)
        expiry = data_dict.get("expiry", None)
        is_token_valid = data != None or expiry != None

        # Check if token is expired
        time_difference = get_datetime_difference(
            parser.parse(expiry), datetime.datetime.now()
        )

        is_not_expired = time_difference < float(self.ttl_in_second)

        if is_token_valid and is_not_expired:
            return True
        return False

    def get_data(self, cipher_text):
        """Returns and checks actual data after decrypting"""
        decrypted_token = self.fernet.decrypt(cipher_text)

        if not decrypted_token:
            return "Invalid token"

        data_dict = convert_string_to_dict(decrypted_token)

        if self._is_token_valid(data_dict):
            return data_dict.get("data")
        else:
            return "Invalid token"


"""
# Initialize JWT with time to live in second.
jwt = JWT(ttl_in_second=2)

data = "my awesome data"
token = jwt.get_token(data)
print(token)

print("\n")
text = jwt.get_data(token)
print(text)
"""