<?php
session_start();
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
// Start the session

?>   
<!DOCTYPE html>
<html>
<head>
<?php
//DATABSE DETAILS//
// $host_name="localhost";
// $user_name="gspecrmc_user";
// $password="gspepws123";
// $database="gspecrmc_data";

date_default_timezone_set('Asia/Jakarta');
?>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Login</title>

<link href="assets/css/bootstrap.min.css" rel="stylesheet">
</head>

<?php
 include('config/connect.php');
if(isset($_POST['tSubmit'])){
 $Name = $_POST['Name'];
 $Pass = $_POST['Pass'];
	 //$dept_id =  $_POST['dept_id'];
	 $sql = mysqli_query($con, "SELECT * FROM User WHERE name='$Name' AND password='$Pass'") or die(mysqli_error());
	 if(mysqli_num_rows($sql) == 0){
	  echo "<script>alert('Username or Password is incorrect')</script>";
	 }else{
	 	mysqli_query($con, "UPDATE User SET last_login=CURRENT_TIMESTAMP() WHERE NAME='admin'");
	 	$row = mysqli_fetch_assoc($sql);
	 	$_SESSION['ID']=$row['id'];
	 	$_SESSION['name']=$Name;
	   echo '<script language="javascript">document.location="generaldata.php";</script>';
	 }
}
?>
<body>
	<br>
	<div class="row">
		<div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
			<div class="login-panel panel panel-default">
				<img class="img-responsive" alt="GSPE" src="images/logo_gspe.jpeg" style="margin: auto;">
				<div class="panel-heading"><b>Login</b></div>
				<div class="panel-body">
					<form role="form" name="LoginF" action="login.php" method="POST">
						<fieldset>
							<div class="form-group">
								<input class="form-control" placeholder="Username" name="Name" type="text" autofocus="">
							</div>
							<div class="form-group">
								<input class="form-control" placeholder="Password" name="Pass" type="password">
							</div>
							<br>
							<input type="Submit" class="btn btn-primary" name="tSubmit" value=" Login ">
						</fieldset>
					</form>
				</div>
			</div>
		</div><!-- /.col-->
	</div><!-- /.row -->	
	<script src="js/jquery-1.11.1.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<!-- <script src="js/chart.min.js"></script>
	<script src="js/chart-data.js"></script>
	<script src="js/easypiechart.js"></script>
	<script src="js/easypiechart-data.js"></script>
	<script src="js/bootstrap-datepicker.js"></script> -->
	<script>
		!function ($) {
			$(document).on("click","ul.nav li.parent > a > span.icon", function(){		  
				$(this).find('em:first').toggleClass("glyphicon-minus");	  
			}); 
			$(".sidebar span.icon").find('em:first').addClass("glyphicon-plus");
		}(window.jQuery);

		$(window).on('resize', function () {
		  if ($(window).width() > 768) $('#sidebar-collapse').collapse('show')
		})
		$(window).on('resize', function () {
		  if ($(window).width() <= 767) $('#sidebar-collapse').collapse('hide')
		})
	</script>	
</body>
<!-- <footer>
	<div class="form-group">
		<h5 style="text-align: center; font-family: Arial, Helvetica, sans-serif;">Supported by :</h5>
		<img class="img-responsive" alt="GSPE" src="images/logo_gspe.jpeg" style="width: 20%; height: 20%; margin: auto;">
		<hr style="border-style: inset; border-width: 2px; margin-left:10%; margin-right: 10%;">
	</div>
</footer> -->
</html>