// To be able to style the different labels in the form
document.addEventListener("DOMContentLoaded", () => {
  const firstLabel = document.querySelector("#services-form label");
  if (firstLabel) {
    firstLabel.classList.add("header-label");
  }
});