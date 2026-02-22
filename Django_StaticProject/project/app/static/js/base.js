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