document.getElementsId('update_header').onclick = function () {
    const item = document.querySelector('header');
    item.textContent = 'New header!!!';
};