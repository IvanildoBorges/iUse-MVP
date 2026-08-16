export default function eventoBuscaItem(botaoDeBusca) {
  if (botaoDeBusca.length > 0) {
    const header = document.querySelector("header");
    const botaoVoltar = document.querySelector(".back-btn");
    const tituloPagina = document.querySelector(".user-name");
    const tituloAnterior = tituloPagina.textContent;

    for (let i = 0; i < botaoDeBusca.length; i++) {
      botaoDeBusca[i].addEventListener("click", () => {
        ativaModalBusca();
      });
    }

    botaoVoltar.addEventListener("click", () => {
      ativaModalBusca();
    });

    function ativaModalBusca() {
      const modalExistente = document.getElementById("meu-modal-busca");

      // Se o modal já existe, remove
      if (modalExistente) {
        modalExistente.remove();

        const estiloExistente = document.getElementById(
          "estilo-ocultar-busca"
        );

        if (estiloExistente) {
          estiloExistente.remove();
        }

        header.classList.remove("search-container");
        tituloPagina.textContent = tituloAnterior;

        return;
      }

      // Se não existe, cria
      header.classList.add("search-container");
      tituloPagina.textContent = "Busca";

      const containerBusca = document.createElement("section");
      containerBusca.id = "meu-modal-busca";
      containerBusca.innerHTML = campoListagemDeBusca();

      insereNoBody(containerBusca);
    }

    function campoListagemDeBusca() {
      return `
        <div class="campo-busca">
          <input type="text" placeholder="Buscar itens">

          <button class="filter-btn">
            <img src="./src/assets/filter.png" alt="Filtros">
          </button>
        </div>

        <div class="filtros-selecionados">
          <span class="tag-filter">
            Caderno <span>✕</span>
          </span>

          <span class="tag-filter">
            Novo <span>✕</span>
          </span>

          <span class="tag-filter">
            Bom <span>✕</span>
          </span>
        </div>

        <div class="lista-resultados" id="listaItens">
          <h2>
            Resultados para "Caderno"
            <span>- 5 resultados</span>
          </h2>
        </div>
      `;
    }

    function insereNoBody(containerBusca) {
      const estiloOcultarExistente = document.getElementById(
        "estilo-ocultar-busca"
      );

      // Evita criar o style várias vezes
      if (!estiloOcultarExistente) {
        const estiloOcultar = document.createElement("style");

        estiloOcultar.id = "estilo-ocultar-busca";

        estiloOcultar.textContent = `
          #meu-modal-busca ~ * {
            display: none !important;
          }
        `;

        document.head.appendChild(estiloOcultar);
      }

      // Insere o modal logo depois do header
      header.insertAdjacentElement("afterend", containerBusca);

      const cadernos = [
        { nome: "Caderno Preto - Bom" },
        { nome: "Caderno Preto - Novo" },
        { nome: "Caderno Amarelo - Regular" },
        { nome: "Caderno Rosa - Bom" },
        { nome: "Caderno Verde - Novo" },
      ];

      const listaContainer = document.getElementById("listaItens");

      cadernos.forEach((item) => {
        const card = document.createElement("div");
        card.classList.add("card-item");

        const img = document.createElement("img");
        img.setAttribute("alt", "Imagem do item");

        const infoDiv = document.createElement("div");
        infoDiv.classList.add("info-item");

        const titulo = document.createElement("p");
        titulo.textContent = item.nome;

        const botao = document.createElement("button");
        botao.textContent = "Reservar item";

        infoDiv.appendChild(titulo);
        infoDiv.appendChild(botao);

        card.appendChild(img);
        card.appendChild(infoDiv);

        listaContainer.appendChild(card);
      });
    }
  }
}