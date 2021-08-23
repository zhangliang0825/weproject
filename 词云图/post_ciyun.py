import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ciyun import main
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()


# class Item(BaseModel):
#
#     keywords: str


@app.get('/items/{keywords}')
async def read_results(keywords:str):

    results = await main(keywords)
    json_compatible_item_data = jsonable_encoder({"keywords": keywords, "results": results})

    return JSONResponse(content=json_compatible_item_data)


# if __name__ == '__main__':
#     uvicorn.run(app='post_ciyun:app', host="0.0.0.0", port=6060)