$('#user-container > .side-wrapper > .side-item').click(function(){
	var index = $(this).index();
	$('#user-container > .side-wrapper > .side-item').removeClass('active')
	$(this).addClass('active')
	
	$('#user-container > .main-wrapper').hide().eq(index).show();
})