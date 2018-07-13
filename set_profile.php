<?php
include ('config/connect.php');
include ('navbar.php');
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
date_default_timezone_set('Asia/Jakarta');
session_start();
if (!isset($_SESSION['ID'])){
// Jika Tidak Arahkan Kembali ke Halaman Login
  header("location: login.php");
} 
?>
<body>
<!--   <form name="form1" method="post" action=""> -->
    <div class="container table-responsive">
        <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
            <div class="login-panel panel panel-default">
              <div class="panel-heading"><b>Profile Settings</b></div>
              <div class="panel-body">
                <form role="form" name="profile" action="set_profile.php" method="POST">
                  <fieldset>
                    <?php
                      $sql = mysqli_query($con, "SELECT * FROM `User`") or die(mysqli_error());
                      $i=0;
                      $data = mysqli_fetch_assoc($sql);
                    ?>
                    <div class="form-group">
                      <label>Username</label>
                      <input class="form-control" placeholder="Username" value=<?php echo $data["name"];?> name="username" title="Username" type="text" autofocus="" readonly>
                    </div>
                    <div class="form-group">
                      <label>Password</label>
                      <input class="form-control" placeholder="Password" value=<?php echo $data["password"]; ?> name="password" type="password" title="Password">
                    </div>
                      <center><input type="Submit" class="btn btn-primary" name="tSubmit" value="Update"></center>
                    </fieldset>
                </form>
                <?php 
                if(isset($_POST['tSubmit'])){
                  $password= $_POST["password"];
                  
                  $update = mysqli_query($con, "UPDATE User SET PASSWORD ='$password' WHERE NAME='admin'");
                  if($update) {
                  ?>
                    <script type="text/javascript">
                      alert("Password successfully changed");
                    </script>
                  <?php
                    }
                    else {
                  ?>                
                      <script type="text/javascript">
                      alert("Password failed changed");
                    </script>                
                  <?php
                    }
                    echo "<meta http-equiv='refresh' content='0; url=set_profile.php'>";

                  }
                  ?>
              </div>
            </div>
        </div><!-- /.col-->
    </div>
  <!-- </form> -->
</body>
<?php include ('footer.php'); ?>