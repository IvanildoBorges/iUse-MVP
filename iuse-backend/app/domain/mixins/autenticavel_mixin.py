from abc import ABC, abstractmethod

class AutenticavelMixin(ABC):
    """
    Mixin que define o contrato de autenticação para usuários.
    Qualquer classe que herde deste mixin deve implementar o método:
    - verificar_senha(senha: str) -> bool
    """

    @abstractmethod
    def verificar_senha(self, senha: str) -> bool:
        """
        Método abstrato que deve ser implementado para verificar e 
        retornar True se a senha fornecida estiver correta.
        """
        pass
