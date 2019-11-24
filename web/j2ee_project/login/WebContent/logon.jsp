<%@ page language="java"  import="java.util.*" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>注册</title>
</head>
<style>
	body {
		line-height:250%;
		width: 100%;
		height: 100%
		background-color:#F0F0F0;
		/*background-image: url("images/background.jpg")*/
	}
	select {
		width: 160px;
	}

    .input_box {
        border-color:cornflowerblue;
		border: 1px solid cornflowerblue;
		border-radius: 15px;
	    height:30px;
		width:150px;
		}
	span {
		color: red;
    }
	.botton {
		border:1px solid black;
		border-radius: 3px;
		background-color:deepskyblue;
		padding: 8px 15px;
		text-align: center;
	    width:100px;
		color: white;
		border-radius: 20px;
	}
	.botton1{
		background-color: lightgray;
	}

	.f{ /*对整个框的操作*/
		
		border:2px solid none;
		padding:10px 40px; 
		border-radius:10px;
		width:25%;
		height: 70%;
		position: absolute;
		top:50%;
		left:80%;
		transform: translate(-50%,-50%);
	}
	.d1{  /*对“用户注册”的操作*/
		border:1px solid #2894FF;
		border-radius: 6px;
		background-color: white;
		position: absolute;
		top:0;
		left:50px;
		transform: translate(-50%,-50%);
		
	}
	#main{
	    white-space:nowrap; 
	}
	#b{
	position:relative;
	left:-5%;
	text-align:center;
	}
</style>
<body>	
    <div id = "main">
	<form action="logoncheck.jsp" method ="post" class="f">
		<h3 align="center">用户注册</h3>
		<table align="center">
	        <tr>
				<td align="right">用户名：</td>
				<td><input class="input_box" type = "text" name = "user"><span>*(最多30个字符)</span></td>
			</tr>
	        <tr>
				<td align="right">密码：</td>
				<td><input class="input_box" type = "text" name = "password"><span>*(最多30个字符)</span></td>
	        </tr>
			
		</table>
	    <div id = "b">
	        <br><input  class="botton" type="submit" value="注册">
			<br><input class="botton botton1" type="submit"  value="返回登录" a>
		</div>
	</form>
	</div>
</body>
</html>
