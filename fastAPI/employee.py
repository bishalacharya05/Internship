from fastapi import APIRouter
from pydantic import BaseModel
router =APIRouter()
class Employee(BaseModel):
    id:int
    name:str
    age:int

employees =[]


@router.post("/employee")
def create_employee(employee:Employee):
    employees.append(employee)
    return {
        "message":"Employee created successfully",
        "employee":employee
    }
    
@router.get("/employee")
def get_details():
    return {
        "employees":employees
    }
#Path parameter with type
@router.get("/employee/{employee_id}")
def get_details(employee_id:int):
    for emp in employees:
        if emp.id==employee_id:
            return emp
    return {"error":"employee not found"}


#Query parameter
@router.get("/empl")
def get_employee(employee_id: int):
    for emp in employees:
        if emp.id== employee_id:
            return emp
    return {"message": "Employee not found"}
    
@router.delete("/employee/{employee_id}")
def delete_employee(employee_id: int):
    for emp in employees:
        if emp.id==employee_id:
            delete_employee=employees.pop(emp)
            return {"message":"employee delete successfull","deleted_items":delete_employee}
    return {"message":"employee not found"}
    
#Put request
@router.put("/employee/{employee_id}")
def update_details(employee_id:int, e:Employee):
    for emp in employees:
        if emp.id== employee_id:
            emp.name=e.name
            emp.age=e.age
            return {"message":"employee updated successfully"}
        return {"message":"employee not found"}
