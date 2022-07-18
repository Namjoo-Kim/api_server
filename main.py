from typing import Optional
from fastapi import FastAPI
from service.dblist import Dblist

app = FastAPI()

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


    @app.get("/items/{item_id}", summary="예제입니다.")
    def read_item(item_id: str, q: Optional[str] = None):
        """example
        """

        return {"item_id": item_id, "q": q}


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