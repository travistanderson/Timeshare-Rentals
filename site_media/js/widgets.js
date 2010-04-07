// /site_media/js/widgets.js


function dateranger(){
	// $('#id_start_room').css({'display':'none'});
	// $('#id_end_room').css({'display':'none'});
	var monthlist = ["January","Febuary","March","April","May","June","July","August","September","October","November","December",]
	var showday = new Date();		// this is a date object the represents today's date
	var firstday = new Date();		// this will be used inside the firstofmonth() function
	var viewyear = [0,0,0];			// this is an array that knows which years the user is looking at
	var viewmonth = [0,1,2];		// this is an array that knows which months the user is looking at
	var lengthmonth = [0,0,0];		// this is an array that knows the lengths of each month
	var fomonth = [0,0,0];			// this is an array that knows the first day of each month relative to the week
	var days0 = new Array();		// this is an array which holds the day objects in cal1
	var days1 = new Array();		// this is an array which holds the day objects in cal2
	var days2 = new Array();		// this is an array which holds the day objects in cal3
	var selected = [];			// this is an array for the first and second selected dates
	var debug = '';


	function settheyears(cmonth,cyear){
		if(cmonth==11){
			viewyear[0]=cyear;viewyear[1]=cyear+1;viewyear[2]=viewyear[1];
		}
		else if(cmonth==10){
			viewyear[0]=cyear;viewyear[1]=viewyear[0];viewyear[2]=cyear + 1;
		}
		else{
			viewyear[0]=cyear;viewyear[1]=viewyear[0];viewyear[2]=viewyear[0];
		}
	}


	function setthemonths(cmonth,cyear){
		if(cmonth==11){
			viewmonth[0]=11;viewmonth[1]=0;viewmonth[2]=1;
		}
		else if(cmonth==10){
			viewmonth[0]=10;viewmonth[1]=11;viewmonth[2]=0;
		}
		else{
			viewmonth[0]=cmonth;viewmonth[1]=cmonth+1;viewmonth[2]=cmonth+2;
		}
	}
	

	function getnumdays(){
        var day = new Date();
		for(i=0;i<3;i++){
			day.setFullYear(viewyear[i]);
	        day.setMonth(viewmonth[i]);
	        day.setDate(1);
	        fomonth[i]=day.getDay();

			day.setDate(1);
	        day.setMonth(viewmonth[i]+1);
	        day.setDate(-1);
			lengthmonth[i]=day.getDate();
		}
    }


	function getdaysarrays(){
		var days = 38;
		for(j=0;j<3;j++){
			for(i=0;i<days;i++){
				if(i<fomonth[j]){
					if(j==0){days0[i]='-';}
					else if (j==1){days1[i]='-';}
					else{days2[i]='-';}
				}
				else{
					if(i<fomonth[j]+lengthmonth[j]+1){
						if(j==0){
							if(i-fomonth[j]+1 > 9){days0[i]=String(i-fomonth[j]+1);}
							else{days0[i]='0'+String(i-fomonth[j]+1);}							
						}
						else if (j==1){
							if(i-fomonth[j]+1 > 9){days1[i]=String(i-fomonth[j]+1);}
							else{days1[i]='0'+String(i-fomonth[j]+1);}
						}
						else{
							if(i-fomonth[j]+1 > 9){days2[i]=String(i-fomonth[j]+1);}
							else{days2[i]='0'+String(i-fomonth[j]+1);}
						}
						
					}
				}
			}
		}
	}


	$('#prev_month').click(function(){
		if(cmonth==0){
			cmonth=11;cyear = cyear-1;
		}
		else{
			cmonth = cmonth-1;
		}
		updateview(cmonth,cyear);
	})
	
	$('#next_month').click(function(){
		if(cmonth==11){
			cmonth=0;cyear = cyear+1;
		}
		else{
			cmonth = cmonth+1;
		}
		updateview(cmonth,cyear);
	})
	
	$('.calday').live("click",function(){
		if(this.id.split('-')[2] != '-'){
			if(selected[0] != "" && selected[1] != ""){					// the end date and start date have a value
				selected[0]=this.id;selected[1]="";
				updatebetweens(selected[0],selected[1]);
				debug = 'both';
			}
			else{
				if(selected[0] != "" && selected[1] == ""){					// the start date has a value, but the end date doesn't
					selected[1]=this.id;
					if(selected[0]>selected[1]){							// check to make sure the end is greater than the start
						var switcher = selected[0];selected[0]=selected[1];selected[1]=switcher;
					}
					updatebetweens(selected[0],selected[1]);
					debug = '0 has a value and 1 is empty before the click';
				}
				if(selected[0] =="" && selected[1] ==""){					// the end date and start date are both empty
					selected[0]=this.id;selected[1]="";
					updatebetweens(selected[0],selected[1]);
					debug = '0 & 1 are both empty before the click';
				}
			}
		}
		var mystring = '12-03';var mynum = '12-20';if(mystring > mynum){debug='true';}

		
		// $('.somediv').append("selected[0] =" + selected[0] + " & selected[1] =" + selected[1] + "<br/>" + debug + "<br/><br/>");
	})
	
	function updatebetweens(start,end){
		$('.calday').removeClass("highlighted");
		$('#id_start_room').val(start);
		$('#id_end_room').val(end);

		
		if(start != "" && end != ""){				// there is a value for start and end
			$('.calday').each(function(i){
				if(this.id >= start && this.id <= end){
					$(this).addClass('highlighted');
				}
			})
		}
		if(start != ""){
			$('#' + start).addClass('highlighted');
		}

	}
	
	function updateview(cmonth,cyear){
		$('#1_cal > .caltitle > span').remove();
		$('#2_cal > .caltitle > span').remove();
		$('#3_cal > .caltitle > span').remove();
		$('.calday').remove();
		$('.caldaynill').remove();
		days0 = [];days1=[];days2=[];
		settheyears(cmonth,cyear);
		setthemonths(cmonth,cyear);
		getnumdays();
		getdaysarrays();


		$('#1_cal > .caltitle').append("<span>"+monthlist[viewmonth[0]] + " " + viewyear[0]+"</span>");
		$('#2_cal > .caltitle').append("<span>"+monthlist[viewmonth[1]] + " " + viewyear[1]+"</span>");
		$('#3_cal > .caltitle').prepend("<span>"+monthlist[viewmonth[2]] + " " + viewyear[2]+"</span>");
		for(i=0;i<days0.length;i++){
			if(days0[i]=='-'){
				$('#1_cal > .caldayboxes').append("<div class='caldaynill'>" + days0[i] + "</div>");
			}else{
				$('#1_cal > .caldayboxes').append("<div class='calday' id='" + viewyear[0]+"-"+(viewmonth[0]+1)+"-"+days0[i]+ "'>" + days0[i] + "</div>");
			}
		}
		for(i=0;i<days1.length;i++){
			if(days1[i]=='-'){
				$('#2_cal > .caldayboxes').append("<div class='caldaynill'>" + days1[i] + "</div>");				
			}else{
				$('#2_cal > .caldayboxes').append("<div class='calday' id='" + viewyear[1]+"-"+(viewmonth[1]+1)+"-"+days1[i]+ ">" + days1[i] + "</div>");				
			}

		}
		for(i=0;i<days2.length;i++){
			if(days2[i]=='-'){
				$('#3_cal > .caldayboxes').append("<div class='caldaynill'>" + days2[i] + "</div>");
			}else{
				$('#3_cal > .caldayboxes').append("<div class='calday' id='" + viewyear[2]+"-"+(viewmonth[2]+1)+"-"+days2[i]+ ">" + days2[i] + "</div>");
			}
		}
		selected[0]=String($('#id_start_room').val());
		selected[1]=String($('#id_end_room').val());
		updatebetweens(selected[0],selected[1]);
	}
	
	
	var cmonth = showday.getMonth();
	var cyear = showday.getFullYear();

	updateview(cmonth,cyear);

	// here is all the stuff for the resort

	// $('#new_resort_name').css({'display':'none'});
	// // $('#id_resort').prepend('<option value="newone" id="newone">Add a new Resort</option>');
	// $('#add_resort').click(function(){
	// 	$('.somediv').append($('#add_resort')[0].checked);
	// 	if($('#add_resort')[0].checked){
	// 		$('#new_resort_name').css({'display':''});
	// 		$('#id_resort').val(0);
	// 		$('#id_resort').attr("disabled", true);
	// 	}else{
	// 		$('#new_resort_name').css({'display':'none'});
	// 		$('#id_resort').removeAttr("disabled");
	// 	}
	// })
	
}
	

