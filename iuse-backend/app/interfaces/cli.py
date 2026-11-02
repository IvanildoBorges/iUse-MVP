from app.domain.models.Ponto_de_Coleta import Ponto_de_Coleta
from app.services.autenticacao_service import AutenticacaoService
from app.domain.models.Item import Item
from app.domain.enums.tipo_item import TipoItem
from app.domain.enums.estado_conservacao import EstadoConservacao

def iniciar_aplicacao():
    print("===== iUse – Sistema de Doação de Materias Escolares =====\n")
    print("Servidor iniciado com sucesso!\n")