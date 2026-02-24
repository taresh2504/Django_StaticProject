var img = document.querySelector('.img1');

img.addEventListener('mouseenter', function(){
    img.src = "/static/images/img1r.jpg";
});

img.addEventListener('mouseleave', function(){
    img.src = "/static/images/img1.jpg";
});

var img2 = document.querySelector('.img2');

img2.addEventListener('mouseenter', function(){
    img2.src = "/static/images/img2r.jpg";
});

img2.addEventListener('mouseleave', function(){
    img2.src = "/static/images/img2.jpg";
});

const categoryItem = document.querySelector('.category-item');
const hoverBox = document.querySelector('.hover-box');

let timeout;

categoryItem.addEventListener('mouseenter', () => {
    clearTimeout(timeout);
    hoverBox.style.display = 'block';
});

categoryItem.addEventListener('mouseleave', () => {
    timeout = setTimeout(() => {
        hoverBox.style.display = 'none';
    }, 3000);
});

hoverBox.addEventListener('mouseenter', () => {
    clearTimeout(timeout);
});

hoverBox.addEventListener('mouseleave', () => {
    timeout = setTimeout(() => {
        hoverBox.style.display = 'none';
    }, 500);
});

