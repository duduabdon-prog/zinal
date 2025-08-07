document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("toggle-theme");
    const html = document.documentElement;

    if (localStorage.getItem("theme") === "dark") {
        html.classList.add("dark-mode");
    }

    toggleButton.addEventListener("click", () => {
        html.classList.toggle("dark-mode");
        localStorage.setItem("theme", html.classList.contains("dark-mode") ? "dark" : "light");
    });
});
