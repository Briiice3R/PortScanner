const form = document.querySelector("form");
const loader = document.querySelector(".loader");

form.addEventListener("submit", ()=>{
    loader.classList.remove("hidden");
    loader.classList.add("block");
});