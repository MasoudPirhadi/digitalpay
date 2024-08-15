function registerErrors(errors) {
    var FIELD_LABELS = {
        'username': 'نام کاربری',
        'mobile': 'موبایل',
        'password': 'رمز عبور',
        'password2': 'رمز عبور',
    }
    var errorMessage = '';
    for (var field in errors) {
        var label = FIELD_LABELS[field];
        errorMessage += '<i class="fa fa-info-circle"></i> &nbsp;&nbsp;' + label + ': ' + errors[field] + '<br>';
    }
    document.getElementById('errors').innerHTML = errorMessage;
}

$(document).on('submit', '.register_form', function (e) {
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function (res) {
            if (res.status === 'input_code') {
                $('.card-body').html(res.body);
            } else if (res.status === 'errors') {
                registerErrors(res.errors)
            }
        },
        error: function () {
            console.log('error')
        }
    })
    e.preventDefault();
})

function verifyErrors(errors) {
    var errorMessage = '';
    for (var field in errors) {
        errorMessage += '<i class="fa fa-info-circle"></i> &nbsp;&nbsp;' + errors[field] + '<br>';
    }
    document.getElementById('errors').innerHTML = errorMessage;
}

$(document).on('submit', '#verify_form', function (e) {
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function (res) {
            if (res.status === 'success') {
                window.location.href = '/installments/'
            } else if (res.status === 'invalid') {
                document.getElementById('errors').innerHTML = '<i class="fa fa-info-circle"></i> &nbsp;&nbsp;' + (res.msg)
            } else if (res.status === 'errors') {
                verifyErrors(res.errors)
            }
        },
        error: function () {
            console.log('error')
        }
    })
    e.preventDefault();
})

$(document).on('submit', '#forgot_form', function (e) {
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function (res) {
            if (res.status === 'receive_code') {
                $('.card-body').html(res.body);
            } else if (res.status === 'not_found') {
                $('#errors').html('<i class="fa fa-info-circle"></i> &nbsp;&nbsp;' + res.msg + '<br>')
            }
        },
        error: function () {
            console.log('error')
        }
    })
    e.preventDefault();
})


$(document).on('submit', '#verify_forgot_form', function (e) {
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function (res) {
            if (res.status === 'success') {
                $('.card-body').html(res.body);
            } else if (res.status === 'invalid') {
                document.getElementById('errors').innerHTML = '<i class="fa fa-info-circle"></i> &nbsp;&nbsp;' + (res.msg)
            } else if (res.status === 'errors') {
                verifyErrors(res.errors)
            }
        },
        error: function () {
            console.log('error')
        }
    })
    e.preventDefault();
})


$(document).on('submit', '#change_pass_form', function (e) {
    $.ajax({
        url: $(this).attr('action'),
        method: $(this).attr('method'),
        data: $(this).serialize(),
        success: function (res) {
            if (res.status === 'changed') {
                $('.card-body').html(res.body);
            } else if (res.status === 'errors') {
                verifyErrors(res.errors)
            }
        },
        error: function () {
            console.log('error')
        }
    })
    e.preventDefault();
})

// for disable btn after empty form
document.addEventListener('DOMContentLoaded', function () {
    var form = document.querySelectorAll('input');
    var btn = document.querySelector('button');
    for (var i = 0; i < form.length; i++) {
        var inputs = form[i]
    }
    inputs.addEventListener('input', function () {
        btn.disabled = inputs.value === '';
    })
})
