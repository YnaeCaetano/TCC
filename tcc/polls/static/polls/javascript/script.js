/* Função para abrir o menu lateral */
const sidebar = document.getElementById("mySidebar");
const main = document.getElementById("main");

sidebar.addEventListener("mouseover", function() {
  sidebar.classList.add("sidebar-open");
  main.classList.add("sidebar-open");
});

sidebar.addEventListener("mouseout", function() {
  sidebar.classList.remove("sidebar-open");
  main.classList.remove("sidebar-open");
});