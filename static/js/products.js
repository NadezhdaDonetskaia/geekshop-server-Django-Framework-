window.onload = function() {
    $('.products_list').on('click', 'input[id="inner_basket"]', function() {
        var t_href = event.target;
        console.log(t_href.name);

        $.ajax({
            url: 'products/add/' + t_href.name + '/',
            success: function (data) {
                $('.products_list').html(data.result);
            }
        })
    });
}