from typing import List

from fastapi import Depends, APIRouter, HTTPException
from pydantic import BaseModel
from app.api.dependencies import get_db
from app.db import session
from app.crud.employee_crud import get_all_employee
from app.schemas.employee_schemas import EmployeeOut,EmployeeCreate
from app.crud.employee_crud import create_employee, get_employee_by_id, update_employee, delete_employee

routers= APIRouter()

@routers.get("/employee/", response_model=List[EmployeeOut])
def get_all_route(db:session = Depends(get_db)):
    return get_all_employee(db)

@routers.post("/employee/", response_model=EmployeeCreate)
def create_employee_route(emp_data:EmployeeCreate=Depends(),db:session= Depends(get_db)):
    return create_employee(db, emp_data)

@routers.get("/employee/{emp_id}", response_model=EmployeeOut)
def get_employee_id_route(emp_id:int,db:session=Depends(get_db)):
    emp = get_employee_by_id(db,emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")   
    return emp

@routers.put("/employee/{emp_id}", response_model=EmployeeOut)
def update_employee_id_route(emp_id:int,db:session=Depends(get_db), Updated_data:EmployeeCreate=Depends()):
    emp = update_employee(db,emp_id, Updated_data)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")   
    return emp


@routers.delete("/employee/{emp_id}")
def delete_employee_route(emp_id: int,db:session=Depends(get_db)):
    emp =delete_employee(db,emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="employee not found")
    return emp
