// 轮播图 swiper
var fs_swiper = new Swiper('#qs-container > .fs > .banner-col > .fs-swiper', {
	centeredSlides: true,
	autoplay: {
		delay: 2500,
		disableOnInteraction: false,
	},
	loop: true
});


// 倒计时
$(document).ready(function() {
	var oDate = new Date();
	var nowTime = oDate.getTime(); // 现在的毫秒数
	oDate.setDate(oDate.getDate() + 1); // 设定截止时间为第二天
	var targetDate = new Date(oDate.toLocaleDateString());
	run(targetDate);
});
function run(enddate) {
	getDate(enddate);
	setInterval("getDate('" + enddate + "')", 1000);
}
function getDate(enddate) {
	var oDate = new Date(); // 获取日期对象
	var nowTime = oDate.getTime(); // 现在的毫秒数
	var enddate = new Date(enddate);
	var targetTime = enddate.getTime(); // 截止时间的毫秒数
	var second = Math.floor((targetTime - nowTime) / 1000); //截止时间距离现在的秒数
	var day = Math.floor(second / 24 * 60 * 60); //整数部分代表的是天；一天有24*60*60=86400秒 ；
	second = second % 86400; //余数代表剩下的秒数；
	var hour = Math.floor(second / 3600); //整数部分代表小时；
	second %= 3600; //余数代表 剩下的秒数；
	var minute = Math.floor(second / 60);
	second %= 60;
	var spanH = $('#qs-container .hour')[0];
	var spanM = $('#qs-container .minute')[0];
	var spanS = $('#qs-container .second')[0];
	spanH.innerHTML = tow(hour);
	spanM.innerHTML = tow(minute);
	spanS.innerHTML = tow(second);
}
function tow(n) {
	return n >= 0 && n < 10 ? '0' + n : '' + n;
}


// 秒杀专区-swiper
var spike_swiper = new Swiper('#qs-container > .spike-zone > .spike-swiper > .swiper-container', {
	centeredSlides: true,
	autoplay: {
		delay: 2000,
		disableOnInteraction: false,
	},
	loop: true,
	pagination: {
        el: '.swiper-pagination',
      },
});


// 特色专区-新闻切换
var currentPage = $('#qs-container > div.feature-zone.clearfix > div.feature-c1.feature-item > div.box-page > b').eq(0)
var aBoxContent = $('#qs-container > div.feature-zone.clearfix > div.feature-c1.feature-item > div.box-content > .page-ct')
$('#qs-container > div.feature-zone.clearfix > div.feature-c1.feature-item > div.box-page').click(function(e){
	// 当前样式处理
	currentPage.removeClass('active')
	var index = currentPage.attr('data-i')
	aBoxContent.eq(index).hide()
	
	// 当前的更换
	currentPage = $(e.target)
	
	// 当前样式
	currentPage.addClass('active')
	index = currentPage.attr('data-i')
	aBoxContent.eq(index).show()
})

// 特色专区-轮播图
$(function(){
	var page_swiper1 = new Swiper('#qs-container > .feature-zone > .feature-c1 > .box-content > .page-ct1 > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	var page_swiper2 = new Swiper('#qs-container > .feature-zone > .feature-c1 > .box-content > .page-ct2 > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	var page_swiper3 = new Swiper('#qs-container > .feature-zone > .feature-c1 > .box-content > .page-ct3 > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	var page_swiper4 = new Swiper('#qs-container > .feature-zone > .feature-c1 > .box-content > .page-ct4 > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	var page_swiper5 = new Swiper('#qs-container > .feature-zone > .feature-c1 > .box-content > .page-ct5 > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	
	var page_swiper6 = new Swiper('#qs-container > .feature-zone > .feature-c2 > .box-content > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
	
	var page_swiper7 = new Swiper('#qs-container > .feature-zone > .feature-c3 > .box-content > .swiper-container', {
		centeredSlides: true,
		// autoplay: {
		// 	delay: 2000,
		// 	disableOnInteraction: false,
		// },
		loop: true,
		pagination: {
	        el: '.swiper-pagination',
	      },
	});
})
