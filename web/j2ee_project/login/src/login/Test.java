package login;

import java.sql.*;

public class Test {

public static void main(String[] args) {
      String driverName="com.microsoft.sqlserver.jdbc.SQLServerDriver";//SQL数据库引擎
     String dbURL="jdbc:sqlserver://localhost:1433;DatabaseName=web";//数据源  ！！！！注意若出现加载或者连接数据库失败一般是这里出现问题
     String Name="sa";
     String Pwd="sa.test";
   try
   {
   Class.forName(driverName);
   Connection conn=DriverManager.getConnection(dbURL,Name,Pwd);
   System.out.println("连接数据库成功");
   }catch(Exception e){
    e.printStackTrace();
      System.out.println("连接失败");
      }
   }

}