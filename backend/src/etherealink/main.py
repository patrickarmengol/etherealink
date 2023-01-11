from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse

from etherealink import crud, schemas
from etherealink.database import orm_init

app = FastAPI()
orm_init(app)


@app.post('/create/', response_model=schemas.URLInfo)
async def create_url(url: schemas.URLCustom):
    if url.custom_key and await crud.get_db_url_by_url_key(url.custom_key):
        raise HTTPException(status_code=400, detail='url key already in use')
    return await crud.create_db_url(url)


@app.get('/{url_key}')
async def redirect_to_target(url_key: str):
    if db_url := await crud.get_db_url_by_url_key(url_key):
        if db_url.clicks_left is not None and db_url.clicks_left < 1:
            raise HTTPException(status_code=400, detail='no clicks left')
        elif db_url.expiry is not None and db_url.expiry.timestamp() < datetime.utcnow().timestamp():
            raise HTTPException(status_code=400, detail='link has expired')
        else:
            await crud.update_url_settings(db_url, schemas.URLSettings(clicks_left=db_url.clicks_left - 1, expiry=db_url.expiry))
            return RedirectResponse(db_url.target_url)
    else:
        raise HTTPException(status_code=404, detail='url not found in database')


@app.get('/admin/{admin_key}', response_model=schemas.URLInfo)
async def get_url_info(admin_key: str):
    if db_url := await crud.get_db_url_by_admin_key(admin_key):
        return db_url
    else:
        raise HTTPException(status_code=404, detail='admin url not found in database')


@app.put('/admin/{admin_key}', response_model=schemas.URLInfo)
async def change_settings(admin_key: str, settings: schemas.URLSettings):
    if db_url := await crud.get_db_url_by_admin_key(admin_key):
        return await crud.update_url_settings(db_url, settings)
    else:
        raise HTTPException(status_code=404, detail='admin url not found in database')


@app.delete('/admin/{admin_key}')
async def delete_url(admin_key: str):
    if db_url := await crud.get_db_url_by_admin_key(admin_key):
        await crud.delete_url(db_url)
        return {'detail': f'deleted {admin_key}'}
    else:
        raise HTTPException(status_code=404, detail='admin url not found in database')
