$(document).ready(function (){
    var csrf = $("input[name=csrfmiddlewaretoken]").val()
    var id_tugas = $('#id_tugas').val()
    // var formData = new FormData();
    

    $("a").on('click', function(e){
        e.preventDefault();
        // formData.append('id_tgs', $('#id_tugas').val())
        var $row = $(this).closest("tr");
        var $text = $row.find("#id_tugas").val();
        var $id_absensi = $row.find("#absensi_id").val();
        if ($row.find("#is_approve_id").prop('checked')){
            $is_approve=true;
        } else {
            $is_approve=false;
        };
        var $tambah_tugas = $row.find("#tambah_tugas_id").val(); 
        console.log($is_approve)
        var $this = $(this);
        // console.log($this);
        $.ajax({
            url:$this.attr('href'),
            type:'post',
            data:{
                id_tgs: $('#id_tugas').val(), //$("#id_tugas").val(),
                id_absensi: $id_absensi,
                is_approve: $is_approve,
                tambah_tugas: $tambah_tugas,
                csrfmiddlewaretoken: csrf,
            },
            success: function(){
                
                // alert("hebohhh")
            }
        });
    });

   
});