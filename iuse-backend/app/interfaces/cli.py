from backend.app.domain.models.Ponto_de_Coleta import Ponto_de_Coleta
from backend.app.services.autenticacao_service import AutenticacaoService
from backend.app.domain.models.Item import Item
from backend.app.domain.enums.tipo_item import TipoItem
from backend.app.domain.enums.estado_conservacao import EstadoConservacao

def iniciar_aplicacao():
    print("===== iUse – Sistema de Doação de Materias Escolares =====\n")

    # Lista de usuários registrados (para simplificar o exemplo)
    usuarios = []
    finalizar_execucao = False

    # Cadastro de usuários via input()
    while True:
        tipo_usuario = input("Digite o tipo de usuário (doador/beneficiario) ou 'sair' para encerrar: ").strip().lower()

        if tipo_usuario == 'sair':
            finalizar_execucao = True
            break

        if tipo_usuario not in ['doador', 'beneficiario']:
            print("Tipo de usuário inválido! Escolha 'doador' ou 'beneficiario'!")
            continue

        nome = input("\nAgora digite o nome do usuário: ").strip()
        email = input("Digite o e-mail do usuário: ").strip()
        senha = input("Digite a senha do usuário: ").strip()

        # Registrando o usuário
        try:
            usuario = AutenticacaoService.registrar_usuario(tipo_usuario, nome, email, senha)
            usuarios.append(usuario)
            print(f"\n{tipo_usuario.capitalize()} '{nome}' cadastrado com sucesso!\n")
        except ValueError as e:
            print(f"Erro no cadastro: {e}")
            continue
    
    if finalizar_execucao and len(usuarios) > 0:
        # Fluxo de autenticação
        print("\n===== Autenticação de Usuário =====")
        email_login = input("Digite o e-mail para login: ").strip()
        senha_login = input("Digite a senha para login: ").strip()

        usuario_logado = AutenticacaoService.autenticar_por_email(email_login, senha_login, usuarios)

        if usuario_logado:
            print(f"\nLogin bem-sucedido! Bem-vindo, {usuario_logado.nome}")
        else:
            print("\nFalha no login!  Verifique as credenciais.")

        ponto = Ponto_de_Coleta(
            id=1,
            endereco_id=1,
            nome_do_local="CSU - Centro Social Urbano",
            endereco="Rua A, 123",
            cidade="Várzea Alegre",
            estado="CE",
            cep="63540-000",
            latitude=-6.9712,
            longitude=-39.5531
        )

        doador_teste = AutenticacaoService.registrar_usuario("doador", "Fulano", "ful@mail.com", "123456")

        item = Item(
            nome="Caderno Universitário",
            categoria=TipoItem.CADERNO,
            descricao="Caderno com poucas folhas usadas",
            estado_conservacao=EstadoConservacao.BOM,
            id_ponto_coleta=ponto.id,
            id_doador=doador_teste.id
        )

        print(f"Item cadastrado com sucesso!", item)
        
        # reserva
        # entrega
        # retirada
        # impacto

    print("\nFluxo concluído com sucesso!")
