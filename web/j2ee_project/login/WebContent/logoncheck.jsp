<%@ page language="java" import="java.util.*"  import="java.sql.*" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>注册</title>
</head>
<body>
   <%
        Connection conn = null;
        PreparedStatement pstmt,pstmt2 = null;
        ResultSet rs = null;
        String driverName = "com.microsoft.sqlserver.jdbc.SQLServerDriver";         
        String userName = "sa";
        String userPwd = "sa.test";
        String dbName = "web";
        String url1 = "jdbc:sqlserver://localhost:1433;DatabaseName=web";
        request.setCharacterEncoding("UTF-8");
        Class.forName(driverName);
        conn = DriverManager.getConnection(url1,userName,userPwd);
        String sql = "insert into L values(?,?)";
        String sql2 = "select * from L where usr=? and psw=?";
        pstmt = conn.prepareStatement(sql);
        pstmt2 = conn.prepareStatement(sql2);
        String user = request.getParameter("user");
        String password = request.getParameter("password");
        System.out.println(user+password);
        
        if (user.length()<6){
        	%><script type="text/javascript" language="javascript">
        	alert("用户名少于6位，请重新输入!");
        	//document.getElementById("user").value = "";
        	//document.getElementById("psw").value = "";
        	window.document.location.href="logon.jsp";
        	</script><%
        }
        else if (password.length()<6){
        	%><script>
        	alert("密码小于6位，请重新输入！");
        	window.document.location.href="logon.jsp";
        	</script><%}
        
        else{
        pstmt.setString(1, user);
        pstmt2.setString(1, user);
        
        pstmt.setString(2, password);
        pstmt2.setString(2, password);
        
        pstmt.executeUpdate();
        rs = pstmt2.executeQuery();
        
        if(rs.next()) {
            %><center><h1>注册成功！</h1></center>
        <%}

        if(rs != null) {
            rs.close();
        }
        if(pstmt != null) {
            pstmt.close();
        }
        if(conn != null) {
            conn.close();
        }
        }
         
   %>
</body>
</html>