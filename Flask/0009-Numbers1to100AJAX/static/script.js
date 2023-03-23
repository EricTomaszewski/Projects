var currentImage = 0;
var imageCount = document.getElementsByTagName('img').length;

function scrollImages() {
    var imageContainer = document.getElementById('image-container');
    var nextImage = (currentImage + 1) % imageCount;
    var currentImg = document.getElementsByTagName('img')[currentImage];
    var nextImg = document.getElementsByTagName('img')[nextImage];
    currentImg.style.zIndex = 0;
    nextImg.style.zIndex = 1;
    imageContainer.style.height = nextImg.height + 'px';
    currentImage = nextImage;
}

setInterval(scrollImages, 1000);
