from fastapi import FastAPI
#importing the employee and student api form the student and employee file
from employee import router as employee_router
from student import router as student_router

#fastAPI instance
app = FastAPI()

#Router Inclusion
app.include_router(employee_router, prefix="/employees")
app.include_router(student_router, prefix="/students")


