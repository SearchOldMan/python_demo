<?php 
header('Content-Type:text/html;charset=utf-8');
$host = '';
$username = '';
$password = '';
$dbName = '';
$port = '';
//连接数据库
$conn = mysql_connect($host,$username,$password) or die("error connecting");
//设置编码
mysql_query("set names utf8");
//打开数据库
mysql_select_db($dbName);
//sql语句
$sql = 'select * from ';
//查询
$result = mysql_query($sql,$conn);
//封装到一个数组里
$row = mysql_fetch_array($result);

//以json的方式返回
echo json_encode($row);
//关闭连接
$conn.close();
 ?>


