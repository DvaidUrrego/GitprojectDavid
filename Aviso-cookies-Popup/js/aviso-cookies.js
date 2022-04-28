const botonAceptarCookies = document.getElementById("btn-aceptar-cookies");
const avisoCookies = document.getElementById("aviso-cookies");
const fondoAvisoCookies = document.getElementById("fondo-aviso-cookies");

dataLayer = []; /*Arreglo para Tac Manager*/

/* Obtiene o accede al elemento que nos queda en el localStorage*/
if (!localStorage.getItem("cookies-aceptadas")) {
  avisoCookies.classList.add("activo"); /*Agrega la clase activo*/
  fondoAvisoCookies.classList.add("activo");
} else {
  dataLayer.push({ event: "cookies-aceptadas" });
}

botonAceptarCookies.addEventListener("click", () => {
  avisoCookies.classList.remove("activo"); /*Elimina la calse activo*/
  fondoAvisoCookies.classList.remove("activo");

  localStorage.setItem("cookies-aceptadas", true);
  dataLayer.push({
    event: "cookies-aceptadas",
  }); /*Dispara el evento de google Tac Manager*/
});
