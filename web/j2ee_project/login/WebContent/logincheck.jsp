<%@ page language="java" import="java.util.*"  import="java.sql.*" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>登录</title>
</head>
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
<body>
   <%
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        String driverName = "com.microsoft.sqlserver.jdbc.SQLServerDriver";         
        String userName = "sa";
        String userPwd = "sa.test";
        String dbName = "web";
        String url1 = "jdbc:sqlserver://localhost:1433;DatabaseName=web";
        request.setCharacterEncoding("UTF-8");
        Class.forName(driverName);
        conn = DriverManager.getConnection(url1,userName,userPwd);
        String sql = "select * from L where usr=? and psw=?";
        pstmt = conn.prepareStatement(sql);
        String user = request.getParameter("user");
        String password = request.getParameter("password");
        String yzm = request.getParameter("yzm");
        String yzm_1 = request.getParameter("yzm_1");
        System.out.println(yzm_1);
        pstmt.setString(1, user);
        pstmt.setString(2, password);
        rs = pstmt.executeQuery();
        System.out.println(rs);
        
        if(rs.next()) {
            %><center><a href = "mainWeb.jsp">点击返回主页</a></center>
        <%}
        else {
            %><script>
        	alert("账号或密码输入错误，请重新输入！");
        	window.document.location.href="login.jsp";
        	</script><%
        }
        
        if(rs != null) {
            rs.close();
        }
        if(pstmt != null) {
            pstmt.close();
        }
        if(conn != null) {
            conn.close();
        }
         
   %>
</body>
</html>