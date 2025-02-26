// Change text for labels in Signup form
document.addEventListener("DOMContentLoaded", () => {
  let emailLabelTwo = document.querySelector("label[for='id_email2']");
  let passwordLabelTwo = document.querySelector("label[for='id_password2']");

  if (emailLabelTwo) {
    emailLabelTwo.innerText = "Email again:";
  }

  if (passwordLabelTwo) {
    passwordLabelTwo.innerText = "Password again:";
  }
})
