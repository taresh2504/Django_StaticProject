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

// search box product card

// search box product card

var productcard = document.querySelector('.product-card');
var productimg = document.querySelector('.product-img1');

productcard.addEventListener('mouseenter', function(){
    productimg.src = "/static/images/img4b.jpg";
});

productcard.addEventListener('mouseleave', function(){
    productimg.src = "/static/images/img4.jpg";
});

var productcard2 = document.querySelector('.product-card2');
var productimg2 = document.querySelector('.product-img2');

productcard2.addEventListener('mouseenter', function(){
    productimg2.src = "/static/images/img3b.jpg";
});

productcard2.addEventListener('mouseleave', function(){
    productimg2.src = "/static/images/img3.jpg";
});

var productcard3 = document.querySelector('.product-card3');
var productimg3 = document.querySelector('.product-img3');

productcard3.addEventListener('mouseenter', function(){
    productimg3.src = "/static/images/img5b.jpg";
});

productcard3.addEventListener('mouseleave', function(){
    productimg3.src = "/static/images/img5.jpg";
});

var productcard4 = document.querySelector('.product-card4');
var productimg4 = document.querySelector('.product-img4');

productcard4.addEventListener('mouseenter', function(){
    productimg4.src = "/static/images/img6b.jpg";
});

productcard4.addEventListener('mouseleave', function(){
    productimg4.src = "/static/images/img6.jpg";
});




