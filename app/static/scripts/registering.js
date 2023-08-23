function registering() {

    let email = document.getElementById('email')
    let name = document.getElementById('name')
    let surname = document.getElementById('surname')
    let password = document.getElementById('password')
    let rep_password = document.getElementById('repeat-password')
    if (email.value === '' || name.value === '' || surname.value === '' || password.value === '') {
        alert('Please enter all fields.')
        window.location.reload()
    }
    if (password.value !== rep_password.value) {
        alert('Passwords mismatch.')
        window.location.reload()
    }

    const request = new XMLHttpRequest();
    request.open('POST', `/api/users`, true);
    request.setRequestHeader('Content-type', 'application/json; charset=utf-8');
    request.send(JSON.stringify({
        'email': email.value,
        'name': name.value,
        'surname': surname.value,
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