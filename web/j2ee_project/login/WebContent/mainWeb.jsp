<%@ page language="java"  import="java.util.*" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>mainWeb</title>
</head>
<style>
	body {
        margin: 0;
    }

	.topmenu{
		list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
        background-color: #777;
	}
	.topmenu li {
        float: left;
    }
	.topmenu li a:hover {
        background-color: #222;
    }
	.topmenu li a {
    display: inline-block;
    color: white;
    text-align: center;
    padding: 16px;
    text-decoration: none;
    }
	.topmenu li a:hover {
    background-color: #222;
    }
    .topmenu li a.active {
    color: white;
    background-color: #4CAF50;
    }
	.column {
    float: left;
    padding: 15px;
    }

    .clearfix::after {
    content: "";
    clear: both;
    display: table;
    }
    .sidemenu {
    width: 25%;
    }
	.column {
    float: left;
    padding: 15px;
}
.clearfix::after {
    content: "";
    clear: both;
    display: table;
}
.sidemenu {
    width: 18%;
}
.content {
    width: 75%;
}
.sidemenu ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
	border:solid #D8D8D8;
	border-radius: 5px;
}
.sidemenu li a {
    margin-bottom: 4px;
    display: block;
    padding: 8px;
    background-color: #eee;
    text-decoration: none;
    color: #666;
}
.sidemenu li a:hover {
    background-color: #555;
    color: white;
}
.sidemenu li a.active {
    background-color: #008CBA;
    color: white;
}
	.d1{
		float:left;
		text-align: center;
		width:20%;
		height:50px;

	}
	.d2{
		float:right;
		text-align: center;
		width:20%;
		height:50px;
		
	}
	.d{
		background-image:url("image\logo.png");
	}
	.d3{
	    border:1px solid #D8D8D8;
	    border-radius: 5px;
	}

</style>

<body>
	<div>
	<img src="images\logo.png" height="70px">
		<p align="right">杭电挖掘机小组</p>
	</div>
	<ul class="topmenu">
		<li><a href="mainWeb.jsp" class="active">首页</a></li>
		<li><a href="login.jsp">登录</a></li>
		<li><a href="logon.jsp">注册</a></li>
		<li><a href="#personal_center" >个人中心</a></li>
		<li><a href="#contact_us" >联系我们</a></li>
	</ul>

		<img src ="images\gate.jpg" style="height:170px;background-color: lightyellow;width:60% float:left;">
	    <img src ="images\hdu2.jpg" style="height:170px;background-color: lightyellow;width:50%;float:right;">
	<div style="background-color: lightgrey; height: 20px;padding:10px 0;">
	    <div class="d1">公告</div>
	    <div class="d1">房价动态</div>
		<div class="d1"></div>
	    <div class="d2">房价趋势</div>
	    <div class="d2">房价预测</div>
	</div>
	
     <div >
    <div class="column sidemenu">
	  
   <ul>
      <li><a href="#text1">text1</a></li>
      <li><a href="#text2" class="active">text2</a></li>
      <li><a href="#text3">text3</a></li>
	   <li><a href="#text4">text4</a></li>
	   <li><a href="#text5">text5</a></li>
	   <li><a href="#text6">text6</a></li>
	   <li><a href="#text7">text7</a></li>
    </ul>
	  
	  

  </div>

  <div class="column sidemenu">
	  
   <ul>
      <li><a href="#text1">text1</a></li>
      <li><a href="#text2" >text2</a></li>
      <li><a href="#text3">text3</a></li>
	   <li><a href="#text4">text4</a></li>
	   <li><a href="#text5">text5</a></li>
	   <li><a href="#text6">text6</a></li>
	   <li><a href="#text7">text7</a></li>
    </ul>
  </div>
</div>
	
	<div style="height:50px;width:40%;float:right;text-align: center">地区选择:</div><br><br><br>
	<table style="border:2px solid #D8D8D8;border-radius: 15px; width:40%;position: absolute;right:0;text-align: center">
		<tr>
		    <td width="500px" height="40px">
				<a href="#">钱塘新区</a>
			</td>
			<td width="500px" height="40px">2</td>
			<td width="500px" height="40px">3</td>
		</tr>
		<tr>
		    <td width="500px" height="40px">4</td>
			<td width="500px" height="40px">5</td>
			<td width="500px" height="40px">6</td>
		</tr>
		<tr>
		    <td width="500px" height="40px">7</td>
			<td width="500px" height="40px">8</td>
			<td width="500px" height="40px">9</td>
		</tr>
		<tr>
		    <td width="500px" height="40px"></td>
			<td width="500px" height="40px"></td>
			<td width="500px" height="40px"></td>
		</tr>
		<tr>
		    <td width="500px" height="40px"></td>
			<td width="500px" height="40px"></td>
			<td width="500px" height="40px"></td>
		</tr>
	</table>
	
</body>
</html>
