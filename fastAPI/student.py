from fastapi import APIRouter

router = APIRouter()

students =[]

@router.get("/students")
def get_students():
    return {"students":students}

@router.get("/students/{id}")
def get_students_by_id(id:int):
    return {"student":students[id]}

@router.post("/students")
def post_details(age:int,name:str):
    student ={"name":name,"age":age}
    students.append(student)
    return {"message":"student is added", "student":student}

@router.put("/students/{id}")
def update_details(id:int, name:str,age:int):
    students[id] = {"name":name,"age":age}
    return {"id":id, "update_student":students[id]}

@router.delete("/students/{id}")
def delete_details(id:int):
    deleted_students= students.pop(id)
    return {"message":"Student is deleted", "students":students}