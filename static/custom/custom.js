let asliddin = document.querySelector(".main-footer").firstElementChild;

asliddin.innerHTML = "Powered by <b><span class='text-success'>CODE TECH ACADEMY</span></b>";

const status = document.querySelectorAll('.field-status');
for(let i = 0; i < status.length; i++) {
    let element = status[i];
    if (element.innerHTML == "Buyurtma berildi") {
        element.innerHTML = "<p class='btn btn-warning'><b>Buyurtma berildi</b></p>";
    } else if (element.innerHTML == "Yetkazildi") {
        element.innerHTML = "<p class='btn btn-success'><b>Yetkazildi</b></p>";
    } else if (element.innerHTML == "Bekor qilindi") {
        element.innerHTML = "<p class='btn btn-danger'><b>Bekor qilindi</b></p>";
    }
}

const passwordInput1 = document.querySelector('#id_password1');
const passwordInput2 = document.querySelector('#id_password2');

passwordInput1.classList.add('form-control');
passwordInput2.classList.add('form-control');