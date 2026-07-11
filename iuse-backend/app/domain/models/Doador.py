from backend.app.domain.models.Usuario import Usuario
from backend.app.utils.validadores import avaliar_estrelas

class Doador(Usuario):
    def __init__(self, nome: str, email: str, senha: str, reputacao: float = 0.0):
        super().__init__(nome, email, senha)
        self.reputacao = reputacao

    # ===== REPUTAÇÃO =====
    @property
    def reputacao(self) -> float:
        return self._reputacao
    @reputacao.setter
    def reputacao(self, valor: float):
        if valor < 0:
            raise ValueError("Reputação não pode ser negativa!")
        self._reputacao = round(valor, 1)

    # ===== Regras de negócio =====
    def atualizar_reputacao(self, nova_avaliacao: int):
        """Atualiza reputação com base em uma nova avaliação (1 a 5)"""
        self._reputacao = avaliar_estrelas(self.reputacao, nova_avaliacao) 

    # ===== Representações =====
    def __repr__(self):
        return (f"Doador(id='{self.id}', nome='{self.nome}', reputacao={self.reputacao})")

    def __str__(self):
        return f"Doador: {self.nome}, {self.reputacao}"