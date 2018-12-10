$(document).ready(function () {
    $('.carousel').carousel({
        interval: false
    });
});

function reveal_review_space() {
    let review = document.getElementById('review-space');
    review.classList.remove('hidden');
}