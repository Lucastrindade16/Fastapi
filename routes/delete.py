from fastapi import APIRouter, HTTPException
from model.models import Delete
from utils.crud import executar_insert  # Essa função deve permitir execuções DELETE também

router = APIRouter(prefix="/delete")

# Lista de tabelas permitidas (importante para segurança!)
TABELAS_PERMITIDAS = {"categoria", "ator", "serie", "motivo_assistir", "avaliacao_serie", "ator_serie"}

@router.delete("/")
def deletar_item(obj: Delete):
    try:
        if obj.tabela not in TABELAS_PERMITIDAS:
            raise HTTPException(status_code=400, detail="Nome de tabela inválido ou não permitido.")

        query = f"DELETE FROM {obj.tabela} WHERE id = %s"
        params = (obj.id,)
        executar_insert(query, params)
        return {"message": f"Item removido com sucesso da tabela {obj.tabela}."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao remover o item: {str(e)}")

