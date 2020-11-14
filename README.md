# Python JWT
Python JWT implementation using symmetric Fernet encryption.

## 1. Installation:
``pip install -r requirements.txt``

## 2. Usage:

**i. Create your own key(In prod)**
```python
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
```
> Use those keys [here](https://github.com/sbhusal123/jwt-python/blob/642fcf626f824a6199c673a9391a07838fe2a0cd/fernet.py#L11)

**ii. Create an object of JWT**
```python
import JWT from jwt

# Initialize JWT with time to live in second.
jwt = JWT(ttl_in_second=2)
```

**iii. Creating token from data**
```python
# returns token
data = "my awesome data"
token = jwt.get_token(data)
```
**iv. Returning data back**
```python
# returns data from token. This returns ""Invalid token" string if not valid.
text = jwt.get_data(token)
```

> If token is invalid. If returns ``Invalid token`` string. Make sure you check for that.
