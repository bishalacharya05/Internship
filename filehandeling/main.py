from fastapi import FastAPI, File, UploadFile,Depends,Response
from database import engine
from database import Base
from database import get_db
from sqlalchemy.orm import Session
from models import File as FileModel

app = FastAPI()

Base.metadata.create_all(bind=engine)
#simple single file upload
@app.post("/upload_single_file/")
def create_single_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename,
            "content_type": file.content_type,
            "file_size": len(file.file.read())}

# #uploading multiple files 
# @app.post("/upload_multiple_file")
# def multiple_file_upload(files: List[UploadFile]=File(...)):
#     return [{"file name":f.filename} for f in files]


# #downloading files
# @app.get("/download/{filename}")
# async def download(filename: str):
#     path = Path("uploads") / filename
#     return FileResponse(path, filename=filename)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    file_bytes = await file.read()  # convert file → bytes

    new_file = FileModel(
        filename=file.filename,
        content_type=file.content_type,
        data=file_bytes
    )

    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return {"message": "File stored", "file_id": new_file.id}


@app.get("/file/{file_id}")
def get_file(file_id:int, db:Session = Depends(get_db)):
    file = db.query(FileModel).filter(FileModel.id == file_id).first()
    if not file:
        return {
            "message":"file not found"
        }
    return Response (
        content =file.data,
        media_type=file.content_type,
        headers={
            "content-disposition": f"attachment; filename={file.filename}"
        }
    )
   
#reading the file that is saved in the database   
@app.get("/read_file/{file_id}")
def read_content(file_id:int,db:Session=Depends(get_db)):
    file = db.query(FileModel).filter(FileModel.id==file_id).first()

    if not file:
        return {"message":"file not found"}
    return Response(
        content = file.data,
        media_type =file.content_type,
        headers={
            "content_disposition": f"attachement; filename={file.filename}"
        }
    )

#Upadating the file
@app.put("/update/{file_id}")
async def update_file(file_id:int, new_file: UploadFile=File(...),db: Session = Depends(get_db)):
    db_file = db.query(FileModel).filter(FileModel.id== file_id).first()
    if not db_file:
        return {
            "error":"file not found"
        }
    
    new_bytes =  await new_file.read()

    #replace old file with new file
    db_file.filename = new_file.filename
    db_file.content_type = new_file.content_type
    db_file.data = new_bytes

    db.commit()
     
    return {
        "message":"file updated successfully"
    }

@app.delete("/delete/{file_id}")
def delete_file(file_id:int,db:Session= Depends(get_db)):
    db_file = db.query(FileModel).filter(FileModel.id== file_id).first()
    if  not db_file:
       return {
        "message":"file Not found"
     }
    db.delete(db_file)
    db.commit()