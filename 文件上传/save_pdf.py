import demjson
import pymysql
from fastapi import FastAPI, File, UploadFile,Form,Request
import uvicorn
app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...), token: str = Form(...), ):
    try:
        content = await file.read()
        all_data = demjson.decode(token)

        path_ = all_data.get("path")

        file_name = all_data.get("name")

        with open(r'{}{}.pdf'.format(path_,file_name),'ab') as f:

            f.write(content)
        if content:
            return {"filename": file.filename, "token": token,'code':1}
        else:
            return {"filename":-1,"token":token,'code':-1}
    except  Exception as e:
        if e:
            return { "filename":-1,"token":token,'code':-1}