from pydantic import BaseModel
from typing import Dict, Any

class Delete(BaseModel):
    tabela: str
    id: int

class UpdateItem(BaseModel):
    tabela: str
    nome: str
    valores: Dict[str, Any]

class Serie(BaseModel):
    id: int
    titulo: str
    descricao: str
    ano: int
    categoria_id: int

class Categoria(BaseModel):
    id: int
    nome: str
    categoria: str

class Ator(BaseModel):
    id: int
    nome: str

class Ator_Serie(BaseModel):
    id_serie: int
    id_ator: int
    personagem: str

class Avaliacao_Serie(BaseModel):
    id: int
    id_serie: int
    nota: int
    comentario: str
    data_avaliacao: str

class Motivo_Assistir(BaseModel):
    id: int
    id_serie: int
    motivo: str

class Ator_serie(BaseModel):
    nome_ator:str
    titulo: str
    personagem: str

