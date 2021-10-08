# smbc-gp-client
An http client to call SMBC GMO Pay APIs.

## upload package
```
python3 -m pip install --user --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

## how to use
use pip install package `smbc-gp-client`
```
pip3 install smbc-gp-client
```
in your code:
```python
from smbc_gp_client.smbc_gp_client import SmbcGpClient

client = SmbcGpClient
client.create_transation(...)
client.execute_transaction(...)
```
for more details, please refer to `SmbcGpClient` class method description.
