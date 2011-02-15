//site_media/js/navigate.js

$(document).ready(function() {
	$('.searchchoice').click(function(){
		// alert('clicked');
		$('.searchchoice').removeClass('searchchoiceactive');
		$(this).addClass('searchchoiceactive');
	})
	$('#searcher').val('Find a timeshare to rent').css({'color':'#8f8'});
	$('#searcher').focus(function(){
		if($(this).val() == 'Find a timeshare to rent'){
			$(this).val('').css({'color':''});
		}
	})
});

function feature(how_many){		// this one will hide all the extra featured ads and call the rotater
	$(document).ready(function(){
		$(".featured_ts").css({"display":"none"});
		$("#fts1").css({"display":"block"});
		rotate_featured_ads(how_many);
	})
}

// this one will rotate the ads
var current = 1;
function rotate_featured_ads(how_many){
	$(document).everyTime(5000, function() {
		if(current == how_many){
			$(".featured_ts").css({"display":"none"});
			current = 1;
			$("#fts" + current).css({"display":"block"});
		}
		else{
			$(".featured_ts").css({"display":"none"});
			current = current + 1;
			$("#fts" + current).css({"display":"block"});
		}
	})
}

