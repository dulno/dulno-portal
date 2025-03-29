window.addEventListener('DOMContentLoaded', function () {
  if (Cookie.find("dulno-theme") == null) {
    Cookie.create("dulno-theme", "light", 60 * 60 * 24 * 365);
  }
  let theme = document.body.hasAttribute("notheme") ? "light" : Cookie.find("dulno-theme");
  let logoSource;
  if (theme === "dark") {
    document.body.classList.add("dark");
    document.body.classList.remove("light");
    document.body.setAttribute("data-bs-theme", "dark");
    logoSource = "logo-light.webp";
  } else {
    document.body.classList.remove("dark");
    document.body.classList.add("light");
    document.body.setAttribute("data-bs-theme", "light");
    logoSource = "logo-dark.webp";
  }
  let logoElements = document.getElementsByClassName("dulno-logo");
  for (let i = 0; i < logoElements.length; i++) {
    logoElements[i].src = "/static/img/" + logoSource;
  }
});