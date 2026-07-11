from datetime import datetime, UTC
from uuid import uuid4
import hashlib
from backend.app.utils.validadores import (validar_email, validar_nome, validar_uuid)
from backend.app.domain.mixins.autenticavel_mixin import AutenticavelMixin

class Usuario(AutenticavelMixin):
    def __init__(self, nome: str, email: str, senha: str, id: str | None = None, criado_em: datetime | None = None):
        # ===== ID e criação com validadores =====
        self.__id = validar_uuid(id if id else str(uuid4()))
        self.nome = nome    # setter usa validar_nome
        self.email = email  # setter usa validar_email
        self.senha = senha  # setter gera hash da senha
        self.__criado_em = criado_em if criado_em else datetime.now(UTC)

    # ===== ID =====
    @property
    def id(self) -> str:
        return self.__id

    # ===== CRIADO_EM =====
    @property
    def criado_em(self) -> datetime:
        return self.__criado_em

    # ===== NOME =====
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, valor: str):
        self._nome = validar_nome(valor)

    # ===== EMAIL =====
    @property
    def email(self) -> str:
        return self._email
    @email.setter
    def email(self, valor: str):
        self._email = validar_email(valor)

    # ===== SENHA =====
    @property
    def senha(self):
        raise AttributeError("Senha não pode ser acessada!")
    @senha.setter
    def senha(self, valor: str):
        if len(valor) < 6:
            raise ValueError("Senha deve ter no mínimo 6 caracteres!")
        self.__senha_hash = self.__gerar_hash(valor)

    def __gerar_hash(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()

    # Método exigido pelo mixin
    def verificar_senha(self, senha_digitada: str) -> bool:
        return self.__senha_hash == self.__gerar_hash(senha_digitada)

    # ===== Representações =====
    def __repr__(self):
        return f"Usuario(id='{self.id}', nome='{self.nome}', email='{self.email}')"

    def __str__(self):
        return f"Usuário: {self.nome}, {self.email}"