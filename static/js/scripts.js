function loadContent(url) {
    console.log('Loading content from:', url);
    $.get(url, function(data) {
        console.log('Received data:', data);
        $('#main-content').html(data);
    });
}

$(document).on('click', '#dashboard-link', function() {
    loadContent('http://127.0.0.1:8000/dashboard/');
});
$(document).on('click', '#realtors-link', function() {
    loadContent('http://127.0.0.1:8000/realtor-list/');
});
$(document).on('click', '#buyers-link', function() {
    loadContent('http://127.0.0.1:8000/buyer-list/');
});
$(document).on('click', '#sellers-link', function() {
    loadContent('http://127.0.0.1:8000/seller-list/');
});
$(document).on('click', '#rent-link', function() {
    loadContent('http://127.0.0.1:8000/rent-list/');
});
$(document).on('click', '#blogs-link', function() {
    loadContent('http://127.0.0.1:8000/blogs-list/');
});