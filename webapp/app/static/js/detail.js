let currentImage = 0;

function redirectToLogin() {
  alert('กรุณาเข้าสู่ระบบเพื่อทำการสั่งซื้อ');
  window.location.href = '/login';
}

function orderButtonClicked() {
  alert('กรุณาเข้าสู่ระบบเพื่อทำการสั่งซื้อ');
  window.location.href = '/login';
}

function showImage(n) {
  const images = document.querySelectorAll('.product-image');
  currentImage += n;

  if (currentImage >= images.length) {
    currentImage = 0;
  } else if (currentImage < 0) {
    currentImage = images.length - 1;
  }

  for (let i = 0; i < images.length; i++) {
    images[i].classList.remove('active');
  }

  images[currentImage].classList.add('active');
}

function changeImage(n) {
  showImage(n);
}

document.addEventListener('DOMContentLoaded', function () {
  const prevButton = document.querySelector('.prev');
  const nextButton = document.querySelector('.next');

  prevButton.addEventListener('click', function () {
    changeImage(-1);
  });

  nextButton.addEventListener('click', function () {
    changeImage(1);
  });
});

function orderProduct(productName) {
  var checkoutLink = document.getElementById("checkout-link");
  if (productName === "ป้ายกล่องไฟ") {
      checkoutLink.setAttribute("href", "{% url 'order2' %}"); 
  } else if (productName === "ป้ายสติ๊กเกอร์") {
      checkoutLink.setAttribute("href", "{% url 'order3' %}");
  } else if (productName === "ป้ายรีดฟิวเจอร์บอร์ด") {
      checkoutLink.setAttribute("href", "{% url 'order4' %}");
  } else if (productName === "ป้ายอักษรพลาสวูด") {
      checkoutLink.setAttribute("href", "{% url 'order5' %}");
  } else if (productName === "ป้ายรีดโฟมบอร์ด") {
      checkoutLink.setAttribute("href", "{% url 'order6' %}");
  } else if (productName === "ป้ายไวนิล") {
      checkoutLink.setAttribute("href", "{% url 'order' %}");
  }
}