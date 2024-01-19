// Get elements from dom
const success = document.querySelector(".success-container");
const successClose = document.querySelector(".success__close");
const responsiveNavbar = document.querySelector(".responsive-navbar");
const responsiveBar = document.querySelector(".responsive-bar");
const responsiveBarOpen = document.querySelector(".responsive-bar-open");
const responsiveBarExit = document.querySelector(".responsive-bar-close");

// Contact form

if (successClose) {
  successClose.addEventListener("click", () => {
    success.classList.add("hidden");
  });
}

// Responsive navbar
if (responsiveBarOpen) {
  responsiveBarOpen.addEventListener("click", () => {
    responsiveBarOpen.classList.add("hidden");
    responsiveBarExit.classList.remove("hidden");
    responsiveNavbar.classList.remove("hidden");
  });
}

if (responsiveBarExit) {
  responsiveBarExit.addEventListener("click", () => {
    responsiveBarOpen.classList.remove("hidden");
    responsiveBarExit.classList.add("hidden");
    responsiveNavbar.classList.add("hidden");
  });
}
