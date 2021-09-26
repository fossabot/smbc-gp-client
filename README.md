# smbc-gp-client
An http client to call smbc-gp api

## upload package
```
python3 -m pip install --user --upgrade setuptools wheel twine
python3 setup.py sdist bdist_wheel
twine upload dist/*
```