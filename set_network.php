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
              <div class="panel-heading" style="font-size: 11px;"><b>Network Settings</b></div>
              <div class="panel-body" style="font-size: 10px;">
                <form role="form" name="LoginF" action="set_network.php" method="POST">
                  <fieldset>
                    <div class="form-group">
                      <label>IP Address</label>
                      <input class="form-control" placeholder="IP Address" value=<?php echo $contentsDecoded['ipAddress']; ?> name="ipaddress" title="IP Address" type="text" autofocus="">
                    </div>
                    <div class="form-group">
                      <label>Netmask</label>
                      <input class="form-control" placeholder="Netmask" value=<?php echo $contentsDecoded['netMask']; ?> name="netmask" type="text" title="Netmask">
                    </div>
                    <div class="form-group">
                      <label>Gateway</label>
                      <input class="form-control" placeholder="Gateway" value=<?php echo $contentsDecoded['gateway']; ?> name="gateway" type="text" title="Gateway">
                    </div>
                    <div class="form-group">
                      <label>SNMP Version</label>
                      <input class="form-control" placeholder="SNMP Version" value=<?php echo $contentsDecoded['snmpVersion']; ?> name="snmp_version" type="text" title="SNMP Version">
                    </div>
                    <div class="form-group">
                      <label>SNMP Community</label>
                      <input class="form-control" placeholder="SNMP Community" value=<?php echo $contentsDecoded['snmpCommunity']; ?> name="snmp_comm" type="text" title="SNMP Community">
                    </div>
                    <div class="form-group">
                      <label>SNMP Port</label>
                      <input class="form-control" placeholder="SNMP Port" value=<?php echo $contentsDecoded['snmpPort']; ?> name="snmp_port" type="text" title="SNMP Port">
                    </div>
                    <div class="form-group">
                      <label>Sys OID</label>
                      <input class="form-control" placeholder="Sys OID" value=<?php echo $contentsDecoded['sysOID']; ?> name="sys_oid" type="text" title="Sys OID">
                    </div>
                      <center><input type="Submit" class="btn btn-primary" name="tSubmit" value="Update" style="font-size: 10px;"> | <a href="confirmation_reset.php"><input type="button" class="btn btn-danger" name="" value="Reset" style="font-size: 10px;"></a></center>
                    </fieldset>
                </form>
                <?php 
                if(isset($_POST['tSubmit'])){
                  // echo "<script>alert('Are you sure you want edit networks ? if yes, device will be restart please you waiting 1 minute')</script>";
                  
                  $contentsDecoded['ipAddress']=$_POST["ipaddress"];
                  $contentsDecoded['netMask']=$_POST["netmask"];
                  $contentsDecoded['gateway']=$_POST["gateway"];
                  $contentsDecoded['snmpVersion']=$_POST["snmp_version"];
                  $contentsDecoded['snmpCommunity']=$_POST["snmp_comm"];
                  $contentsDecoded['snmpPort']=$_POST["snmp_port"];
                  $contentsDecoded['sysOID']=$_POST["sys_oid"];

                  $json = json_encode($contentsDecoded);
                  $update = file_put_contents('json/Comm.json', $json);
                  //exec("python /var/www/html/reboot.py");
                  exec("cd /var/www/html");
                  exec("./reboot");
                  if($update) {
                    echo "<script>alert('Data successfully changed')</script>";
                  }else {               
                    echo "<script>alert('Data failed changed')</script>";                
                  }
                    echo "<meta http-equiv='refresh' content='0; url=set_network.php'>";
                }
                
                ?>
              </div>
            </div>
        </div><!-- /.col-->
    </div>
  <!-- </form> -->
</body>
<?php include ('footer.php'); ?>