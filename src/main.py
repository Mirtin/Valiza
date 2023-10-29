from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.admin.model_views import ProductModelView, RatingModelView

from src.operations.router import router as operations_router
from src.rating.router import router as rating_router


from sqladmin import Admin
from database import engine


app = FastAPI(title="Valiza")

admin = Admin(app, engine)


admin.add_view(ProductModelView)
admin.add_view(RatingModelView)

origins = [
    "http://127.0.0.1:9000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*", "POST"],
    allow_headers=["*"],
)


app.include_router(operations_router)
app.include_router(rating_router)
