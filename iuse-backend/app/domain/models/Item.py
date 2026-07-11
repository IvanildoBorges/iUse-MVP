from datetime import datetime, UTC
from uuid import uuid4
from backend.app.utils.validadores import validar_uuid
from backend.app.domain.enums.tipo_item import TipoItem
from backend.app.domain.enums.estado_conservacao import EstadoConservacao
from backend.app.domain.enums.disponibilidade import Disponibilidade

class Item:
    def __init__(
        self,
        nome: str,
        categoria: TipoItem,
        descricao: str,
        estado_conservacao: EstadoConservacao,
        id_ponto_coleta: int,
        id_doador: str,
        disponibilidade: Disponibilidade = Disponibilidade.DISPONIVEL,
        id: str | None = None,
        criado_em: datetime | None = None
    ):
        self.__id = validar_uuid(id if id else str(uuid4()))    # Identidade
        self.nome = nome
        self.tipo = categoria
        self.descricao = descricao
        self.estado_conservacao = estado_conservacao
        self.disponibilidade = disponibilidade
        self.id_ponto_coleta = id_ponto_coleta
        self.id_doador = validar_uuid(id_doador)
        self.__criado_em = criado_em if criado_em else datetime.now(UTC)

    # ========= ID =========
    @property
    def id(self) -> str:
        return self.__id

    # ========= CRIADO EM =========
    @property
    def criado_em(self) -> datetime:
        return self.__criado_em

    # ========= NOME =========
    @property
    def nome(self) -> str:
        return self._nome
    @nome.setter
    def nome(self, value: str):
        if not value or len(value.strip()) < 2:
            raise ValueError("Nome do item deve conter ao menos 2 caracteres!")
        self._nome = value.strip()

    # ========= TIPO =========
    @property
    def tipo(self) -> TipoItem:
        return self._tipo
    @tipo.setter
    def tipo(self, value: TipoItem):
        if not isinstance(value, TipoItem):
            raise ValueError("Tipo inválido para o item!")
        self._tipo = value

    # ========= DESCRIÇÃO =========
    @property
    def descricao(self) -> str:
        return self._descricao
    @descricao.setter
    def descricao(self, value: str):
        if not value or not value.strip():
            raise ValueError("Descrição não pode estar vazia!")
        self._descricao = value.strip()

    # ========= ESTADO DE CONSERVAÇÃO =========
    @property
    def estado_conservacao(self) -> EstadoConservacao:
        return self._estado_conservacao
    @estado_conservacao.setter
    def estado_conservacao(self, value: EstadoConservacao):
        if not isinstance(value, EstadoConservacao):
            raise ValueError("Estado de conservação inválido!")
        self._estado_conservacao = value

    # ========= DISPONIBILIDADE =========
    @property
    def disponibilidade(self) -> Disponibilidade:
        return self._disponibilidade
    @disponibilidade.setter
    def disponibilidade(self, value: Disponibilidade):
        if not isinstance(value, Disponibilidade):
            raise ValueError("Disponibilidade inválida!")
        self._disponibilidade = value

    # ========= FOREIGN KEYS =========
    @property
    def id_ponto_coleta(self) -> int:
        return self._id_ponto_coleta
    @id_ponto_coleta.setter
    def id_ponto_coleta(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do ponto de coleta deve ser um inteiro positivo!")
        self._id_ponto_coleta = value

    @property
    def id_doador(self) -> str:
        return self._id_doador
    @id_doador.setter
    def id_doador(self, value: str):
        self._id_doador = validar_uuid(value)

    # ========= REGRAS DE NEGÓCIO =========
    def tornar_indisponivel(self):
        self._disponibilidade = Disponibilidade.INDISPONIVEL

    def tornar_disponivel(self):
        self._disponibilidade = Disponibilidade.DISPONIVEL

    # ========= REPRESENTAÇÕES =========
    def __repr__(self):
        return (
            f"Item(id='{self.id}', nome='{self.nome}', "
            f"tipo='{self.tipo.value}', "
            f"disponibilidade='{self.disponibilidade.value}')"
        )

    def __str__(self):
        return (
            f"Item: {self.nome} | {self.tipo.value} | "
            f"{self.estado_conservacao.value} | "
            f"{self.disponibilidade.value}"
        )