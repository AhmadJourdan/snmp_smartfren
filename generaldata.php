<?php
include ('config/connect.php');
include ('navbar.php');
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
date_default_timezone_set('Asia/Jakarta');
// session_start();
// if (!isset($_SESSION['ID'])){
// // Jika Tidak Arahkan Kembali ke Halaman Login
//   header("location: login.php");
// } 
?>
<?php
    $base_url = "http://" . $_SERVER['SERVER_NAME']."";
    $result = file_get_contents("json/GenData.json");
    $json_object = json_decode($result);
    $sql = mysqli_query($con, "SELECT DATE(TIMESTAMP + INTERVAL 3 MONTH) AS backup_date FROM GeneralData ORDER BY TIMESTAMP ASC LIMIT 1");
    $data = mysqli_fetch_assoc($sql);
    $backup_date = $data['backup_date'];
?>
<!-- <meta http-equiv="refresh" content="10"> -->
<body>
  <form name="form1" method="post" action="generaldata_excel.php">
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
              <input name="export" value="Export" type="Submit" id="export" class="btn btn-primary" formaction="generaldata_excel.php">
            </div>
          </td>
        </tr>
      </table>
      <br>
    </div>
  </form>
    <!-- <div class="container table-responsive">
      <div class="col-md-3"></div>
      <div class="col-md-5" style="background-color: #f9f9f9; border-radius: 15px;">
        <fieldset>
          <legend>Overview</legend>
          <table>
            <tr>
              <td width="110px;"><label>CV</label></td>
              <td><input type="text" class="form-control" style="width: 50%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->CV; ?> readonly></td>
              <td><label>Volt</label></td>
            </tr>
            <tr>
              <td><label>CCL</label></td>
              <td><input type="text" class="form-control" style="width: 50%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->CCL; ?> readonly></td>
              <td><label>Ampere</label></td>
            </tr>
            <tr>
              <td><label>DCL</label></td>
              <td><input type="text" class="form-control" style="width: 50%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->DCL; ?> readonly></td>
              <td><label>Ampere</label></td>
            </tr>
            <tr>
              <td><label>EDV</label></td>
              <td><input type="text" class="form-control" style="width: 50%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->EDV; ?> readonly></td>
              <td><label>Volt</label></td>
            </tr>
            <tr>
              <td><label>Bus Volt</label></td>
              <td><textarea class="form-control" rows="1" readonly="" style="margin-bottom: 3px; width: 150px;"><?php echo $json_object->Bus_Volt; ?></textarea></td>
              <td><label>Volt</label></td>
            </tr>
            <tr>
              <td><label>Bus Curr</label></td>
              <td><textarea class="form-control" rows="1" readonly="" style="margin-bottom: 3px; width: 150px;"><?php echo $json_object->Bus_Curr; ?></textarea></td>
              <td><label>Ampere</label></td>
            </tr>
            <tr>
              <td><label>Detected Mod</label></td>
              <td><input type="text" class="form-control" style="width: 50%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Detected_Mod; ?> readonly></td>
              <td><label>Module</label></td>
            </tr>
            <tr>
              <td><label>Capacity</label></td>
              <td><textarea class="form-control" rows="1" readonly="" style="margin-bottom: 3px; width: 150px;"><?php echo $json_object->Capacity; ?></textarea></td>
              <td><label>Ah</label></td>
            </tr>
            <tr>
              <td><label>BackupTime</label></td>
              <td><textarea class="form-control" rows="1" cols="25" readonly="" style="margin-bottom: 3px; width: 210px;"><?php echo $json_object->BackupTime; ?></textarea></td>
            </tr>
            <tr>
              <td><label>Status</label></td>
              <td><textarea class="form-control" rows="6" readonly="" style="margin-bottom: 3px; width: 210px;"><?php echo $json_object->Status; ?></textarea></td>
            </tr>
            <tr>
              <td><label>Warning</label></td>
              <td><textarea class="form-control" rows="6" readonly="" style="margin-bottom: 3px; width: 210px;"><?php echo $json_object->Warning; ?></textarea></td>
            </tr>
            <tr>
              <td><label>Alarm</label></td>
              <td><textarea class="form-control" rows="6" readonly="" style="margin-bottom: 3px; width: 210px;"><?php echo $json_object->Alarm; ?></textarea></td>
            </tr>  
            <tr>
              <td><label>Error</label></td>
              <td><textarea class="form-control" rows="6" readonly="" style="margin-bottom: 3px; width: 210px;"><?php echo $json_object->Error; ?></textarea></td>
            </tr>
          </table>
          
        </fieldset>
      </div>
      <div class="col-md-3"></div>
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