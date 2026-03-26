from pydantic import BaseModel,EmailStr

#this is the base model which will be used for both creating and updating the employee details, so all the fields are required
class EmployeeBase(BaseModel):
    name:str
    age:int
    department:str
    email: EmailStr

class EmployeeCreate(EmployeeBase):
    pass

#this is ude for update the employee details, so all the fields are optional
class EmployeeUpdate(BaseModel):
    name:str | None=None
    email:EmailStr | None=None
    department :str | None=None
    age :int | None=None

class EmployeeOut(EmployeeBase):
    id :int
    class Config:
        form_attributes = True



