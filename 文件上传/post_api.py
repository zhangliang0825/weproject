import json
import demjson
import pymysql
from fastapi import FastAPI, File, UploadFile,Form,Request
from pydantic import BaseModel
from weeklipdf_post import get_content
from fastapi.responses import JSONResponse
import uvicorn

dbhost3 = '120.26.106.222'
dbuser3 = 'julai01'
passwd3 = 'Sh51785136@sh'
dbname3 = 'jijin'


app = FastAPI()

# class Item(BaseModel):
#     id_: int
#     pdf:

@app.get("/itemday/{item_id}")
async def insert_data(item_id:int, pdf:str):

    conn3 = pymysql.connect(host=dbhost3,user= dbuser3,password= passwd3,database= dbname3, charset='utf8')
    cur3 = conn3.cursor()
    id_ = item_id
    pdf_url = pdf
    result = get_content(id_,cur3,pdf_url)
    if result==1:
        print({"id":item_id,"result":result})
        return {"id":item_id,"result":result}
    else:
        return {"id":0,"result":0}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), token: str = Form(...), ):
    content = await file.read()
    all_data = demjson.decode(token)

    path_ = all_data.get("path")

    file_name = all_data.get("name")

    with open(r'{}\{}.pdf'.format(path_,file_name),'ab') as f:
        f.write(content)
    if path_:
        return {"filename": file.filename, "token": token}
    else:
        return {"filename":-1,"token":token}
    # # all_data = dict(item)
    # print(all_data)
    # id_= all_data.get("id_")
    # print(id_)
    # result = get_content(id_)
    #
    # all_result = {'id_':id_,
    #     'result':'1',
    #     'code':1
    # }
    #
    # return JSONResponse(content=all_result)


# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"Hello": "World"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str = None):
#     return {"item_id": item_id, "q": q}

# uvicorn post_api:app --host 127.0.0.1 --port 8080 --reload


if __name__ == '__main__':
    uvicorn.run(app='post_api:app', host="127.0.0.1", port=8080)