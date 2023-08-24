from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from bot import msj_bienvenida, get_rpta

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501"
    "https://joelcori.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"mensaje": msj_bienvenida()}


@app.post("/{entrada}")
def enviar_entrada(entrada: str):
    print(entrada)
    return {"rpta": get_rpta(entrada)}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
