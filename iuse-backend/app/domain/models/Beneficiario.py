from backend.app.domain.models.Usuario import Usuario

class Beneficiario(Usuario):
    def __init__(self, nome: str, email: str, senha: str):
        super().__init__(nome, email, senha)

    # ===== Representações =====
    def __repr__(self):
        return (f"Beneficiario(id_usuario='{self.id}', nome='{self.nome}')")

    def __str__(self):
        return f"Beneficiario: {self.nome}"