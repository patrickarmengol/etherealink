# etherealink

FastAPI backend for **etherealink**
URL shortener API for self-destructible and expirable links

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation

set the `DB_URL` environment variable (works with .env file) (default is `sqlite://:memory:`)

with docker:
```console
git clone git@github.com:patrickarmengol/etherealink.git
cd etherealink/backend

docker build -t etherealink-backend .
docker run -it -p 5000:5000 --rm etherealink-backend
```

without docker:
```console
git clone git@github.com:patrickarmengol/etherealink.git
cd etherealink/backend

python -m venv venv
source venv/bin/activate
pip install --upgrade build hatchling && pip install .

uvicorn etherealink.main:app --host 0.0.0.0 --port 5000
```

## Usage

see generated docs after installation at http://0.0.0.0:5000/docs

## License

`etherealink` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)
