import re

class Ponto_de_Coleta:
    def __init__(self, id: int, endereco_id: int, nome_do_local: str, endereco: str, cidade: str, estado: str, cep: str, latitude: float, longitude: float):
        self.id = id
        self.endereco_id = endereco_id
        self.nome_do_local = nome_do_local
        self.endereco = endereco
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.latitude = latitude
        self.longitude = longitude

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do Ponto de Coleta deve ser um inteiro positivo!")
        self._id = value

    @property
    def endereco_id(self) -> int:
        return self._endereco_id
    
    @endereco_id.setter
    def endereco_id(self, value: int):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID do endereço deve ser um inteiro positivo")
        self._endereco_id = value

    @property
    def nome_do_local(self) -> str:
        return self._nome_do_local
    
    @nome_do_local.setter
    def nome_do_local(self, value: str):
        if not value or not value.strip():
            raise ValueError("Nome do local não pode estar vazio")
        self._nome_do_local = value.strip()

    @property
    def cep(self) -> str:
        return self._cep
    
    @cep.setter
    def cep(self, value: str):
        # Remove caracteres não numéricos
        cep_limpo = re.sub(r'\D', '', value)
        if len(cep_limpo) != 8:
            raise ValueError("CEP deve conter 8 dígitos")
        # Formata como XXXXX-XXX
        self._cep = f"{cep_limpo[:5]}-{cep_limpo[5:]}"

    @property
    def estado(self) -> str:
        return self._estado
    
    @estado.setter
    def estado(self, value: str):
        estados_validos = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
                          'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
                          'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        value_upper = value.upper().strip()
        if value_upper not in estados_validos:
            raise ValueError(f"Estado inválido. Use uma sigla válida: {', '.join(estados_validos)}")
        self._estado = value_upper

    @property
    def latitude(self) -> float:
        return self._latitude
    
    @latitude.setter
    def latitude(self, value: float):
        if not -90 <= value <= 90:
            raise ValueError("Latitude deve estar entre -90 e 90")
        self._latitude = value

    @property
    def longitude(self) -> float:
        return self._longitude
    
    @longitude.setter
    def longitude(self, value: float):
        if not -180 <= value <= 180:
            raise ValueError("Longitude deve estar entre -180 e 180")
        self._longitude = value

    @property
    def endereco(self) -> str:
        return self._endereco
    
    @endereco.setter
    def endereco(self, value: str):
        if not value or not value.strip():
            raise ValueError("Endereço não pode estar vazio")
        self._endereco = value.strip()

    @property
    def cidade(self) -> str:
        return self._cidade
    
    @cidade.setter
    def cidade(self, value: str):
        if not value or not value.strip():
            raise ValueError("Cidade não pode estar vazia")
        self._cidade = value.strip()

    @property
    def endereco_completo(self) -> str:
        return f"{self._endereco}, {self._cidade}, {self._estado}, CEP: {self._cep}"

    @property
    def coordenadas(self) -> tuple:
        return (self._latitude, self._longitude)

    def __str__(self):
        return f"Ponto de Coleta: {self._nome_do_local} - {self.endereco_completo}"
    