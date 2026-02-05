-- Restrição: email único
-- Índice para buscas rápidas por nome 
CREATE TABLE USUARIO (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL UNIQUE,
  senha_hash VARCHAR(255) NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE INDEX idx_usuario_nome ON USUARIO (nome);

-- Especialização de USUARIO
--Integridade: se o usuário for excluído, o beneficiário também
CREATE TABLE BENEFICIARIO (
  id_usuario INT PRIMARY KEY,
  FOREIGN KEY (id_usuario) REFERENCES USUARIO (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Especialização de USUARIO
-- Reputação é a média de avaliações obtida por uma VIEW
CREATE TABLE DOADOR (
  id_usuario INT PRIMARY KEY,
  FOREIGN KEY (id_usuario) REFERENCES USUARIO (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Índice: (cidade, estado) para buscas geográficas
CREATE TABLE PONTO_COLETA (
  id SERIAL PRIMARY KEY,
  nome_local VARCHAR(100) NOT NULL,
  endereco VARCHAR(200) NOT NULL,
  cidade VARCHAR(100) NOT NULL,
  estado CHAR(2) NOT NULL,
  cep CHAR(8) NOT NULL,
  latitude DECIMAL(9, 6),
  longitude DECIMAL(9, 6)
);
CREATE INDEX idx_ponto_coleta_localizacao ON PONTO_COLETA (cidade, estado);

-- Restrição: cada item pertence a um único doador e ponto de coleta
-- Índice: (tipo, disponibilidade) para filtros rápidos
CREATE TABLE ITEM (
  id SERIAL PRIMARY KEY,
  nome VARCHAR(100) NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  descricao TEXT,
  estado_conservacao VARCHAR(20) CHECK (
    estado_conservacao IN ('novo', 'bom', 'regular', 'ruim')
  ),
  disponibilidade BOOLEAN DEFAULT TRUE,
  id_ponto_coleta INT NOT NULL,
  id_doador INT NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_ponto_coleta) REFERENCES PONTO_COLETA (id) ON DELETE RESTRICT ON UPDATE CASCADE,
  FOREIGN KEY (id_doador) REFERENCES DOADOR (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_item_tipo_disponibilidade ON ITEM (tipo, disponibilidade);

-- Cardinalidade ajustada: item pode ter nenhuma ou muitas imagens
CREATE TABLE IMAGEM (
  id SERIAL PRIMARY KEY,
  id_item INT NOT NULL,
  imagem BYTEA NOT NULL,
  texto_alternativo VARCHAR(255),
  FOREIGN KEY (id_item) REFERENCES ITEM (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Restrição: garante que um item só pode ter uma reserva ativa
-- Índice para status da reserva 
CREATE TABLE RESERVA (
  id SERIAL PRIMARY KEY,
  id_beneficiario INT NOT NULL,
  id_item INT NOT NULL UNIQUE,
  id_doador INT NOT NULL,
  status_da_reserva VARCHAR(20) CHECK (
    status_da_reserva IN ('pendente', 'aceita', 'recusada', 'concluida')
  ) DEFAULT 'pendente',
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_beneficiario) REFERENCES BENEFICIARIO (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_item) REFERENCES ITEM (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_doador) REFERENCES DOADOR (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_reserva_status ON RESERVA (status_da_reserva);

-- 
CREATE TABLE ENTREGA (
  id SERIAL PRIMARY KEY,
  id_item INT NOT NULL,
  id_doador INT NOT NULL,
  id_ponto_coleta INT NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_item) REFERENCES ITEM (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_doador) REFERENCES DOADOR (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_ponto_coleta) REFERENCES PONTO_COLETA (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Restrição: código único para validação da retirada
CREATE TABLE RETIRADA (
  id SERIAL PRIMARY KEY,
  codigo_retirada CHAR(10) UNIQUE NOT NULL,
  id_reserva INT NOT NULL,
  id_beneficiario INT NOT NULL,
  id_ponto_coleta INT NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_reserva) REFERENCES RESERVA (id) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_beneficiario) REFERENCES BENEFICIARIO (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_ponto_coleta) REFERENCES PONTO_COLETA (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Restrição: uma retirada pode ter no máximo uma avaliação
-- Índice para busca por nota 
CREATE TABLE AVALIACAO (
  id SERIAL PRIMARY KEY,
  nota SMALLINT CHECK (nota BETWEEN 1 AND 5),
  comentario TEXT,
  id_beneficiario INT NOT NULL,
  id_retirada INT UNIQUE,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_beneficiario) REFERENCES BENEFICIARIO (id_usuario) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_retirada) REFERENCES RETIRADA (id) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE INDEX idx_avaliacao_nota ON AVALIACAO (nota);

-- Cardinalidade ajustada: impacto vinculado ao item, não ao beneficiário
CREATE TABLE IMPACTO (
  id SERIAL PRIMARY KEY,
  qtd_economia DECIMAL(10, 2) DEFAULT 0.0,
  qtd_residuos_evitados DECIMAL(10, 2) DEFAULT 0.0,
  id_item INT NOT NULL,
  criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (id_item) REFERENCES ITEM (id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- VIEW para reputação do doador
CREATE VIEW view_reputacao_doador AS
SELECT
  d.id_usuario AS id_doador,
  u.nome AS nome_doador,
  AVG(a.nota) AS reputacao
FROM
  DOADOR d
  JOIN USUARIO u ON d.id_usuario = u.id
  JOIN ITEM i ON i.id_doador = d.id_usuario
  JOIN RESERVA r ON r.id_item = i.id
  JOIN RETIRADA rt ON rt.id_reserva = r.id
  LEFT JOIN AVALIACAO a ON a.id_retirada = rt.id
GROUP BY
  d.id_usuario,
  u.nome;
