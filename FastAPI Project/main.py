import uvicorn
from fastapi import FastAPI
from db import DB

app = FastAPI()

@app.get("/fetch_all")
def fetch_all():
    db_obj = DB()
    data = db_obj.fetch_all()
    return {"message": data}

@app.post("/add_recrod")
def add_record(first_name : str,
                last_name :str ,
                DOB : str,
                phone : str,
                email : str,
                company: str,
                sector: str,
                skills: str):
    
    try:
        db_obj = DB()
        db_obj.add_record(first_name,
                last_name,
                DOB ,
                phone,
                email,
                company,
                sector,
                skills)
        return {"message": "Success!"}
    except Exception as e:
        print(f"There is some issue while inserting data {e}")
    
@app.get("/fetch_by_id")
def fetch_by_id(id :int):
    
    try:
        db_obj = DB()
        data = db_obj.fetch_by_id(id)
        return {"message": data}
    except Exception as e:
        print(f"There is some issue while inserting data {e}")

@app.put("/update_first_name")
def update_first_name(old_first_name : str ,
                      new_first_name : str):
    
    try:
        db_obj = DB()
        data = db_obj.update_first_name(old_first_name, new_first_name)
        return {"message": data}
    except Exception as e:
        print(f"There is some issue while inserting data {e}")

@app.delete("/delete_record")
def delete_record(id : int):
    db_obj = DB()
    try:
        data = db_obj.delete_record(id)
        return {"message": data}
    except Exception as e:
        print(f"There is some issue while deleting the record ! {e}")
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload= True)