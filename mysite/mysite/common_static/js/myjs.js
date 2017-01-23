$(function(){
    //第一张显示
    $(".pic li").eq(0).show();
    //鼠标滑过手动切换，淡入淡出
    $("#position li").mouseover(function() {
      $(this).addClass('cur').siblings().removeClass("cur");
      var index = $(this).index();
      i = index;//不加这句有个bug，鼠标移出小圆点后，自动轮播不是小圆点的后一个
      // $(".pic li").eq(index).show().siblings().hide();
      $(".pic li").eq(index).fadeIn(500).siblings().fadeOut(500);
    });
    //自动轮播
    var i=0;
    var timer=setInterval(play,2000);
    //向右切换
    var play=function(){
      i++;
      i = i > 2 ? 0 : i ;
      $("#position li").eq(i).addClass('cur').siblings().removeClass("cur");
      $(".pic li").eq(i).fadeIn(500).siblings().fadeOut(500);
      console.log(i);
    }
    //向左切换
    var playLeft=function(){
      i--;
      i = i < 0 ? 2 : i ;
      $("#position li").eq(i).addClass('cur').siblings().removeClass("cur");
      $(".pic li").eq(i).fadeIn(500).siblings().fadeOut(500);
    }
    //鼠标移入移出效果
    $(".banner").hover(function() {
      clearInterval(timer);
    }, function() {
      timer=setInterval(play,2000);
    });
    //左右点击切换
    $("#prev").click(function(){
      playLeft();
    })
    $("#next").click(function(){
      play();
    })


    /*关于我们*/

    $('#obj_list').children().click(function(){
      $(this).addClass('active').siblings().removeClass('active');
      if($(this).html() === '公司介绍'){
        $('#construction').show();
        $('.history').hide();
        $('.job').hide();
      }else if($(this).html() === '成长历史'){
        $('.history').show();
        $('#construction').hide();
        $('.job').hide();
      }else{
        $('.history').hide();
        $('#construction').hide();
        var lis = $(this).children('ul').children('li');
        lis.click(function(){
          $('.job').show();
          $('.job div').hide();
          var names = $(this).attr('id');
          $('#tab-obj'+names).show();
        });
        }
    });

    /*阅读声明*/
    $('#iSure').click(function(){
      $('#iamvaildInvestor').click(function(){
        $('.read_only').hide();
        $('.footer').show();
      });
    });

    /*注册框架*/
    $('#submit3').click(function(){
      var pw1 = $('#inputPassword3').val();
      var pw2 = $('#repeat_inputPassword3').val();
      var inputName = $('#inputName').val();
      var inputNumber = $('#inputNumber').val();
      var inputEmail3 = $('#inputEmail3').val();
      if(pw1 != pw2 || inputName == '' || inputNumber == '' || inputEmail3 == ''){
        alert('注册失败');
        return false;
      }else{
        alert('注册成功');
        return true;
        window.location.reload();
      }
    });
 });
        
      