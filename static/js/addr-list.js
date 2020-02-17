// 默认地址设置
$('#addr-container > .addr-wrapper > .addr-item > .content > .default').click(function(){
	$('#addr-container > .addr-wrapper > .addr-item > .title > b').hide()
	
	$(this).parent().prev().find('b').show()
	$('#addr-container > .addr-wrapper > .addr-item > .content > .default').show()
	$(this).hide()
})

// 删除按钮
$('#addr-container > .addr-wrapper > .addr-item > .title > strong').click(function(){
	that = $(this)
	alert('是否删除', function(){
		that.parent().parent().remove()
	})
})

// 新增地址
$('#addr-container > .addr-wrapper > .addr-bar > .add-bt').click(function(){
	var window_h  = $(window).height();
	var window_w  = $(window).width();
	var iframe_w = $('#add-cover > .cover-ct').width()
	var iframe_h = $('#add-cover > .cover-ct').height()
	
	// 蒙层点击
	$('#add-cover').show().height(window_w).width(window_w).click(function(event){
		$(this).hide()
	})
	
	// 阻止事件冒泡
	$('#add-cover > .cover-ct').click(function(){
		return false
	})
	
	// 关闭
	$('#add-cover > .cover-ct > .title > b').click(function(){
		$('#add-cover').hide()
	})
	
	// 居中设置
	$('#add-cover > .cover-ct').offset({
		left:((window_w-iframe_w)/2),
		top:((window_h-iframe_h)/2),
	})
	
})

// 保存
// $('#add-cover > .cover-ct > .detail > .save-bt').click(function(){
// 	$('#add-cover').hide()
// })