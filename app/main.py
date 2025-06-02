from fastapi import FastAPI
from routes import ator_serie, avaliacao_serie, categoria, serie, motivos_assistir, delete, update

app = FastAPI()

app.include_router(serie.router, prefix="/series", tags=["Séries"])
app.include_router(categoria.router, prefix="/categorias", tags=["Categorias"])
app.include_router(ator_serie.router, prefix="/atores", tags=["Atores"])
app.include_router(avaliacao_serie.router, prefix="/avaliacoes", tags=["Avaliações"])
app.include_router(motivos_assistir.router, prefix="/motivos", tags=["Motivos para Assistir"])
app.include_router(delete.router, prefix="/delete", tags=["Delete"])
