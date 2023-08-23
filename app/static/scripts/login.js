function login_user() {

    let email = document.getElementById('email')
    let password = document.getElementById('password')

    const request = new XMLHttpRequest();
    request.open('POST', `/api/users/login`, true);
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send(JSON.stringify({
        'email': email.value,
        'password': password.value
    }));

    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            let response = JSON.parse(request.response);
            if (request.status === 200) {
                window.location.href = '/home'
            } else {
                alert(response.message)
                window.location.reload()
            }
        }
    }

}