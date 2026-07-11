from backend.app.domain.models.Usuario import Usuario
from backend.app.domain.models.Doador import Doador
from backend.app.domain.models.Beneficiario import Beneficiario

class AutenticacaoService:
    @staticmethod
    def login(usuario: Usuario, senha: str) -> bool:
        """
        Realiza o processo de autenticação de um usuário (simples, sem API e token).
        
        Parâmetros:
        - usuario: Instância de Usuario, Doador ou Beneficiario.
        - senha: Senha fornecida pelo usuário durante o login.
        
        Retorna:
        - bool: True se a autenticação for bem-sucedida, False caso contrário.
        """
        if usuario.verificar_senha(senha):
            return True
        return False

    @staticmethod
    def autenticar_por_email(usuario_email: str, senha: str, usuarios: list[Usuario]) -> Usuario | None:
        """
        Busca e autentica um usuário com base no e-mail.
        
        Parâmetros:
        - usuario_email: E-mail do usuário.
        - senha: Senha fornecida para autenticação.
        - usuarios: Lista de instâncias de Usuario (ou derivados).
        
        Retorna:
        - Usuario: O usuário autenticado ou None se não encontrado ou falha na senha.
        """
        for usuario in usuarios:
            if usuario.email == usuario_email:
                if AutenticacaoService.login(usuario, senha):
                    return usuario
        return None

    @staticmethod
    def registrar_usuario(tipo: str, nome: str, email: str, senha: str) -> Usuario:
        """
        Registra um novo usuário (Doador ou Beneficiário) no sistema.
        
        Parâmetros:
        - tipo: Tipo de usuário ('doador' ou 'beneficiario').
        - nome: Nome do usuário.
        - email: E-mail do usuário.
        - senha: Senha do usuário.
        
        Retorna:
        - Usuario: O objeto do tipo Doador ou Beneficiario.
        """
        if tipo == "doador":
            return Doador(nome, email, senha)
        elif tipo == "beneficiario":
            return Beneficiario(nome, email, senha)
        else:
            raise ValueError("Tipo de usuário inválido! Deve ser 'doador' ou 'beneficiario'!")

