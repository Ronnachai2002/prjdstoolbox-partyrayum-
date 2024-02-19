const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function login() {

    var username = document.getElementById('username').value;
    var pass1 = document.getElementById('pass1').value;

    var userType = checkUserType(username);

    if (userType === 'admin') {
        alert('ยินดีต้อนรับ Admin ' + username);

        window.location.href = 'admin.html';
    } else if (userType === 'user') {
        alert('ยินดีต้อนรับ ' + username);

        window.location.href = 'user.html';
    } else {
        alert('บัญชีผู้ใช้ไม่ถูกต้อง');
    }
}

function checkUserType(username) {

    if (username === 'admin') {
        return 'admin';
    } else {
        return 'user';
    }
}
$.ajax({
    type: 'POST',
    url: '/your-endpoint/',
    data: {
        username: $('#username').val(),  
        password: $('#password').val(),  
        
        csrfmiddlewaretoken: getCookie('csrftoken')  
    },
    success: function(response) {
        
        if (response.success) {
            
            window.location.href = '/home/';
        } else {
            
            console.error('Unexpected success scenario:', response);
        }
    },
    error: function(error) {
        
        console.error('Error:', error);

        
        window.location.href = '/home/';
    }
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}