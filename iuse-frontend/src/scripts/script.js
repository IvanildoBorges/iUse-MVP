// =========================================
// BUSCA
// =========================================
import inicializarFiltrosAcervo from "./components/acervo-filtros.js";
import inicializarFormularioDoacao from "./components/form-interesse.js";
import eventoBuscaItem from "./components/search.js";

const listaDebotoesDeBusca = document.getElementsByClassName("search-btn");

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", inicializarFormularioDoacao, {
    once: true,
  });
} else {
  inicializarFormularioDoacao();
}
eventoBuscaItem(listaDebotoesDeBusca);
inicializarFiltrosAcervo();
