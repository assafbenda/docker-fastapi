from fastapi import FastAPI, Depends, HTTPException
from .router import installations_router
# Create server application.
app = FastAPI(
    title="Sample FastAPI Application",
    description="This is a sample FastAPI application.",
    docs_url="/api",
    swagger_ui_parameters={"docExpansion": "none"},
)

app.include_router(installations_router, prefix="/api/v1")