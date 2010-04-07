//site_media/js/navigate.js
// var current=0;

// this one will handle the navigation
// function subnav(show){
// 	$(document).ready(function(){
// 		$(".sub" + show).css({"display":"block"});
// 		$("#navigation > li").hover(
// 			function () {
// 				for(i=0;i<4;i++){
// 					if($(this).hasClass("nav" + String(i+1))){current = i+1;}
// 				}
// 				$(".subs").css({"display":"none"});
// 				c = ".sub" + String(current);
// 	        	$(c).css({"display":"block"});
// 		    }, 
// 			function () {
// 	        	// $(c).css({"display":"none"});
// 	      	}
// 	    );
// 	})
// }

// this one will hide all the extra featured ads and call the rotater
function feature(how_many){
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

