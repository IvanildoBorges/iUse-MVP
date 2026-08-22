const categorias = [
  "caderno",
  "calculadora",
  "mochila",
  "caneta",
  "estojo",
  "livro",
  "caneta",
  "mochila",
  "calculadora",
  "caderno",
  "livro",
];

function mostrarItens(cards, categoria) {
  cards.forEach((card, index) => {
    card.style.display = categorias[index] === categoria ? "flex" : "none";
  });
}

function mostrarTodosOsItens(cards) {
  cards.forEach((card) => {
    card.style.display = "flex";
  });
}

function inicializarFiltrosPorCategoria(cards) {
  const filtros = document.querySelectorAll(".filtro");

  filtros.forEach((filtro) => {
    filtro.addEventListener("click", (event) => {
      if (event.target.tagName === "SPAN") {
        return;
      }

      const categoria = filtro.textContent
        .replace("×", "")
        .trim()
        .toLowerCase();

      mostrarItens(cards, categoria);
    });

    const fechar = filtro.querySelector("span");
    fechar.addEventListener("click", (event) => {
      event.stopPropagation();
      mostrarTodosOsItens(cards);
    });
  });
}

function inicializarMenuDeFiltros(cards) {
  const btnFiltro = document.querySelector(".btn-filtro");
  const menuFiltros = document.querySelector(".menu-filtros");

  if (!btnFiltro || !menuFiltros) {
    return;
  }

  btnFiltro.addEventListener("click", () => {
    menuFiltros.classList.toggle("ativo");
  });

  const opcoesFiltro = menuFiltros.querySelectorAll("button");
  opcoesFiltro.forEach((opcao) => {
    opcao.addEventListener("click", () => {
      mostrarItens(cards, opcao.dataset.categoria);
      menuFiltros.classList.remove("ativo");
    });
  });
}

export default function inicializarFiltrosAcervo() {
  const cards = document.querySelectorAll(".card-acervo");

  if (cards.length === 0) {
    return;
  }

  inicializarFiltrosPorCategoria(cards);
  inicializarMenuDeFiltros(cards);
}
