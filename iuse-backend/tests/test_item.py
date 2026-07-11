import pytest
from datetime import datetime, UTC
from backend.app.domain.models.Item import Item
from backend.app.domain.enums.tipo_item import TipoItem
from backend.app.domain.enums.estado_conservacao import EstadoConservacao
from backend.app.domain.enums.disponibilidade import Disponibilidade

# ========= FIXTURES =========
@pytest.fixture
def item_mochila_escolar():
    return Item(
        nome="Mochila Escolar Infantil",
        categoria=TipoItem.MOCHILA,
        descricao="Mochila escolar de rodinhas, com alças acolchoadas, em tecido resistente",
        estado_conservacao=EstadoConservacao.BOM,
        id_ponto_coleta=1,
        id_doador="550e8400-e29b-41d4-a716-446655440000"
    )

# ========= TESTES DE CRIAÇÃO =========
def test_criar_item_com_dados_validos(item_mochila_escolar):
    """Teste de criação de item com dados válidos"""
    assert item_mochila_escolar.nome == "Mochila Escolar Infantil"
    assert item_mochila_escolar.descricao == "Mochila escolar de rodinhas, com alças acolchoadas, em tecido resistente"
    assert item_mochila_escolar.estado_conservacao == EstadoConservacao.BOM
    assert item_mochila_escolar.disponibilidade == Disponibilidade.DISPONIVEL
    assert item_mochila_escolar.id is not None
    assert item_mochila_escolar.criado_em is not None

def test_criar_item_com_uuid_customizado():
    """Teste para criar um item com UUID customizado"""
    item = Item(
        nome="Mochila de Rodinhas",
        categoria=TipoItem.MOCHILA,
        descricao="Mochila de rodinhas para crianças, com zíper e compartimentos",
        estado_conservacao=EstadoConservacao.BOM,
        id_ponto_coleta=2,
        id_doador="550e8400-e29b-41d4-a716-446655440001",
        id="550e8400-e29b-41d4-a716-446655440001"
    )
    assert item.id == "550e8400-e29b-41d4-a716-446655440001"

def test_criar_item_com_data_customizada():
    """Teste para criar um item com data personalizada"""
    data = datetime(2024, 1, 1, tzinfo=UTC)
    item = Item(
        nome="Mochila Escolar Infantil",
        categoria=TipoItem.MOCHILA,
        descricao="Mochila escolar de rodinhas, com alças acolchoadas, em tecido resistente",
        estado_conservacao=EstadoConservacao.BOM,
        id_ponto_coleta=3,
        id_doador="550e8400-e29b-41d4-a716-446655440002",
        criado_em=data
    )
    assert item.criado_em == data

# ========= TESTES DE VALIDAÇÃO =========
def test_nome_invalido():
    """Teste para garantir que o nome do item tenha pelo menos 2 caracteres"""
    with pytest.raises(ValueError, match="Nome do item deve conter ao menos 2 caracteres!"):
        Item(
            nome="M", 
            categoria=TipoItem.MOCHILA,
            descricao="Mochila escolar com design moderno",
            estado_conservacao=EstadoConservacao.BOM,
            id_ponto_coleta=1,
            id_doador="550e8400-e29b-41d4-a716-446655440000"
        )

def test_descricao_invalida():
    """Teste para garantir que a descrição não pode ser vazia"""
    with pytest.raises(ValueError, match="Descrição não pode estar vazia!"):
        Item(
            nome="Mochila",
            categoria=TipoItem.MOCHILA,
            descricao="",
            estado_conservacao=EstadoConservacao.BOM,
            id_ponto_coleta=1,
            id_doador="550e8400-e29b-41d4-a716-446655440000"
        )

def test_estado_conservacao_invalido():
    """Teste para garantir que o estado de conservação seja válido"""
    with pytest.raises(ValueError, match="Estado de conservação inválido!"):
        Item(
            nome="Mochila Escolar Infantil",
            categoria=TipoItem.MOCHILA,
            descricao="Mochila escolar de rodinhas",
            estado_conservacao="EXCELENTE",  # Estado inválido
            id_ponto_coleta=1,
            id_doador="550e8400-e29b-41d4-a716-446655440000"
        )

def test_tipo_invalido():
    """Teste para garantir que o tipo do item seja válido"""
    with pytest.raises(ValueError, match="Tipo inválido para o item!"):
        Item(
            nome="Mochila Escolar",
            categoria="MATERIAL_DE_ARTE",  # Tipo inválido
            descricao="Mochila escolar de rodinhas",
            estado_conservacao=EstadoConservacao.BOM,
            id_ponto_coleta=1,
            id_doador="550e8400-e29b-41d4-a716-446655440000"
        )

# ========= TESTES DE DISPONIBILIDADE =========
def test_tornar_indisponivel(item_mochila_escolar):
    """Teste para garantir que o item se torna indisponível"""
    item_mochila_escolar.tornar_indisponivel()
    assert item_mochila_escolar.disponibilidade == Disponibilidade.INDISPONIVEL

def test_tornar_disponivel(item_mochila_escolar):
    """Teste para garantir que o item se torna disponível novamente"""
    item_mochila_escolar.tornar_disponivel()
    assert item_mochila_escolar.disponibilidade == Disponibilidade.DISPONIVEL

# ========= TESTES DE REPRESENTAÇÃO =========
def test_repr_item(item_mochila_escolar):
    """Teste para garantir a representação correta do item com repr"""
    texto = repr(item_mochila_escolar)
    assert "Item" in texto
    assert item_mochila_escolar.nome in texto
    assert item_mochila_escolar.tipo.value in texto
    assert item_mochila_escolar.disponibilidade.value in texto

def test_str_item(item_mochila_escolar):
    """Teste para garantir a representação legível do item com str"""
    texto = str(item_mochila_escolar)
    assert "Item" in texto
    assert item_mochila_escolar.nome in texto
    assert item_mochila_escolar.tipo.value in texto
    assert item_mochila_escolar.estado_conservacao.value in texto
    assert item_mochila_escolar.disponibilidade.value in texto
