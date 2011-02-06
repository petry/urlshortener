		
$(document).ready(function() { 
    $('#short_form').ajaxForm({ 
        dataType:  'json', 
        success:   processJson 
    }); 
});
function processJson(data) { 
    $('form#short_form>.errorlist').remove();
	
	if(data.status == 'success'){
		$('#short-url').html(data.short_url);
		$('form#short_form>#id_long_url').val(data.long_url);
	}
	if(data.status == 'error'){
		$('#short-url').html('');
		$('form#short_form>#id_long_url').before('<ul class="errorlist"><li>'+data.error.long_url+'</li></ul>');
		//$('form#short_form>#id_long_url').val(data.long_url);
	}
}