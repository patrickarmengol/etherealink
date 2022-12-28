from fastapi import FastAPI

from etherealink import schemas

app = FastAPI()


@app.post('/create/', response_model=schemas.URLInfo)
def create_url(url: schemas.URLCreate):
    pass


@app.get('/{url_key}')
def redirect_to_target(url_key: str):
    pass


@app.get('/admin/{secret_key}', response_model=schemas.URLInfo)
def get_url_info(secret_key: str):
    pass


@app.put('/admin/{secret_key}')
def change_settings(secret_key: str, settings: schemas.URLChange):
    pass


@app.delete('/admin/{secret_key}')
def delete_url(secret_key: str):
    pass
