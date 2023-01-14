# etherealink frontend

Vue.js frontend for **etherealink**
URL shortener for self-destructible and expirable links

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

set the `VITE_BASE_URL` and `VITE_API_URL` environment variables (works with .env file)

with docker:
```console
git clone git@github.com:patrickarmengol/etherealink.git
cd etherealink/frontend

docker build -t etherealink-frontend .
(can pass env vars with --build-arg VITE_BASE_URL="...")
docker run -it -p 8080:80 --rm etherealink-frontend
```

without docker:
```console
git clone git@github.com:patrickarmengol/etherealink.git
cd etherealink/frontend

npm install
npm install -g http-server
npm run build
http-server dist
```


## Usage

submit a valid target URL and specify expiry settings in the form
the response contains a shortened link that will redirect you when visited and an admin link where you can change expiry settings for the link or delete it

## License

`etherealink` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)
