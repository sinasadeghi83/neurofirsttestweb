var colors = ["#DB6413", "red", "#3A3838", "#548135", "#833C0B", "#002060", "#92D050", "#5b9bd5"];
var countTrue = [0, 0, 0, 0, 0, 0, 0];
var musicState = ['', '400', '1000', '3000', '7000', '10000', '12000'];
var state = 0;
var countInState = 0;
var audio = -1;
var choosed = -1;
var trueId = -1;
$(document).ready(function(){
  $("#startbtn").click(function(){
    $("#nextbtn").attr("disabled", "true");
    $(".firstpage").hide();
    $("#heading").text('با دقت نگاه کنید');
    $(".timerpanel").show();
    $("#nextbtn").click(function(){
      if(false){
        alert("لطفا یکی از دایره ها را انتخاب کنید");
      }else{
        countInState++;
        if(choosed == trueId){
          countTrue[state]++;
        }
        if(countInState == 10){
          state++;
          countInState = 0;
          if(audio != -1){
            audio.pause();
          }
          if(state != 7){
            audio = new Audio("./"+musicState[state]+".wav");
            audio.loop = true;
            audio.play();
          }
          $("#t"+(state-1)).attr("value", countTrue[state-1]);
        }
        $(this).attr("disabled", "true");
        for(i = 0; i < 8; i++){
          $("#c"+i).remove();
        }
        $('#header').text("لطفا با دقت نگاه کنید");
        $('#header').css("color", "black");
        $('body').css("background", 'white');
        test();
      }
    });
    var distance = 5;
    var countDown = setInterval(function(){
      $("#timertext").text(distance);
      distance--;
      if(distance == -1){
        clearInterval(countDown);
        $(".timerpanel").hide();
        $(".tablepanel").show();
        $(".tablegrid").html(createTable());
        cellWidth = $(".tds").css("width");
        numCellWidth = Number(cellWidth.replace('px', ''));
        $(".tds").css("height", cellWidth);
        test();
      }
    }, 1000);
  });
});

function test(){
  if(state != 7){
    $("#nextbtn").css("display", 'inline-block');
    newRound();
  }else{
    $(".tablepanel").hide();
    $("#heading").text("نتیجه");

  }
}

function newRound(){
  var randomCircles = [];
  var radius = Number(cellWidth.replace('px', ''));
  $(".circle").css('display', 'inline-block');
  for(i = 0; i < 8; i++){
    var x = Math.floor(Math.random()*21) + 16 + radius;
    var y = Math.floor(Math.random()*12) + 16 + 2 * radius;
    while(isInCircle(x, y, randomCircles, radius)){
      x = Math.floor(Math.random()*21) * radius + 16 + radius;
      y = Math.floor(Math.random()*12) * radius + 16 + 2 * radius;
    }
    var temp = [x, y];
    randomCircles.push(temp);
    $("#nextbtn").before(createCircle(colors[i], radius, x, y, "c" + i));
  }
  setTimeout(function(){getAnswer(randomCircles, radius);}, 1480);
}

function getAnswer(randomCircles, radius){
  for(i = 0; i < 8; i++){
    $("#c"+i).css("display", "none");
  }
  var randoms4 = []
  var trueColor = '';
  for(i=0;i<4;i++){
    var mId = Math.floor(Math.random()*8);
    while(containsObject(mId,randoms4)){
      mId = Math.floor(Math.random()*8);
    }
    randoms4.push(mId);
    if(i==0){
      trueColor = $("#c"+mId).css('background-color');
      trueId = mId;
      console.log(trueColor + " " + mId + " " );
    }
    $("#c"+mId).css("background", "none");
    $("#c"+mId).css("border", "1px solid #000");
    $("#c"+mId).css("display", "inline-block");
  }
  $('#header').text("دایره مورد نظر با رنگ متن را انتخاب کنید");
  $('#header').css("color", trueColor);
  $('body').css("background", trueColor);
  if(state == 6 && countInState == 9){
    $("#formpanel").css("display", 'block');
    $("#nextbtn").css("display", 'none');
  }
  $('.circle').click(function(){
    for(i = 0; i < 4; i++){
      $("#c"+randoms4[i]).css("background", "none");
      $("#c"+randoms4[i]).css("opacity", 1);
    }
    document.getElementById("nextbtn").disabled = false;
    choosed = Number($(this).attr('id').replace("#c", ""));
    $(this).css("background", "green");
    $(this).css("opacity", "0.2");
    if(state == 6 && countInState == 9){
      if(choosed){
        countTrue[state]++;
      }
      $("#t"+(state)).attr("value", countTrue[state]);
    }
  });
  // $("#nextbtn").click(function(){
  //   if(false){
  //     alert("لطفا یکی از دایره ها را انتخاب کنید");
  //   }else{
  //     countInState++;
  //     if(choosed == randoms4[0]){
  //       countTrue[state]++;
  //     }
  //     if(countInState == 10){
  //       state++;
  //       countInState = 0;
  //       if(audio != -1){
  //         audio.pause();
  //       }
  //       if(state != 7){
  //         audio = new Audio("./"+musicState[state]+".wav");
  //         audio.play();
  //       }
  //       $("#t"+(state-1)).attr("value", countTrue[state-1]);
  //     }
  //     $(this).attr("disabled", "true");
  //     for(i = 0; i < 8; i++){
  //       $("#c"+i).remove();
  //     }
  //     $('#header').text("لطفا با دقت نگاه کنید");
  //     test();
  //   }
  // });
}

function containsObject(obj, list) {
    var i;
    for (i = 0; i < list.length; i++) {
        if (list[i] === obj) {
            return true;
        }
    }

    return false;
}

function isInCircle(x, y, circles, radius){
  for(i = 0; i < circles.length; i++){
    dx = Math.abs(x - circles[i][0]);
    dy = Math.abs(y - circles[i][1]);
    dis = Math.sqrt(dx*dx + dy*dy)
    if(dis < 2*radius)
      return true;
  }
  return false;
}

function createCircle(color, cellWidth, x, y, mid){
  var circlev = '<span style="opacity:1; background-color:'+color+'; width:'+2*cellWidth+'px; height:'+2*cellWidth+'px; bottom:'+y+'px; right:'+x+'px;" class="circle" id="'+mid+'"></span>';
  return circlev;
}

function createTable(){
  var tablev = '';
  for(i = 0; i < 13; i++){
    tablev+='<tr>';
    for(j=0;j<22;j++){
      tablev+='<td class="tds"></td>';
    }
    tablev+='<tr/>';
  }
  return tablev;
}
