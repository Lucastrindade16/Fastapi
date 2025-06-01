from fastapi import APIRouter, HTTPException
from database import Database
from utils.tabelas import table
from app.create import get_id_by_name
from app.create import create_item, criar_ator_serie

db = Database()
tb = table()

router = APIRouter(prefix="/update")
 
@staticmethod
def update_item(table_name: str, nome: str, item: dict):
        if table_name not in tb.TABELAS:
            raise HTTPException(status_code=400, detail="Tabela não permitida")

        try:
            id_valor = get_id_by_name(table_name, nome)
            colunas = tb.TABELAS[table_name] 
            chave_primaria = tb.PRIMARY_KEYS[table_name]

            set_clause = ', '.join([f"{col} = %s" for col in colunas])
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {chave_primaria} = %s"
            params = tuple(item[col] for col in colunas) + (id_valor,)

            with Database() as db:
                db.executar(sql, params)

            raise HTTPException(status_code=200, detail=f"Item atualizado com sucesso!") 

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao atualizar o item: {str(e)}")
        
@router.put("/{table_name}")
def create_routes(table_name: str, item: dict):
    return create_item(table_name, item)