
// <div class="atar_Show">
// 	<p tip="3.5"></p>
// </div>
$('.atar_Show p').each(function(index,element){
	var num = $(this).attr("tip");
	// var www = num * 2 * 12;  // 24宽度
	var www = num * 2 * 16; 
	$(this).css("width", www);
})
