//site_media/js/navigate.js
var current=0;
function subnav(show){
	$(document).ready(function(){
		$(".sub" + show).css({"display":"block"});
		$("#navigation > li").hover(
			function () {
				for(i=0;i<4;i++){
					if($(this).hasClass("nav" + String(i+1))){current = i+1;}
				}
				$(".subs").css({"display":"none"});
				c = ".sub" + String(current);
	        	$(c).css({"display":"block"});
		    }, 
			function () {
	        	// $(c).css({"display":"none"});
	      	}
	    );
	})
}



