-- ====================================================
--  População de tabelas (INSERTS)
-- ====================================================

-- USUÁRIOS
INSERT INTO USUARIO (nome, email, senha_hash) VALUES
('Ana Souza', 'ana.s@aluno.ufca.edu.br', 'hash_ana'),
('Carlos Lima', 'carlos.l@aluno.ufca.edu.br', 'hash_carlos'),
('Mariana Alves', 'mariana.a@aluno.ufca.edu.br', 'hash_mariana');

-- Doadores: Ana e Mariana
INSERT INTO DOADOR (id_usuario)
    SELECT id 
    FROM USUARIO
    WHERE email IN ('ana.s@aluno.ufca.edu.br', 'mariana.a@aluno.ufca.edu.br');

-- Beneficiários: Carlos e Mariana
INSERT INTO BENEFICIARIO (id_usuario)
    SELECT id 
    FROM USUARIO
    WHERE email IN ('carlos.l@aluno.ufca.edu.br', 'mariana.a@aluno.ufca.edu.br');

-- PONTOS DE COLETA
INSERT INTO PONTO_COLETA (nome_local, endereco, cidade, estado, cep, latitude, longitude)
VALUES
    ('Escola Municipal Esperança', 'Rua das Flores, 100', 'São Paulo', 'SP', '01001000', -23.550520, -46.633308),
    ('Centro Comunitário Saber', 'Av. Central, 500', 'Campinas', 'SP', '13010000', -22.905560, -47.060830);

-- ITENS (UUID)
INSERT INTO ITEM (nome, tipo, descricao, estado_conservacao, id_ponto_coleta, id_doador)
VALUES
    ('Mochila Escolar', 'mochila', 'Mochila infantil em bom estado', 'bom', 1,
        (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'ana.s@aluno.ufca.edu.br')),
    ('Kit de Cadernos', 'caderno', 'Três cadernos universitários usados', 'regular', 2,
        (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'mariana.a@aluno.ufca.edu.br'));

-- IMAGENS DOS ITENS
INSERT INTO IMAGEM (id_item, imagem, texto_alternativo)
    SELECT id, decode('FFD8FFE0', 'hex'), 'Imagem ilustrativa do item'
    FROM ITEM;

-- RESERVA
INSERT INTO RESERVA (id_beneficiario, id_item, id_doador)
VALUES
    ((SELECT id_usuario FROM BENEFICIARIO b
        JOIN USUARIO u ON u.id = b.id_usuario
        WHERE u.email = 'carlos.l@aluno.ufca.edu.br'),

    (SELECT id FROM ITEM
        WHERE nome = 'Mochila Escolar'),

    (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'ana.s@aluno.ufca.edu.br'));

-- ENTREGA
INSERT INTO ENTREGA (id_item, id_doador, id_ponto_coleta)
VALUES
    ((SELECT id FROM ITEM 
        WHERE nome = 'Mochila Escolar'),
    (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'ana.s@aluno.ufca.edu.br'),
    1);

-- RETIRADA
INSERT INTO RETIRADA (codigo_retirada, id_reserva, id_beneficiario, id_ponto_coleta)
VALUES
    ('RET123ABC9',
    (SELECT id FROM RESERVA LIMIT 1),
    (SELECT id_usuario FROM BENEFICIARIO b
        JOIN USUARIO u ON u.id = b.id_usuario
        WHERE u.email = 'carlos.l@aluno.ufca.edu.br'),
    1);

-- AVALIAÇÃO
INSERT INTO AVALIACAO (nota, comentario, id_beneficiario, id_retirada)
VALUES
    (5,
    'Material em ótimo estado, ajudou muito!',
    (SELECT id_usuario FROM BENEFICIARIO b
        JOIN USUARIO u ON u.id = b.id_usuario
        WHERE u.email = 'carlos.l@aluno.ufca.edu.br'),
    (SELECT id FROM RETIRADA 
        LIMIT 1));

-- IMPACTO
INSERT INTO IMPACTO (qtd_economia, qtd_residuos_evitados, id_item)
VALUES
    (120.00, 
    2.5,
    (SELECT id FROM ITEM 
        WHERE nome = 'Mochila Escolar'));