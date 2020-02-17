// 选项卡
$('#order-container > .nav-bar > .nav-item').click(function(){
	$('#order-container > .nav-bar > .nav-item').removeClass('active')
	$(this).addClass('active')
	
	// console.log($(this).index())
	
	$('#order-container > .order-main > .order-wrapper').addClass('hide').eq($(this).index()).removeClass('hide')
	
	
	// 高度设置
	setReferenceLine()
})

// 高度设置
function setReferenceLine(){
	$('#order-container > .order-main > .order-wrapper > .order-item').each(function(){
		var height = $(this).find('.goods-wrapper').height()
		$(this).find('.line').css('height', height)
		
		// $(this).find('.time').css('top', (height-90)/2)
	})
}
setReferenceLine()