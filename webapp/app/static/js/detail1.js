let currentImage = 0;


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

function orderProduct(productTitle) {
  // ตรวจสอบว่าชื่อสินค้าเป็นอะไรและส่งไปยัง URL ที่ถูกต้อง
  var orderUrl;
  switch(productTitle) {
      case "ป้ายกล่องไฟ":
          orderUrl = "{% url 'order2' %}";
          break;
      case "ป้ายสติ๊กเกอร์":
          orderUrl = "{% url 'order3' %}";
          break;
      case "ป้ายรีดฟิวเจอร์บอร์ด":
          orderUrl = "{% url 'order4' %}";
          break;
      case "ป้ายอักษรพลาสวูด":
          orderUrl = "{% url 'order5' %}";
          break;
      case "ป้ายรีดโฟมบอร์ด":
          orderUrl = "{% url 'order6' %}";
          break;
      case "ป้ายไวนิล":
      default:
          orderUrl = "{% url 'order' %}";
  }
  window.location.href = orderUrl;
}
