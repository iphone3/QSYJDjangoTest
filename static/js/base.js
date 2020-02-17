// 搜索框处理
$('#search').focus(function() { // 获取焦点
	$("#header > div > div.nav-t > div.search > div.s-input.fl > ul").show()
}).blur(function() { // 失去焦点
	$("#header > div > div.nav-t > div.search > div.s-input.fl > ul").hide()
})

$("#header > div > div.nav-t > div.search > div.s-input.fl > ul>li").mouseover(function() { // 鼠标移入
	$(this).css("background-color", "#ffdfc6").find('b').css('color', '#5d8ebf')
}).mouseout(function() { // 鼠标移出
	$(this).css("background-color", "white").find('b').css('color', '#bbbbbb')
})

$("#header > div > div.nav-t > div.search > div.s-input.fl > ul>li:last").unbind('mouseover'); // 最后一个元素取消操作

$("#header > div > div.nav-t > div.search > div.s-input.fl > ul > li > b").click(function() { // 删除按钮
	console.log(1)
	$(this).parent().remove()
})

// 购物车
$('#header > .content > .nav-t > .car').mouseover(function() { // 显示
	$(this).find('.car-list').show()
}).mouseout(function() { // 隐藏
	$(this).find('.car-list').hide()
})
$('#header > .content > .nav-t > .car .del').click(function() { // 删除操作
	$(this).parent().parent().remove()
})