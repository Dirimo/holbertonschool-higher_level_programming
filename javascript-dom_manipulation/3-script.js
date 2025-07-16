document.getElementById('toggle_header').onclick = function () {
    const item = document.querySelector('header');
if(item.classList === 'red') {
    item.classList.remove('red');
    item.classList.add('green');
 } else {
    item.classList.remove('green');
    item.classList.add('red');
 }
};
