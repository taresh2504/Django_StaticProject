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
    }, 300);
});

hoverBox.addEventListener('mouseenter', () => {
    clearTimeout(timeout);
});

hoverBox.addEventListener('mouseleave', () => {
    timeout = setTimeout(() => {
        hoverBox.style.display = 'none';
    }, 300);
});

const categoryItem2 = document.querySelector('.category-item2');
const hoverBox2 = document.querySelector('.hover-box2');

let timeout2;

categoryItem2.addEventListener('mouseenter', () => {
    clearTimeout(timeout2);
    hoverBox2.style.display = 'block';
});

categoryItem2.addEventListener('mouseleave', () => {
    timeout2 = setTimeout(() => {
        hoverBox2.style.display = 'none';
    }, 300);
});

hoverBox2.addEventListener('mouseenter', () => {
    clearTimeout(timeout2);
});

hoverBox2.addEventListener('mouseleave', () => {
    timeout2 = setTimeout(() => {
        hoverBox2.style.display = 'none';
    }, 300);
});

const categoryItem3 = document.querySelector('.category-item3');
const hoverBox3 = document.querySelector('.hover-box3');

let timeout3;

categoryItem3.addEventListener('mouseenter', () => {
    clearTimeout(timeout3);
    hoverBox3.style.display = 'block';
});

categoryItem3.addEventListener('mouseleave', () => {
    timeout3 = setTimeout(() => {
        hoverBox3.style.display = 'none';
    }, 300);
});

hoverBox3.addEventListener('mouseenter', () => {
    clearTimeout(timeout3);
});

hoverBox3.addEventListener('mouseleave', () => {
    timeout3 = setTimeout(() => {
        hoverBox3.style.display = 'none';
    }, 300);
});



