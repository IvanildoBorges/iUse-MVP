from datetime import datetime, UTC
import pytest
from backend.app.domain.models.Usuario import Usuario

# ========= FIXTURES =========
@pytest.fixture
def usuario_valido():
    """Usuário padrão válido para reutilização nos testes"""
    return Usuario(nome="João Silva", email="joao@email.com", senha="senha123")

# ========= TESTES DE CRIAÇÃO =========
def test_criar_usuario_valido(usuario_valido):
    assert usuario_valido.nome == "João Silva"
    assert usuario_valido.email == "joao@email.com"
    assert usuario_valido.id is not None
    assert usuario_valido.criado_em is not None

def test_criar_usuario_com_uuid_customizado():
    usuario = Usuario(
        nome="Ana Souza",
        email="ana@email.com",
        senha="senha123",
        id="550e8400-e29b-41d4-a716-446655440000"
    )
    assert usuario.id == "550e8400-e29b-41d4-a716-446655440000"

def test_criar_usuario_com_data_customizada():
    data = datetime(2024, 1, 1, tzinfo=UTC)
    usuario = Usuario(nome="Carlos", email="carlos@email.com", senha="senha123", criado_em=data)
    assert usuario.criado_em == data

# ========= TESTES DE VALIDAÇÃO =========
def test_nome_invalido():
    with pytest.raises(ValueError, match="Nome inválido"):
        Usuario(nome="J", email="teste@email.com", senha="senha123")

def test_email_invalido():
    with pytest.raises(ValueError, match="E-mail inválido"):
        Usuario(nome="João", email="emailinvalido", senha="senha123")

def test_email_convertido_para_lowercase():
    usuario = Usuario(nome="João", email="JOAO@EMAIL.COM", senha="senha123")
    assert usuario.email == "joao@email.com"

def test_senha_invalida_curta():
    with pytest.raises(ValueError, match="Senha deve ter no mínimo 6 caracteres"):
        Usuario(nome="João", email="joao@email.com", senha="123")

def test_uuid_invalido():
    with pytest.raises(ValueError, match="ID deve ser um UUID válido"):
        Usuario(nome="Ana", email="ana@email.com", senha="senha123", id="uuid-invalido")

# ========= TESTES DE SENHA E AUTENTICAÇÃO =========
def test_verificar_senha_correta(usuario_valido):
    assert usuario_valido.verificar_senha("senha123") is True

def test_verificar_senha_incorreta(usuario_valido):
    assert usuario_valido.verificar_senha("outrasenha") is False

def test_senha_nao_pode_ser_acessada(usuario_valido):
    with pytest.raises(AttributeError, match="Senha não pode ser acessada"):
        _ = usuario_valido.senha

# ========= TESTES DE REPRESENTAÇÃO =========
def test_repr_usuario(usuario_valido):
    texto = repr(usuario_valido)
    assert "Usuario" in texto
    assert usuario_valido.nome in texto
    assert usuario_valido.email in texto

def test_str_usuario(usuario_valido):
    texto = str(usuario_valido)
    assert "Usuário:" in texto
    assert usuario_valido.nome in texto