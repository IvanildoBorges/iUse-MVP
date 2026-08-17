// =========================================
// BUSCA
// =========================================

import eventoBuscaItem from "./components/search.js";

// Variáveis globais
const listaDebotoesDeBusca = document.getElementsByClassName("search-btn");

// Eventos
eventoBuscaItem(listaDebotoesDeBusca);


// =========================================
// ACERVO - FILTROS
// =========================================

// Todos os cards do acervo
const cards = document.querySelectorAll(".card-acervo");

// Botões de filtro
const filtros = document.querySelectorAll(".filtro");


// =========================================
// CATEGORIA DE CADA ITEM
// =========================================

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
    "livro"
];


// =========================================
// MOSTRAR OS ITENS
// =========================================

function mostrarItens(categoria) {

    cards.forEach((card, index) => {

        if (categorias[index] === categoria) {
            card.style.display = "flex";
        } else {
            card.style.display = "none";
        }

    });

}


// =========================================
// CLIQUE NOS FILTROS
// =========================================

filtros.forEach((filtro) => {

    filtro.addEventListener("click", (event) => {

        // Se clicar no "×", não executa o filtro
        if (event.target.tagName === "SPAN") {
            return;
        }

        const categoria = filtro.textContent
            .replace("×", "")
            .trim()
            .toLowerCase();

        mostrarItens(categoria);

    });

});


// =========================================
// CLIQUE NO "X" DOS FILTROS
// =========================================

filtros.forEach((filtro) => {

    const fechar = filtro.querySelector("span");

    fechar.addEventListener("click", (event) => {

        event.stopPropagation();

        // Mostra novamente todos os cards
        cards.forEach((card) => {
            card.style.display = "flex";
        });

    });

});


// =========================================
// MENU DE FILTROS
// =========================================

const btnFiltro = document.querySelector(".btn-filtro");
const menuFiltros = document.querySelector(".menu-filtros");


// Verifica se o menu existe na página
if (btnFiltro && menuFiltros) {

    // Abre e fecha o menu
    btnFiltro.addEventListener("click", () => {
        menuFiltros.classList.toggle("ativo");
    });


    // Seleciona uma categoria pelo menu
    const opcoesFiltro = document.querySelectorAll(".menu-filtros button");

    opcoesFiltro.forEach((opcao) => {

        opcao.addEventListener("click", () => {

            const categoria = opcao.dataset.categoria;

            mostrarItens(categoria);

            // Fecha o menu depois de selecionar
            menuFiltros.classList.remove("ativo");

        });

    });

}