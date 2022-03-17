import uvicorn
from fastapi import FastAPI


app = FastAPI()

if __name__ == '__main__':
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)