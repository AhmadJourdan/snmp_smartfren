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
<?php
  $base_url = "http://" . $_SERVER['SERVER_NAME']."";
  $result = file_get_contents("json/Comm.json");
  $json_object = json_decode($result);
  $sql = mysqli_query($con, "SELECT DATE(TIMESTAMP + INTERVAL 3 MONTH) AS backup_date FROM GeneralData ORDER BY TIMESTAMP ASC LIMIT 1");
  $data = mysqli_fetch_assoc($sql);
  $backup_date = $data['backup_date'];
?>
<meta http-equiv="refresh" content="10">
<body>
  <!-- <MARQUEE align="center" direction="left" height="20" scrollamount="6" width="100%" behavior="alternate" style="background-color: #1d388c; color: white; margin-top:-10%;">Please backup data before <?php echo $backup_date; ?> !!!</MARQUEE> -->
  <form name="form1" method="post" action="communication_excel.php">
    <div class="container table-responsive">
      <table>
        <tr>
          <td><label>Date</label></td>
          <td><label>:</label></td>
          <td>&nbsp;</td>
          <td>
            <div class="form-group">
              <div class="input-group date form_date" data-date="" data-date-format="mm dd yyyy" data-link-field="dari" data-link-format="yyyy-mm-dd hh:mm:ss">
                    <input class="form-control" id="dari" name="dari" size="16" type="text">
                          <span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>
                <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
                      </div>
            </div>
          </td>
          <td>&nbsp;-&nbsp;</td>
          <td>
            <div class="form-group">
              <div class="input-group date form_date" data-date="" data-date-format="mm dd yyyy" data-link-field="sampai" data-link-format="yyyy-mm-dd hh:mm:ss">
                      <input class="form-control" id="sampai" name="sampai" size="16" type="text">
                          <span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>
                <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
                      </div>
            </div>
          </td>
          <td>&nbsp;&nbsp;</td>
          <td>
            <div class="form-group">
              <input name="export" value="Export" type="Submit" id="export" class="btn btn-primary">
            </div>
          </td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td><h4><?php echo "Latest Update : ".$json_object->Timestamp ?></h4></td>
        </tr>
      </table>
      <br>
    </div>
  </form>
    <!-- <div class="container table-responsive">
      <div class="col-md-4"></div>
      <div class="col-md-4" style="background-color: #f9f9f9; border-radius: 15px;">
        <fieldset>
          <legend>Communication</legend>
          <table>
            <tr>
              <td width="110px;"><label>Ip Address</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->ipAddress; ?> readonly></td>
            </tr>
            <tr>
              <td><label>Netmask</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->netMask; ?> readonly></td>
            </tr>
            <tr>
              <td><label>Gateway</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->gateway; ?> readonly></td>
            </tr>
            <tr>
              <td><label>SNMP Version</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->snmpVersion; ?> readonly></td>
            </tr>
            <tr>
              <td><label>SNMP Community</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->snmpCommunity; ?> readonly></td>
            </tr>
            <tr>
              <td><label>SNMP Port</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->snmpPort; ?> readonly></td>
            </tr>
            <tr>
              <td><label>Sys OID</label></td>
              <td><input type="text" class="form-control" style="height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->sysOID; ?> readonly></td>
            </tr>  
          </table>
          
        </fieldset>
      </div>
      <div class="col-md-4"></div>
    </div> -->
</body>
<?php include ('footer.php'); ?>
<script type="text/javascript">
  $('.form_date').datetimepicker({
  language: 'id',
  weekStart: 0,
  todayBtn:  1,
  autoclose: 1,
  todayHighlight: 1,
  startView: 2,
  minView: 2,
  forceParse: 0
  });
</script>