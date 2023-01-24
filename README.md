# flask-aruba-central
Very simple flask API examples


Installation:

# must have git installed

[Install Git](https://github.com/git-guides/install-git)


# Must have docker and docker compose installed.
[Install Docker Desktop](https://www.docker.com/products/docker-desktop)

Works well with docker-desktop for macbook

```
% git clone https://github.com/xod442/flask-aruba-central.git
% cd flask-aruba-central
flask-aruba-central1%  docker-compose up -d
```

# Test api directory
flask-aruba-central/tests

./test.py

# Edit pycentral central_info.py file ==> utility/central_info.py
```
central_info = {
           "username": "email@address.com",
           "password": "*****************",
           "client_id": "XXxXXXXXXXXXXX",
           "client_secret": "XXxXXXXXXXXXXX",
           "customer_id": "XXxXXXXXXXXXXX",
           "base_url": "https://apigw-uswest4.central.arubanetworks.com",
           "refresh_token": "XXxXXXXXXXXXXX"
       }
```

Get the values from Aruba Central API page
