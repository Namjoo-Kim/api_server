from typing import Optional
from fastapi import APIRouter, FastAPI
from fastapi.encoders import jsonable_encoder
from starlette.middleware.cors import CORSMiddleware
from routers import data

app = FastAPI()
app.include_router(data.router)

origins = [
    "https://knjoo.duckdns.org",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Main:

    def __init__(self):
        print('init')
        super().__init__()

    def __new__(cls):
        print('new')
        return super().__new__(cls)

    @app.get("/")
    def read_root():
        return {"Hello": "World"}


    @app.get("/items/{item_id}", tags=["items"], summary="예제입니다.")
    def read_item(item_id: str, q: Optional[str] = None):
        """example
        """
        return {"item_id": item_id, "q": q}

    @app.get("/data", summary="예제입니다.")
    async def data(item_id: str):
        """data
        """
        if item_id == '2' :
            date = [
            {
            "year": '1951 年',
            "value": 38,
            },
            {
            "year": '1952 年',
            "value": 52,
            },
            {
            "year": '1956 年',
            "value": 61,
            },
            {
            "year": '1957 年',
            "value": 145,
            },
            {
            "year": '1958 年',
            "value": 48,
            }
            ]
        elif item_id == '3' :
            date = [
                {
                "year": '1Q',
                "value": 38,
                },
                {
                "year": '2Q',
                "value": 52,
                },
                {
                "year": '3Q',
                "value": 61,
                },
                {
                "year": '4Q',
                "value": 145,
                }
            ]
        elif item_id == '4' :
            date = [
                {
                "year": '25week',
                "value": 38,
                },
                {
                "year": '26week',
                "value": 52,
                },
                {
                "year": '27week',
                "value": 61,
                },
                {
                "year": '28week',
                "value": 145,
                }
            ]
        return date

#python -m uvicorn main:app --reload
def main():
    print('==main()==')    
    uvicorn.run(
    app = "main:app",
    host="127.0.0.1",
    port=8000,
    reload=True,
    # reload_excludes=["app/files/"],
    )

if __name__ == "__main__":
    main()