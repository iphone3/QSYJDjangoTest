// 删除操作
$('#car-content > table > tbody tr > td > .del').click(function(){
	$(this).attr('check', 'false')
	price_compute($(this))
	$(this).parent().parent().remove()
})

// 加操作
$('#car-content > table > tbody > tr > td > .num-wrapper > .add').click(function(){
	var num = parseInt($(this).prev().attr('value'))
	num++
	$(this).prev().attr('value', num)
	
	var price = parseInt($(this).parent().parent().parent().find('.price').attr('price'))
	
	// 判断是否选择
	if($(this).parent().parent().parent().find('input[type=checkbox]').attr('check') == 'true'){
		setTotalPrice(price,1)
	}
	
	// 小计
	$(this).parent().parent().parent().find('.subtotal').text(num*price)
})

// 减操作
$('#car-content > table > tbody > tr > td > .num-wrapper > .sub').click(function(){
	var num = parseInt($(this).next().attr('value'))
	num--
	if(num >= 1){
		$(this).next().attr('value', num)
		
		// 判断是否选择
		if($(this).parent().parent().parent().find('input[type=checkbox]').attr('check') == 'true'){
			var price = parseInt($(this).parent().parent().parent().find('.price').attr('price'))
			setTotalPrice(price,-1)
		}
	}
})


// 设置总金额
function setTotalPrice(price, num){
	console.log(price*num)
	
	var total =  parseInt($("#buy-bar > .buy-wrapper > div.price > b").text())
	
	$("#buy-bar > .buy-wrapper > div.price > b").text(total + price*num)
}

// 金额处理
function price_compute(that){
	// 获取单价
	var price = that.parent().parent().find('.price').attr('price')
	
	// 获取数量
	var num = that.parent().parent().find('.num').attr('value')
	
	// 设置
	if(that.attr('check') == 'true'){	// 选中
		setTotalPrice(price, num)
	} else {	// 取消选中
		setTotalPrice(price, -num)
	}
}

// 商品选择
var shop_checks = $('#car-content > table > tbody > tr > td input[type=checkbox]')
shop_checks.click(function(){
	if ($(this).attr('check') == 'true'){	// 选中
		$(this).attr('check', 'false')
		// 判断是否全选
		if($('#car-content > table > tbody > tr.title > th:nth-child(1) > input').attr('isAll') == 'true'){
			$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', false).attr('isAll', 'false')
			$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', false).attr('isAll', 'false')
		}
	} else {
		$(this).attr('check', 'true')
		
		// 是否全部选中
		var isAll = true
		shop_checks.each(function(){
			if($(this).attr('check') == 'false'){
				isAll = false
			}
		})
		if(isAll){
			$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', true).attr('isAll', 'true')
			$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', true).attr('isAll', 'true')
		}
	}
	
	price_compute($(this))
})

// 全选
$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', false).click(function(){
	var isAll = $(this).attr('isAll') == 'false' ? true : false
	
	if(isAll){	// 全选
		$(this).attr('isAll', 'true')
		$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', true).attr('isAll', 'true')
		
		shop_checks.each(function(){
			if($(this).attr('check') == 'false'){
				$(this).attr('check', 'true').prop('checked', true)
				price_compute($(this))
			}
		})
		
	} else {	// 取消全选
		$(this).attr('isAll', 'false')
		$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', false).attr('isAll', 'false')
		
		shop_checks.each(function(){
			$(this).attr('check', 'false').prop('checked', false)
			price_compute($(this))
		})
	}
})

$('#buy-bar > .buy-wrapper > div.check-all.fl > input').click(function(){
	var isAll = $(this).attr('isAll') == 'false' ? true : false
	
	if(isAll){	// 全选
		$(this).attr('isAll', 'true')
		$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', true).attr('isAll', 'true')
		shop_checks.each(function(){
			if($(this).attr('check') == 'false'){
				$(this).attr('check', 'true').prop('checked', true)
				price_compute($(this))
			}
		})
		
	} else {	// 取消全选
		$(this).attr('isAll', 'false')
		$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', false).attr('isAll', 'false')
		shop_checks.each(function(){
			$(this).attr('check', 'false').prop('checked', false)
			price_compute($(this))
		})
	}
})


// 删除选中
$('#buy-bar > .buy-wrapper > .del-bt').click(function(){
	$('#car-content > table > tbody > tr > td input[type=checkbox]').each(function(){
		if($(this).attr('check') == 'true'){
			// 单个处理
			$(this).attr('check', 'false')
			price_compute($(this))
			$(this).parent().parent().remove()
			
			// 全选处理
			$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', false).attr('isAll', 'false')
			$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', false).attr('isAll', 'false')
		}
	})
})

// 清空
$('#buy-bar > .buy-wrapper > .clear-bt').click(function(){
	shop_checks.each(function(){
		// 单个处理
		$(this).attr('check', 'false')
		price_compute($(this))
		$(this).parent().parent().remove()
		
		// 全选处理
		$('#car-content > table > tbody > tr.title > th:nth-child(1) > input').prop('checked', false).attr('isAll', 'false')
		$('#buy-bar > .buy-wrapper > div.check-all.fl > input').prop('checked', false).attr('isAll', 'false')
	
		$("#buy-bar > .buy-wrapper > div.price > b").text(0)
	})
})