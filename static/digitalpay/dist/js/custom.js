(function () {
    'use strict'

    // for fetch products name in installment
    document.addEventListener('DOMContentLoaded', function () {
        var btns = document.querySelectorAll('#btn-product');
        btns.forEach(function (btn) {
            btn.addEventListener('click', function () {
                var installmentDiv = btn.closest('.installment');
                var installmentID = installmentDiv.getAttribute('data-installment-id');
                fetch(`/installments/api/${installmentID}/products/`).then(response => response.json()).then(data => {
                    var productList = document.querySelector('#product_list');
                    productList.innerHTML = '';
                    data.products.forEach(function (product) {
                        var li = document.createElement('li');
                        li.textContent = `${product.name}    (${product.count} عدد)`;
                        productList.appendChild(li);
                    });
                })
            })
        })
    })
})()