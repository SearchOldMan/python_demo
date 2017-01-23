<?php 

 ?>
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>商羊资产</title>
	 <!-- 引入百度的cdn服务 -->
	<link rel="stylesheet" href="http://apps.bdimg.com/libs/bootstrap/3.3.4/css/bootstrap.css">
	<script src="http://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
	<script src="http://apps.bdimg.com/libs/bootstrap/3.3.4/js/bootstrap.min.js"></script>
	<!-- 自己的css和js文件 -->
	<link rel="stylesheet" href="../css/sample.css">
	<link rel="shortcut icon" href="../images/syzc.ico">
	<script src="../js/myjs.js"></script>
</head>
<body>
<div class="tel">
		<table class="tel_table">
			<th>
				<td>
					<img src="../images/wico03.png" alt="">
				</td>
				<td>
					<b style="color:#c4c4c4">客服电话0591 83321371  关注我们</b>
				</td>
				<td>
					<a href="" data-toggle="modal" data-target="#myModal"><img src="../images/wico02.png" alt=""></a>
				</td>
				
			</th>
		</table>
	</div>
	<!-- 模态框用来存放公司的二维码 -->
	<!-- Modal -->
	<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
	  <div class="modal-dialog" style="width: 300px;">
	    <div class="modal-content">
	      <div class="modal-header">
	     	<img src="../images/qrcode.jpg" alt="">   
	      </div>
	      <div class="modal-footer">
	        <p style="font-size:14px;">打开微信，点击底部的"发现",使用"扫一扫"</p>
	        <p style="font-size:14px;text-align:center;">即可关注商羊资产官方微信</p>
	      </div>
	    </div>
	  </div>
	</div>
	<!-- logo、导航栏 -->
	<div class="container" class="logo">
		<table>
			<tr>
				<td>
					<img src="../images/logo.jpg" class="logo_img" alt="" style="height: 100px;">
				</td>
				<td style="position: relative;" class="col-md-6 col-xs-8">
					<span style="font-size: 30px;position: absolute;bottom:0;">上海商羊资产管理有限公司</span>
				</td>
				<td class="nav_header col-md-8" style="position: relative;">
					<ul>
						<li><a href="./home.html">首页</a></li>
						<li>|</li>
						<li><a href="./produces_center.html">产品中心</a></li>
						<li>|</li>
						<li><a href="./about_us.html">关于我们</a></li>
						<li>|</li>
						<li><a href="./about_us.html">招贤纳士</a></li>
						<li>|</li>
						<li><a href="./chat_us.html">联系我们</a></li>
					</ul>
				</td>
			</tr>
		</table>
	</div>
	<div class="main_content">
		<div class="container user_message" style="background-color: #fff;height:700px;">
			<div class="title">
				<h2>产品净值</h2>
			</div>
			<div class="panel panel-warning col-md-3" style="margin: 0;padding:0">
				<div class="panel-heading">
					<h3 class="panel-title">基金产品</h3>
				</div>
				<ul class="list-group chanpin-list">
					<li class="list-group-item" id="1">商羊盈信1号</li>
					<li class="list-group-item" id="2">金友商羊1号</li>
					<li class="list-group-item" id="3">商羊进取1号</li>
					<li class="list-group-item" id="4">商羊盈信3号</li>
					<li class="list-group-item" id="5">商羊盈信5号</li>
					<li class="list-group-item" id="6">兴鑫商羊2号</li>
					<li class="list-group-item" id="7">商羊进取2号</li>
					<li class="list-group-item" id="8">商羊盈信6号</li>
				</ul>
			</div>
		</div>
	</div>
	<!-- 尾部版权区域 -->
	<div class="footer">
		<ul class="copy_ul">
			<li>关于我们</li>
			<li>|</li>
			<li>招贤纳士</li>
			<li>|</li>
			<li>产品中心</li>
			<li>|</li>
			<li>联系我们</li>
		</ul>
		<p class="copy_p">
			©2016 闽ICP备16002209号
		</p>
	</div>

	<script>
		showDetail();
	    function showDetail(){
	      var lis = $('.chanpin-list li');
	      lis.click(function(){
	        console.log($(this).attr('id'))
	      });
	    }
	</script>
</body>
</html>
