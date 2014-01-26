$(document).ready(function () {
	var ajaxData = {
	  category: 0,
	  search: "",
	  page: 1	
	}

	var url = "http://webproject.roohy.me/ajax/1/unknown/category/list" ;
	$("#test").click(function () {
	$.ajax({
		url: url,
		type: 'post',
		dataType: 'json',
		data: ajaxData,
		error: function (data, status, tmp) {
            alert('Error:' + data + 'status: ' + status + " " + tmp);
        },
		success: function(data, status, xhr){
		    if (data.result == 0){
		       alert('haji khalie');
		    }else {
				alert("salam");
		       var cat = $.parseJSON(data);
			   
		    }
		},
		// ...
	});
	});
});