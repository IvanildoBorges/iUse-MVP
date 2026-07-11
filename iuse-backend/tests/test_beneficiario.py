import pytest
from backend.app.domain.models.Beneficiario import Beneficiario

# ========= FIXTURES =========
@pytest.fixture
def beneficiario_valido():
    return Beneficiario(nome="Ana Souza", email="ana@email.com", senha="abcdef")

# ========= TESTES DE CRIAÇÃO =========
def test_criar_beneficiario_com_dados_validos(beneficiario_valido):
    assert beneficiario_valido.nome == "Ana Souza"
    assert beneficiario_valido.email == "ana@email.com"
    assert beneficiario_valido.id is not None

def test_beneficiario_herda_de_usuario(beneficiario_valido):
    assert beneficiario_valido.verificar_senha("abcdef") is True
    assert beneficiario_valido.verificar_senha("errada") is False

# ========= TESTES DE VALIDAÇÕES =========
def test_beneficiario_email_invalido():
    with pytest.raises(ValueError, match="E-mail inválido"):
        Beneficiario(nome="Ana", email="email_invalido", senha="123456")

def test_beneficiario_nome_invalido():
    with pytest.raises(ValueError, match="Nome inválido"):
        Beneficiario(nome=" ", email="ana@email.com", senha="123456")

def test_beneficiario_senha_curta():
    with pytest.raises(ValueError, match="Senha deve ter no mínimo 6 caracteres"):
        Beneficiario(nome="Ana", email="ana@email.com", senha="123")

# ========= TESTES DE REPRESENTAÇÃO =========
def test_repr_beneficiario(beneficiario_valido):
    texto = repr(beneficiario_valido)
    assert "Beneficiario" in texto
    assert beneficiario_valido.nome in texto

def test_str_beneficiario(beneficiario_valido):
    texto = str(beneficiario_valido)
    assert "Beneficiario:" in texto