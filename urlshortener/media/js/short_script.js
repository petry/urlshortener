		
$(document).ready(function() { 
    $('#short_form').ajaxForm({ 
        dataType:  'json', 
        success:   processJson 
    }); 
});
function processJson(data) { 
    $('form#short_form>p>.errorlist').remove();
	
	if(data.status == 'success'){
		$('#short-url').html(data.short_url);
		$('form#short_form>p>#id_long_url').val(data.long_url);
		
        $.get("/api/data/", function(html) { 
            $("table tbody").html(html); 
            $("#url_table").trigger("update");         
        }); 		
	}
	if(data.status == 'error'){
		$('form#short_form>p>#id_long_url').before('<ul class="errorlist"><li>'+data.error.long_url+'</li></ul>');
		
	}
}