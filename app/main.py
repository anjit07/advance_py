from fastapi import FastAPI
from app.api import routes
from app.api import staff_router

app = FastAPI()
app.include_router(routes.router)
app.include_router(staff_router.staff_routers,prefix="/staff")
