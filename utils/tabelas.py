class table:
    TABELAS = {
        "serie": ["id","titulo","descricao", "ano", "categoria_id"],
        "categoria": ["id","nome","categoria"],
        "ator_serie": ["id", "id_ator","serie_id","personagem"],
        "avaliacao_serie": ["id","serie_id","nota","comentario","data_avaliacao"],
        "motivo_assistir": ["id","serie_id","motivo"],

    }

    PRIMARY_KEYS = {
        "serie": "id",
        "categoria": "id",
        "ator_serie": "id",
        "avaliacao_serie": "id",
        "motivo_assistir": "id",
    }