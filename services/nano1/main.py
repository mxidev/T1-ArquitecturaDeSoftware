import logging

from fastapi import FastAPI

app = FastAPI()

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Hello from (nano)Service 1"}


@app.get("/health")
def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "ok"}
