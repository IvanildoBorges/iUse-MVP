-- ======================================================
-- CENÁRIO 1 — Reserva recusada pelo doador
-- ======================================================
-- Situação:
--      1. Mariana doa um item
--      2. Carlos tenta reservar
--      3. Mariana recusa a reserva
--      4. Não há entrega nem retirada
-- ======================================================

-- 1. Novo item doado (Mariana)
INSERT INTO ITEM (nome, tipo, descricao, estado_conservacao, id_ponto_coleta, id_doador)
VALUES
    ('Estojo Escolar', 'estojo', 'Estojo simples, pouco usado', 'bom', 2, 
    (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'mariana.a@aluno.ufca.edu.br'));

-- 2. Reserva criada pelo beneficiário
INSERT INTO RESERVA (id_beneficiario, id_item, id_doador)
VALUES
    ((SELECT id_usuario FROM BENEFICIARIO b
        JOIN USUARIO u ON u.id = b.id_usuario
        WHERE u.email = 'carlos.l@aluno.ufca.edu.br'),
    (SELECT id FROM ITEM 
        WHERE nome = 'Estojo Escolar'),
    (SELECT id_usuario FROM DOADOR d
        JOIN USUARIO u ON u.id = d.id_usuario
        WHERE u.email = 'mariana.a@aluno.ufca.edu.br'));

    -- 3. Reserva recusada
    UPDATE RESERVA
    SET status_da_reserva = 'recusada'
    WHERE id_item = (SELECT id FROM ITEM WHERE nome = 'Estojo Escolar');

-- 4. Item continua disponível. Não existe retirada nem avaliação


-- ======================================================
-- CENÁRIO 2 — Reserva aceita, mas item não retirado
-- ======================================================
-- Situação:
--      1. Ana doa um item
--      2. Carlos reserva
--      3. Ana aceita
--      4. Entrega acontece
--      5. Beneficiário não comparece
--      6. Sem retirada, sem avaliação
-- ======================================================

-- 1. Novo item doado (Ana)
INSERT INTO ITEM (nome, tipo, descricao, estado_conservacao, id_ponto_coleta, id_doador)
VALUES
('Caixa de Lápis de Cor', 'material', '12 lápis de cor seminovos', 'bom', 1,
(SELECT id_usuario FROM DOADOR d
    JOIN USUARIO u ON u.id = d.id_usuario
    WHERE u.email = 'ana.s@aluno.ufca.edu.br'));

-- 2. Reserva criada
INSERT INTO RESERVA (id_beneficiario, id_item, id_doador)
VALUES
((SELECT id_usuario FROM BENEFICIARIO b
    JOIN USUARIO u ON u.id = b.id_usuario
    WHERE u.email = 'carlos.l@aluno.ufca.edu.br'),
 (SELECT id FROM ITEM
    WHERE nome = 'Caixa de Lápis de Cor'),
 (SELECT id_usuario FROM DOADOR d
    JOIN USUARIO u ON u.id = d.id_usuario
    WHERE u.email = 'ana.s@aluno.ufca.edu.br'));

-- 3. Reserva aceita
UPDATE RESERVA
SET status_da_reserva = 'aceita'
WHERE id_item = (SELECT id FROM ITEM WHERE nome = 'Caixa de Lápis de Cor');

-- 4. Entrega realizada
INSERT INTO ENTREGA (id_item, id_doador, id_ponto_coleta)
VALUES
((SELECT id FROM ITEM
    WHERE nome = 'Caixa de Lápis de Cor'),
(SELECT id_usuario FROM DOADOR d
    JOIN USUARIO u ON u.id = d.id_usuario
    WHERE u.email = 'ana.s@aluno.ufca.edu.br'),
 1);

-- 5. Não existe retirada
-- 6. Logo, Sem avaliação e sem impacto registrado


-- ======================================================
-- CONSULTAS PARA VALIDAR OS CENÁRIOS
-- ======================================================
-- Reservas recusadas
SELECT r.id, i.nome, r.status_da_reserva
FROM RESERVA r
JOIN ITEM i ON i.id = r.id_item
WHERE r.status_da_reserva = 'recusada';

-- Reservas aceitas sem retirada
SELECT
    r.id AS reserva,
    i.nome AS item,
    r.status_da_reserva
FROM RESERVA r
JOIN ITEM i ON i.id = r.id_item
LEFT JOIN RETIRADA rt ON rt.id_reserva = r.id
WHERE r.status_da_reserva = 'aceita' AND rt.id IS NULL;