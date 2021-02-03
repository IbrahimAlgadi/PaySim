import uvicorn
from decouple import config

if __name__ == "__main__":
    uvicorn.run("ebs:app",
                host=config("S_HOST", default="127.0.0.1"),
                port=config("S_PORT", default=5000, cast=int),
                log_level=config("S_LOG_LEVEL", default="info"),
                reload=True)
