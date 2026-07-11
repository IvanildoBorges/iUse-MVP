import pytest
from backend.app.domain.models.Doador import Doador

# ========= FIXTURES =========
@pytest.fixture
def doador_valido():
    return Doador(nome="João Silva", email="joao@email.com", senha="123456", reputacao=4.0)

# ========= TESTES DE CRIAÇÃO =========
def test_criar_doador_com_dados_validos(doador_valido):
    assert doador_valido.nome == "João Silva"
    assert doador_valido.email == "joao@email.com"
    assert doador_valido.reputacao == 4.0
    assert doador_valido.id is not None

def test_doador_herda_de_usuario(doador_valido):
    # Verifica se métodos herdados funcionam
    assert doador_valido.verificar_senha("123456") is True
    assert doador_valido.verificar_senha("senha_errada") is False

# ========= TESTES DE REPUTAÇÃO =========
def test_reputacao_nao_pode_ser_negativa():
    with pytest.raises(ValueError, match="Reputação não pode ser negativa"):
        Doador(nome="Maria", email="maria@email.com", senha="123456", reputacao=-1)

def test_atualizar_reputacao_com_avaliacao_valida(doador_valido):
    doador_valido.atualizar_reputacao(5)    # reputacao inicial = 4.0
    assert doador_valido.reputacao == 4.5   # (4.0 + 5) / 2 = 4.5

def test_atualizar_reputacao_com_avaliacao_invalida(doador_valido):
    with pytest.raises(ValueError, match="Avaliação deve estar entre 1 e 5"):
        doador_valido.atualizar_reputacao(6)

# ========= TESTES DE REPRESENTAÇÃO =========
def test_repr_doador(doador_valido):
    texto = repr(doador_valido)
    assert "Doador" in texto
    assert doador_valido.nome in texto

def test_str_doador(doador_valido):
    texto = str(doador_valido)
    assert "Doador:" in texto