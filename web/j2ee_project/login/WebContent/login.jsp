<%@ page language="java"  import="java.util.*" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>

<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>登录</title>
<script>
window.onload=function(){
	 createCode(4);    
   }

   //生成验证码的方法
   function createCode(length) {
       var code = "";
       var codeLength = parseInt(length); //验证码的长度
       var checkCode = document.getElementById("checkCode");
       ////所有候选组成验证码的字符，当然也可以用中文的
       var codeChars = new Array(0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'); 
       //循环组成验证码的字符串
       for (var i = 0; i < codeLength; i++)
       {
           //获取随机验证码下标
           var charNum = Math.floor(Math.random() * 62);
           //组合成指定字符验证码
           code += codeChars[charNum];
       }
       if (checkCode)
       {
           //为验证码区域添加样式名
           checkCode.className = "code";
           //将生成验证码赋值到显示区
           checkCode.innerHTML = code;
       }
   }
   if(checkCode.innerHTML!=document.getElementById("checkCode").value){
		alert("验证码错误");
		createCode(4);
		}

</script>
<style>
	body {
		line-height:300%;
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
		background-color:deepskyblue;
		padding: 8px 15px;
		text-align: center;
	    width:80px;
		color: white;
		border-radius: 17px;
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
	.d1{  /*对“用户登录”的操作*/
		position: relative;
		left: 43%;	
	}
	.d2{    /*对登录注册按钮的位置调整*/
		position: relative;
		left:36%;
	}
	#main{
	    white-space:nowrap; 
	}
	#checkCode{
	    border-style:none;
	}

</style>
<body>	
<div name="a"></div>
    <div id = "main">
    <form name="form2"   action="logincheck.jsp"  method="post"  class="f">
		<h3 class="d1">用户登录</h3>
		<table>
	        <tr>
				<td align="right">用户名：</td>
				<td><input class="input_box" type = "text" name = "user"></td>
			</tr>
	        <tr>
				<td align="right">密码：</td>
				<td><input class="input_box" type = "text" name = "password"></td>
	        </tr>
	        <tr>
				<td align="right">验证码：</td>
				<td><input class="input_box" type = "text" name = "yzm"></td>
				<td><p id = "checkCode" name = "yzm_1" onclick = "createCode(4)"></p></td>
	        </tr>

		</table>
	    <div class="d2">
			 <input  class="botton" type="submit" value="登录">
			<input class="botton" type="submit"  value="注册" onclick=window.open(logon.jsp) >
		</div>
	</form>
	</div>
</body>
</html>
