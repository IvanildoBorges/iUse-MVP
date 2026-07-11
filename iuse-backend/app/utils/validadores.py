import re
from uuid import UUID

def validar_email(email: str) -> str:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(padrao, email):
        raise ValueError("E-mail inválido!")
    return email.lower()

def validar_nome(nome: str) -> str:
    if not nome or len(nome.strip()) < 2:
        raise ValueError("Nome inválido!")
    return nome.strip()

def validar_uuid(valor: str) -> str:
    try:
        UUID(valor)
    except Exception:
        raise ValueError("ID deve ser um UUID válido!")
    return valor

def avaliar_estrelas(avaliacao: float, nova_avaliacao: int) -> float:
    if not 1 <= nova_avaliacao <= 5:
        raise ValueError("Avaliação deve estar entre 1 e 5!")
    return round((avaliacao + nova_avaliacao) / 2, 1)   # regra simples (média incremental)
