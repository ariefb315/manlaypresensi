$(function (){

    $(".js-create-hukuman").click(function(){
        $.ajax({
            url: '/hukuman/buat/',
            type: 'get',
            dataType: 'json',
            beforeSend: function(){
                $("#modal-hukuman").modal("show");
            },
            success: function(data){
                $("#modal-hukuman .modal-content").html(data.html_form);
            }
        });
    });

    $("#modal-hukuman").on("submit", ".js-buat-hukuman-form", function(){
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data){
                if (data.form_is_valid){
                    $("#hukuman-table tbody").html(data.html_daftar_hukuman);
                    $("#modal-hukuman").modal("hide");
                }
                else {
                    $("#modal-hukuman .modal-content").html(data.html_form);
                }
            }
        });
        return false;
    });
});