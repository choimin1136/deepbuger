from typing import Annotated
import uuid
import os

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from src.google_cloud.storage_c import GCS
from src.google_cloud.firebase_c import GCFS
from test import test


gcs=GCS()
fb=GCFS()

app = FastAPI()

@app.get("/")
def read_root():


    content = """
<body>
    <form action="/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)

# dataset = { 
#     datapath
# }
class Item(BaseModel):
    name : str
    file : str


@app.post("/files/")
async def create_files(files: UploadFile):
    print(files.content_type)
    UPLOAD_DIR = "./downloader"
    content = await files.read()
    filename=f"{str(uuid.uuid4())}.mp4"

    # storage 저장
    url=gcs.upload_to_bucket("input/",filename,content)

    # model_path=""
    output_path="./downloader/output"
    
    predict=67.08
    output=url
    # output,predict=test_full_image_network(url,model_path,output_path,start_frame=0,end_frame=None,cuda=True)
    # video_path='./DEEPBUGER/videos/jisoo.mp4'
    model_path="./models/11_deepburger.pkl"
    predict=test(video_path=url,model_path=model_path)
    


    fb.insert_data(url,predict)

    # with open(os.path.join(UPLOAD_DIR, filename), "wb") as fp:
    #     fp.write(content)

    return {"output": url, "result":predict}


    # return dataset