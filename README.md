# Boilerplate for KONG with Let’s Encrypt on docker-compose


`init-letsencrypt.sh` fetches and ensures the renewal of a Let’s
Encrypt certificate for one or multiple domains in a docker-compose
setup with nginx.
This is useful when you need to set up nginx as a reverse proxy for an
application.

## Installation
1. [Install docker-compose](https://docs.docker.com/compose/install/#install-compose).

2. Clone this repository: `git clone https://github.com/binhbt/Kong-SSL-Let-sencrypt.git .`

3. Install CertBot on server: sudo apt-get install certbot
- sudo certbot certonly --manual
- Add domains and email addresses to generate key
- Make sure your web server displays the following content at
http://domain/.well-known/acme-challenge/ya6k1ed-SOME-LONG-URL before continuing: 
-Get token and paste to app.letsencrypt_check response for endpoint /.well-known/acme-challenge/ 
-Enter to continue
-Now SSL key will save to /etc/letsencrypt/live/your-domain/fullchain.pem and /etc/letsencrypt/live/your-domain/privkey.pem 
-Add SSL key to KONG by: 
`curl -i -m 60 -X POST http://localhost:8001/certificates \
-F "cert=$(cat /etc/letsencrypt/live/your-domain/fullchain.pem)" \
-F "key=$(cat /etc/letsencrypt/live/your-domain/privkey.pem)" \
-F "snis=your-domain"`

4. Now can access https://your-domain



## License
All code in this repository is licensed under the terms of the `MIT License`. For further information please refer to the `LICENSE` file.
