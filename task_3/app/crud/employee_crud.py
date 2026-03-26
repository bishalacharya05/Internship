from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.db.session import SessionLocal
from app.models.employee_model import Employee
from app.schemas.employee_schemas import EmployeeCreate, EmployeeOut, EmployeeUpdate


def get_all_employee(db: Session):
    employees = db.execute(select(Employee))
    return employees.scalars().all()

def create_employee(db: Session, emp_data: EmployeeCreate):
    employee = Employee(**emp_data.model_dump())
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee

def get_employee_by_id(db:Session, emp_id:int):
    employee = db.execute(select(Employee).where(Employee.id == emp_id))
    result = employee.scalar_one_or_none()
    return result


#function to update employee using Id
def update_employee(db: Session, emp_id: int, Updated_data: EmployeeUpdate):
    employee = db.execute(select(Employee).where(Employee.id == emp_id))
    result = employee.scalar_one_or_none()

    if result:
        result.name = Updated_data.name
        result.department = Updated_data.department
        result.age = Updated_data.age
        result.email = Updated_data.email
        db.commit()
        db.refresh(result)

    return result

#function to delete employee using ID
def delete_employee(db: Session, emp_id: int):
    employee = db.execute(select(Employee).where(Employee.id == emp_id))
    result = employee.scalar_one_or_none()

    if result:
        db.delete(result)
        db.commit()
        return {
            "message": f"Employee with id {emp_id} has been deleted successfully."
        }

    return {
        "message": f"Employee with id {emp_id} not found."
    }



