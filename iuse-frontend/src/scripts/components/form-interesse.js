const TEMPO_ABERTURA = 3000;

// Cria o fundo do modal.
function criarSobreposicao() {
  const sobreposicao = document.createElement("div");
  sobreposicao.className = "sobreposicao-doacao";
  sobreposicao.hidden = true;
  document.body.appendChild(sobreposicao);
  return sobreposicao;
}

// Abre o formulário.
function abrirFormulario(secao, sobreposicao, aoAbrir) {
  secao.hidden = false;
  sobreposicao.hidden = false;
  aoAbrir?.();
  requestAnimationFrame(() => {
    secao.classList.add("aberto");
    sobreposicao.classList.add("visivel");
  });
}

// Fecha com deslize.
function fecharFormulario(secao, sobreposicao) {
  secao.classList.remove("aberto");
  secao.classList.add("fechando");
  sobreposicao.classList.remove("visivel");

  secao.addEventListener(
    "animationend",
    () => {
      secao.hidden = true;
      secao.classList.remove("fechando");
      sobreposicao.hidden = true;
    },
    { once: true },
  );
}

// Valida campos e formato.
function configurarValidacao(formulario, aoEnviarSucesso) {
  const mensagem = formulario.querySelector(".retorno-formulario");
  const camposObrigatorios = formulario.querySelectorAll("[required]");
  const email = formulario.querySelector("#email-doador");

  formulario.querySelectorAll("input, select, textarea").forEach((campo) => {
    campo.addEventListener("blur", () => {
      campo.classList.toggle("invalido", !campo.checkValidity());
      campo.classList.toggle("valido", campo.checkValidity());
    });

    campo.addEventListener("input", () => {
      campo.classList.remove("invalido");
    });
  });

  formulario.addEventListener("submit", (event) => {
    event.preventDefault();
    mensagem.className = "retorno-formulario";

    const campoVazio = [...camposObrigatorios].find(
      (campo) => !campo.value.trim(),
    );

    if (campoVazio) {
      campoVazio.classList.add("invalido");
      mensagem.textContent = "Preencha todos os campos obrigatórios.";
      mensagem.classList.add("erro");
      campoVazio.focus();
      return;
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
      email.classList.add("invalido");
      mensagem.textContent = "Digite um e-mail válido para continuar.";
      mensagem.classList.add("erro");
      email.focus();
      return;
    }

    mensagem.textContent = "Interesse enviado! Obrigado por contribuir.";
    mensagem.classList.add("sucesso");
    formulario.querySelectorAll("input, select, textarea").forEach((campo) => {
      campo.classList.add("valido");
    });
    formulario.classList.add("enviado");
    aoEnviarSucesso?.();
  });
}

// Bloqueia o redimensionamento.
function bloquearRedimensionamento(formulario) {
  const areaTexto = formulario.querySelector("#mensagem-doacao");

  if (areaTexto) {
    areaTexto.style.resize = "none";
  }
}

// Configura ajuda e controles.
export default function inicializarFormularioDoacao() {
  const secao = document.querySelector("#formulario-doacao");
  const formulario = document.querySelector("#formulario-interesse");
  const botaoChat = document.querySelector(".botao-chat-doacao");
  const botaoFechar = document.querySelector(".fechar-doacao");
  const botaoAjuda = document.querySelector(".botao-ajuda-doacao");
  const conteudoAjuda = document.querySelector("#conteudo-ajuda-doacao");

  if (!secao || !formulario || !botaoChat || !botaoFechar) {
    return;
  }

  if (secao.dataset.inicializado === "true") {
    return;
  }

  secao.dataset.inicializado = "true";
  const sobreposicao = criarSobreposicao();
  const botaoEnvio = formulario.querySelector(".envio-doacao");
  let temporizadorFechamento;

  const restaurarFormulario = () => {
    clearInterval(temporizadorFechamento);
    formulario.reset();
    formulario.classList.remove("enviado");
    formulario.querySelectorAll("input, select, textarea").forEach((campo) => {
      campo.classList.remove("valido", "invalido");
    });
    const mensagem = formulario.querySelector(".retorno-formulario");
    mensagem.className = "retorno-formulario";
    mensagem.textContent = "";
    if (botaoEnvio) {
      botaoEnvio.disabled = false;
      botaoEnvio.textContent = "Enviar interesse";
    }
  };

  const iniciarFechamentoAutomatico = () => {
    if (!botaoEnvio) return;

    let segundos = 5;
    botaoEnvio.disabled = true;
    botaoEnvio.textContent = `Fechando em ${segundos}s`;
    temporizadorFechamento = setInterval(() => {
      segundos -= 1;
      botaoEnvio.textContent = `Fechando em ${segundos}s`;

      if (segundos === 0) {
        clearInterval(temporizadorFechamento);
        fecharFormulario(secao, sobreposicao);
      }
    }, 1000);
  };

  configurarValidacao(formulario, iniciarFechamentoAutomatico);
  bloquearRedimensionamento(formulario);

  botaoChat.addEventListener("click", () =>
    abrirFormulario(secao, sobreposicao, restaurarFormulario),
  );
  botaoFechar.addEventListener("click", () =>
    fecharFormulario(secao, sobreposicao),
  );
  sobreposicao.addEventListener("click", () =>
    fecharFormulario(secao, sobreposicao),
  );

  botaoAjuda?.addEventListener("click", () => {
    const aberto = botaoAjuda.getAttribute("aria-expanded") === "true";
    botaoAjuda.setAttribute("aria-expanded", String(!aberto));
    if (conteudoAjuda) conteudoAjuda.hidden = aberto;
  });

  setTimeout(
    () => abrirFormulario(secao, sobreposicao, restaurarFormulario),
    TEMPO_ABERTURA,
  );
}
