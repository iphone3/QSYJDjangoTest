//Tab控制函数
function tabs(tabId, tabNum){
	//设置点击后的切换样式
	$(tabId + " .tab li").removeClass("curr");
	$(tabId + " .tab li").eq(tabNum).addClass("curr");
	//根据参数决定显示内容
	$(tabId + " .tabcon").hide();
	$(tabId + " .tabcon").eq(tabNum).show();
}


//鼠标经过预览图片函数
function preview(img){
	$("#preview .jqzoom img").attr("src",$(img).attr("src"));
	$("#preview .jqzoom img").attr("jqimg",$(img).attr("bimg"));
}

//图片放大镜效果
$(function(){
	$(".jqzoom").jqueryzoom({xzoom:380,yzoom:410});
});

//图片预览小图移动效果,页面加载时触发
$(function(){
	var tempLength = 0; //临时变量,当前移动的长度
	var viewNum = 5; //设置每次显示图片的个数量
	var moveNum = 2; //每次移动的数量
	var moveTime = 300; //移动速度,毫秒
	var scrollDiv = $(".spec-scroll .items ul"); //进行移动动画的容器
	var scrollItems = $(".spec-scroll .items ul li"); //移动容器里的集合
	var moveLength = scrollItems.eq(0).width() * moveNum; //计算每次移动的长度
	var countLength = (scrollItems.length - viewNum) * scrollItems.eq(0).width(); //计算总长度,总个数*单个长度
	  
	//下一张
	$(".spec-scroll .next").bind("click",function(){
		if(tempLength < countLength){
			if((countLength - tempLength) > moveLength){
				scrollDiv.animate({left:"-=" + moveLength + "px"}, moveTime);
				tempLength += moveLength;
			}else{
				scrollDiv.animate({left:"-=" + (countLength - tempLength) + "px"}, moveTime);
				tempLength += (countLength - tempLength);
			}
		}
	});
	//上一张
	$(".spec-scroll .prev").bind("click",function(){
		if(tempLength > 0){
			if(tempLength > moveLength){
				scrollDiv.animate({left: "+=" + moveLength + "px"}, moveTime);
				tempLength -= moveLength;
			}else{
				scrollDiv.animate({left: "+=" + tempLength + "px"}, moveTime);
				tempLength = 0;
			}
		}
	});
});


// 眼镜规格选择
var sz_items1 = $('.product-intro > .itemInfo-wrap > .choose-attrs > .size:first .item')
var sz_currentPage1 = $('.product-intro > .itemInfo-wrap > .choose-attrs > .size:first .item.select')
var sz_items2 = $('.product-intro > .itemInfo-wrap > .choose-attrs > .size:last .item')
var sz_currentPage2 = $('.product-intro > .itemInfo-wrap > .choose-attrs > .size:last .item.select')
sz_items1.click(function(){
	// 当前样式处理
	sz_currentPage1.removeClass('select')
	sz_currentPage1 = $(sz_items1[$(this).index()])
	sz_currentPage1.addClass('select')

	set_attr_cookies()
	window.location.href = sz_currentPage1.attr('data-href')
})
sz_items2.click(function(){
	// 当前样式处理
	sz_currentPage2.removeClass('select')
	sz_currentPage2 = $(sz_items2[$(this).index()])
	sz_currentPage2.addClass('select')

	set_attr_cookies()
	window.location.href = sz_currentPage1.attr('data-href')
})
// 设置cookie操作
function set_attr_cookies(){
	var temp = ''
	standard_id1 = sz_items1.parent().prev().attr('data-standard')
	attr_id1 = sz_currentPage1.attr('data-id')
	temp = standard_id1 + '_' + attr_id1 + '_'

	standard_id2 = sz_items2.parent().prev().attr('data-standard')
	attr_id2 = sz_currentPage2.attr('data-id')
	temp += standard_id2 + '_' + attr_id2
	// 设置cookie，传入产品选择的属性值
	$.cookie('select_attr', temp, { path: '/' });
}


// 数量选择
var sub_bt = $('.product-intro > .itemInfo-wrap > .choose-attrs > .num .sub')
var add_bt = $('.product-intro > .itemInfo-wrap > .choose-attrs > .num .add')
var num_tx = $('.product-intro > .itemInfo-wrap > .choose-attrs > .num b')
sub_bt.click(function(){
	var num = parseInt(num_tx.text())
	if(num > 0){
		num_tx.text(--num)
	}
	if(num == 0) sub_bt.addClass('disable')
})
add_bt.click(function(){
	var num = parseInt(num_tx.text())
	num_tx.text(++num)
	if(num > 0){
		sub_bt.removeClass('disable')
	}
})



// 商品简介/评价切换
var synopsis_cn = $('.product-desc > .detail > .tab-cont > .synopsis')	
var assess_cn = $('.product-desc > .detail > .tab-cont > .assess')	
var detail_tab_curr = $('.product-desc > .detail > .tab-main > .item').eq(0)
$('.product-desc > .detail > .tab-main > .item').click(function(){
	detail_tab_curr.removeClass('active')
	detail_tab_curr = $(this)
	detail_tab_curr.addClass('active')
	
	if($(this).index() == 0){
		synopsis_cn.show()
		assess_cn.hide()
	} else if($(this).index() == 1 ){
		synopsis_cn.hide()
		assess_cn.show()
	}
})

// 评价内容切换(好评、中评、差评)
var assess_items = $('.product-desc > .detail > .tab-cont > .assess > .tab-cont > div')
var assess_item_curr = assess_items.eq(0)
var assess_tabs = $('.product-desc > .detail > .tab-cont > .assess > .tab-main > .tab-item')
var assess_tab_curr = assess_tabs.eq(0)
assess_tabs.click(function(){
	assess_tab_curr.removeClass('active')
	assess_item_curr.hide()
	
	assess_tab_curr = $(this)
	assess_item_curr = assess_items.eq($(this).index())
	
	assess_tab_curr.addClass('active')
	assess_item_curr.show()
})

