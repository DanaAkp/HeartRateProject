get_heart_rate()
function add_heart_rate() {
    let heart_rate = document.getElementById('heart_rate')
    if (heart_rate.value === '') {
        console.log(heart_rate.value)
        alert('Please input heart rate.')
    }
    const request = new XMLHttpRequest();
    request.open('POST', `/api/heart_rates/heart_rates`, true);
    request.setRequestHeader('Content-type',
        'application/json; charset=utf-8');
    request.send(JSON.stringify({
        'current_heart_rate': Number(heart_rate.value),
    }));

    request.onreadystatechange = function () {
        if (request.readyState === 4) {
            let response = JSON.parse(request.response);
            if (request.status === 200) {

                let curr_hr = document.getElementById('result')
                curr_hr.value = ''
                if (response.current_heart_rate > response.average_heart_rate) {
                    curr_hr.innerHTML = `Your heart rate increase`
                } else if (response.current_heart_rate < response.average_heart_rate) {
                    curr_hr.innerHTML = `Your heart rate decrease`
                } else {
                    curr_hr.innerHTML = `Your heart rate not changed`
                }
                get_heart_rate()
            } else alert(response.message);
        }
    }
}

function get_heart_rate() {
    const request = new XMLHttpRequest();

    request.open('GET', `/api/heart_rates/heart_rates`, false);
    request.send();
    let response = JSON.parse(request.response)
    let heart_rate = response.heart_rate;
    let create_time = response.create_time;
    let last_hr = document.getElementById('last-hr')
    last_hr.innerHTML = `Last heart rate: ${heart_rate} on ${create_time}`
}


function logout_user() {
    const request = new XMLHttpRequest();
    request.open('POST', `/api/users/logout`, false);
    request.send();
    if (request.status === 200)
        window.location.href = 'home'

}