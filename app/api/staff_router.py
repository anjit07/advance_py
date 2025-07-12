from fastapi import APIRouter
from app.data_repository.local_data import get_staff_list
from app.data_repository.local_data import add_staff
from app.model.staff import Staff

staff_routers = APIRouter()

@staff_routers.get("/list")
def get_staffs():
    data_list = get_staff_list()
    return data_list

@staff_routers.post("/add")
def add_new_staff(staff:Staff):
    response =  add_staff(staff)
    return response

