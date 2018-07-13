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

$contents = file_get_contents('json/Comm.json');
$contentsDecoded = json_decode($contents, true);

?>
<body>
<!--   <form name="form1" method="post" action=""> -->
    <div class="container table-responsive">
        <div class="col-xs-10 col-xs-offset-1 col-sm-8 col-sm-offset-2 col-md-4 col-md-offset-4">
            <div class="login-panel panel panel-default">
              <div class="panel-heading" style="font-size: 11px;"><b>Are you sure want reset the network ?</b></div>
              <div class="panel-body" style="font-size: 10px;">
                <form role="form" name="LoginF" action="confirmation_reset.php" method="POST">
                  <fieldset>
                    
                      <center><input type="Submit" class="btn btn-success" name="yes" value="Yes" style="font-size: 10px;"> | <a href="set_network.php"><input type="button" class="btn btn-danger" name="no" value="No" style="font-size: 10px;"></a></center>
                    </fieldset>
                </form>
                <?php 
                if(isset($_POST['yes'])){
                    
                    $contentsDecoded['ipAddress']="192.168.2.100";
                    $contentsDecoded['netMask']="255.255.255.0";
                    $contentsDecoded['gateway']="192.168.2.1";
                    $contentsDecoded['snmpVersion']="2";
                    $contentsDecoded['snmpCommunity']="public";
                    $contentsDecoded['snmpPort']="161";
                    $contentsDecoded['sysOID']=".1.3.6.1.4.1.10000.10.1";

                    $json = json_encode($contentsDecoded);
                    $update = file_put_contents('json/Comm.json', $json);
                    exec("cd /var/www/html/");
                    exec("./reboot");
                    if($update) {
                      echo "<script>alert('Data successfully reset')</script>";
                    }
                    //echo "<meta http-equiv='refresh' content='0; url=set_network.php'>";
                }
                ?>
              </div>
            </div>
        </div><!-- /.col-->
    </div>
  <!-- </form> -->
</body>