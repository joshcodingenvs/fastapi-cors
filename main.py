# import modules/packages
from fastapi import FastAPI

# import CORSMiddleware use the second recommended by docs
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware

# import routes
from Routes.routes import router

# app instance
app = FastAPI()

# CORS configurations
origins = [
    "http://localhost:3000",
    "http://localhost:5000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

# configure routes
app.include_router(router)