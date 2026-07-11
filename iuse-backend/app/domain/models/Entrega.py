from datetime import datetime

class Entrega:
    def __init__(self, entrega_id: int, item_id: int, doador_id: int, ponto_coleta_id: int, data_hora: datetime):
        self.entrega_id = entrega_id
        self.item_id = item_id
        self.doador_id = doador_id
        self.ponto_coleta_id = ponto_coleta_id
        self.data_hora = data_hora

    @property
    def entrega_id(self) -> int:
        return self._entrega_id
    
    @entrega_id.setter
    def entrega_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID da entrega deve ser um inteiro positivo")
        self._entrega_id = value

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
    def ponto_coleta_id(self) -> int:
        return self._ponto_coleta_id
    
    @ponto_coleta_id.setter
    def ponto_coleta_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do ponto de coleta deve ser um inteiro positivo")
        self._ponto_coleta_id = value

    @property
    def data_hora(self) -> datetime:
        return self._data_hora
    
    @data_hora.setter
    def data_hora(self, value: datetime):
        if not isinstance(value, datetime):
            raise TypeError("Data/hora deve ser um objeto datetime")
        if value > datetime.now():
            raise ValueError("Data/hora da entrega não pode ser no futuro")
        self._data_hora = value

    def __str__(self):
        return f"Entrega #{self._entrega_id} - Item: {self._item_id} - Data: {self._data_hora.strftime('%d/%m/%Y %H:%M')}"