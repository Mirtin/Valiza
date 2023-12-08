
# Online shop "Valiza"

"Valiza" is an open-source ecommerce platform built on the FastApi Web Framework.

"Valiza" is a project that works like microservice for ["Gudzik"](//) to provide data about products.



## Features Included

- Admin Panel
- Encryption/Decryption with fernet

## Authors

- [@Mirtin](https://www.github.com/Mirtin)

## How to run project

step 1:

Connect DataBase

Configure environment variables `DB_HOST`,`DB_PORT`,`DB_NAME`,`DB_USER`,`DB_PASS` in .env file to configur database

Attention: DataBase has to be PostgreSQL

step 2:

Configure Fernet

Configure environment variable `ENCRYPTION_KEY` in .env file to configure fernet

Attention: `ENCRYPTION_KEY` has to be the same as in ["Gudzik"](//)




