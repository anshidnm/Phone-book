$(document).on("click","#add_but",function(e){
    e.preventDefault()
    var url = $(this).attr('data-url')
    var name = $('#id_name').val()
    var number = $('#id_mobile').val()

    if(!name.trim()){
        $("#name_error").text("This field is required")
        $("#name_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#name_error").attr("style","display:none;color:red;")
        },2000)
        return false
    }
    if(!number.trim()){
        $("#number_error").text("This field is required")
        $("#number_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#number_error").attr("style","display:none;color:red;")
        },2000)
        return false
    }
    if(number.length != 10){
        $("#number_error").text("Invalid Number,10 digit number required")
        $("#number_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#number_error").attr("style","display:none;color:red;")
        },2000)
        return false
    }
    
    var csrftoken =$("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        method:"POST",
        headers:{"X-CSRFToken": csrftoken},
        url:url,
        data:{
            number:number,name:name
        },
        beforeSend:function(){
            $("#add_but").html("ADDING.....")
        },
        success:function(response){
            if(response.status){
                $("#number_list").html(response.template)
                $("#id_name").val(null)
                $("#id_mobile").val(null)
                $(".message_div").text("Contact added successfully")
                $(".message_div").attr("style","display:block;background-color:green;")
                setTimeout(function(){
                    $(".message_div").attr("style","display:none;")
                },2000)
            }
        },
        complete:function(){
            $("#add_but").html("ADD NUMBER")
        }
    })
})

$(document).on("click",".delete_contact",function(){
    var url = $(this).attr("data-url")
    swal({
        icon:"warning",
        title:"Are you sure ?",
        buttons:true,
        text:"Do you want delete this contact ?",
        dangerMode:true
    }).then(function(willdelete){
        if(willdelete){
            $.ajax({
                method:"GET",
                url:url,
                success:function(response){
                    if(response.status){
                        $("#number_list").html(response.template)
                        swal("Success","Contact deleted successfully","success")
                    }
                }
            })
        }
        
    })

})

$(document).on("click",".edit_contact",function(){
    var url = $(this).attr("data-url")
    $.ajax({
        url:url,
        method:"GET",
        success:function(response){
            $("#modal").html(response.template)
        }
    })
})

$(document).on("click","#edit_but",function(){
    var id = $(this).attr("data-id")
    var url = `/edit-contact/${parseInt(id)}/`
    var name = $(".edit_name").val()
    var number = $(".edit_mobile").val()
    if(!name.trim()){
        $("#edit_error").text("Name is required")
        $("#edit_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#edit_error").attr("style","display:none;color:red;")
        },2000)
        return false
    }
    if(!number.trim()){
        $("#edit_error").text("Number is required")
        $("#edit_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#edit_error").attr("style","display:none;color:red;")
        },2000)
        return false
    }
    if(number.length != 10){
        $("#edit_error").text("Invalid Number,10 digit number required")
        $("#edit_error").attr("style","display:block;color:red;")
        setTimeout(function(){
            $("#edit_error").attr("style","display:none;color:red;")
        },1000)
        return false
    }
    var csrftoken =$("[name=csrfmiddlewaretoken]").val();
    $.ajax({
        url:url,
        method:"POST",
        headers:{"X-CSRFToken": csrftoken},
        data:{
            name:name,number:number
        },
        beforeSend:function(){
            $("#edit_but").html("Editing....")
        },
        success:function(response){
            if(response.status){
                $.fancybox.close();
                $("#number_list").html(response.template)
                swal("Success","Contact edited successfully","success")
            }
        },
        complete:function(){
            $("#edit_but").html("Edit")
        }
    })
})

$(document).on("click",".view_contact",function(){
    var url = $(this).attr("data-url")
    $.ajax({
        method:"GET",
        url:url,
        success:function(response){
            if(response.status)[
                $("#modal_view").html(response.template)
            ]
        }
    })
})