function limitCheckboxSelection(checkbox) {
    var checkboxes = document.getElementsByName("selected_item");
    checkboxes.forEach(function (cb) {
        if (cb !== checkbox) {
            cb.checked = false;
        }
    });

    var checkoutLink = document.getElementById("checkout-link");
    var productName = checkbox.parentNode.parentNode.cells[0].innerText.trim();

    if (checkbox.checked) {
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
    } else {
        checkoutLink.setAttribute("href", "{% url 'order' %}");
    }
} else {
    checkoutLink.setAttribute("href", "{% url 'order' %}");
}
}