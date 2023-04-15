function handleEnterKey(event) {
    if (event.keyCode === 13) {
      // Enter key was pressed
      console.log("Enter key pressed in textarea");
      // Add your code here to handle the Enter key press
    }
  }
  
var textarea = document.getElementById("my-textarea");
textarea.addEventListener("keydown", handleEnterKey);

document.addEventListener("DOMContentLoaded", function() {
  const element = document.querySelector('#chat');
  element.scrollTop = element.scrollHeight;
});


const body = document.querySelector('body');
const modal = document.querySelector('.modal');
const btnOpenPopup = document.querySelector('.btn-open-popup');


btnOpenPopup.addEventListener('click', () => {
  modal.classList.toggle('show');

  if (modal.classList.contains('show')) {
    body.style.overflow = 'hidden';
  }
});

modal.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.classList.toggle('show');

    if (!modal.classList.contains('show')) {
      body.style.overflow = 'auto';
    }
  }
});


const modal1 = document.querySelector('.modal1');
const btn1OpenPopup = document.querySelector('.btn1-open-popup');
btn1OpenPopup.addEventListener('click', () => {
  modal1.classList.toggle('show');

  if (modal1.classList.contains('show')) {
    body.style.overflow = 'hidden';
  }
});

modal1.addEventListener('click', (event) => {
  if (event.target === modal1) {
    modal1.classList.toggle('show');

    if (!modal1.classList.contains('show')) {
      body.style.overflow = 'auto';
    }
  }
});

const modal2 = document.querySelector('.modal2');
const btn2OpenPopup = document.querySelector('.btn2-open-popup');
btn2OpenPopup.addEventListener('click', () => {
  modal2.classList.toggle('show');

  if (modal2.classList.contains('show')) {
    body.style.overflow = 'hidden';
  }
});

modal2.addEventListener('click', (event) => {
  if (event.target === modal2) {
    modal2.classList.toggle('show');

    if (!modal2.classList.contains('show')) {
      body.style.overflow = 'auto';
    }
  }
});