from datetime import datetime
from typing import Optional

class Reserva:
    STATUS_VALIDOS = ['pendente', 'confirmada', 'cancelada', 'concluída']
    
    def __init__(self, reserva_id: int, beneficiario_id: int, item_id: int, doador_id: int, status_da_reserva: str, data_hora: datetime):
        self.reserva_id = reserva_id
        self.beneficiario_id = beneficiario_id
        self.item_id = item_id
        self.doador_id = doador_id
        self.status_da_reserva = status_da_reserva
        self.data_hora = data_hora
        self._retirada_id: Optional[int] = None

    @property
    def reserva_id(self) -> int:
        return self._reserva_id
    
    @reserva_id.setter
    def reserva_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID da reserva deve ser um inteiro positivo")
        self._reserva_id = value

    @property
    def beneficiario_id(self) -> int:
        return self._beneficiario_id
    
    @beneficiario_id.setter
    def beneficiario_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do beneficiário deve ser um inteiro positivo")
        self._beneficiario_id = value

    @property
    def item_id(self) -> int:
        return self._item_id
    
    @item_id.setter
    def item_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do item deve ser um inteiro positivo")
        self._item_id = value

    @property
    def doador_id(self) -> int:
        return self._doador_id
    
    @doador_id.setter
    def doador_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do doador deve ser um inteiro positivo")
        self._doador_id = value

    @property
    def status_da_reserva(self) -> str:
        return self._status_da_reserva

    @status_da_reserva.setter
    def status_da_reserva(self, novo_status: str):
        if novo_status.lower() not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use: {', '.join(self.STATUS_VALIDOS)}")
        self._status_da_reserva = novo_status.lower()

    @property
    def data_hora(self) -> datetime:
        return self._data_hora
    
    @data_hora.setter
    def data_hora(self, value: datetime):
        if not isinstance(value, datetime):
            raise TypeError("Data/hora deve ser um objeto datetime")
        self._data_hora = value

    @property
    def retirada_id(self) -> Optional[int]:
        return self._retirada_id

    @retirada_id.setter
    def retirada_id(self, retirada_id: int):
        if not isinstance(retirada_id, int) or retirada_id <= 0:
            raise ValueError("ID da retirada deve ser um inteiro positivo")
        self._retirada_id = retirada_id
        self._status_da_reserva = 'concluída'

    def __str__(self):
        return f"Reserva #{self._reserva_id} - Status: {self._status_da_reserva} - Data: {self._data_hora.strftime('%d/%m/%Y %H:%M')}"