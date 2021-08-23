import pymysql
from fastapi import FastAPI

from pydantic import BaseModel
from zjx_data import get_content_api

app = FastAPI()
from zjx_setting import *



# all_dataes = []


class Item(BaseModel):
    item_id: int


@app.get("/items/{item_id}")
async def read_item(item_id: int,):
    conn3 = pymysql.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE, charset='utf8')
    cur3 = conn3.cursor()
    out_id_ = get_content_api(item_id,cur3,conn3)
    if out_id_ ==0:
        return {"item_id": 0,'out_id':0}
    else:
        return {"item_id": item_id,'out_id':out_id_}







