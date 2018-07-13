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
$sql = mysqli_query($con, "SELECT DATE(TIMESTAMP + INTERVAL 3 MONTH) AS backup_date FROM GeneralData ORDER BY TIMESTAMP ASC LIMIT 1");
$data = mysqli_fetch_assoc($sql);
$backup_date = $data['backup_date'];
?>
      <?php
              $module = $_POST["module"];
              $final_module = "Module".$module."";
              //echo '<center><h4>Data '.$final_module.'</h4></center>';
              $base_url = "http://" . $_SERVER['SERVER_NAME'].""; 
              if($final_module=="Module1"){
                $result = file_get_contents("json/mod1.json");  
              }elseif($final_module=="Module2"){
                $result = file_get_contents("json/mod2.json");
              }elseif($final_module=="Module3"){
                $result = file_get_contents("json/mod3.json");
              }elseif($final_module=="Module4"){
                $result = file_get_contents("json/mod4.json");
              }elseif($final_module=="Module5"){
                $result = file_get_contents("json/mod5.json");
              }elseif($final_module=="Module6"){
                $result = file_get_contents("json/mod6.json");
              }elseif($final_module=="Module7"){
                $result = file_get_contents("json/mod7.json");
              }elseif($final_module=="Module8"){
                $result = file_get_contents("json/mod8.json");
              }elseif($final_module=="Module9"){
                $result = file_get_contents("json/mod9.json");
              }elseif($final_module=="Module10"){
                $result = file_get_contents("json/mod10.json");
              }elseif($final_module=="Module11"){
                $result = file_get_contents("json/mod11.json");
              }elseif($final_module=="Module12"){
                $result = file_get_contents("json/mod12.json");
              }elseif($final_module=="Module13"){
                $result = file_get_contents("json/mod13.json");
              }elseif($final_module=="Module14"){
                $result = file_get_contents("json/mod14.json");
              }elseif($final_module=="Module15"){
                $result = file_get_contents("json/mod15.json");
              }elseif($final_module=="Module16"){
                $result = file_get_contents("json/mod16.json");
              }else{
                $result = file_get_contents("json/mod1.json"); 
              }
              
              $json_object = json_decode($result);
        ?>
<!-- <meta http-equiv="refresh" content="60"> -->
<body>
  <!-- <MARQUEE align="center" direction="left" height="20" scrollamount="6" width="100%" behavior="alternate" style="background-color: #1d388c; color: white; margin-top:-10%;">Please backup data before <?php echo $backup_date; ?> !!!</MARQUEE> -->
  <form name="form1" method="post" action="module.php">
    <div class="container table-responsive">
      <table>
        <tr>
          <td><label>Module</label></td>
          <td><label>:</label></td>
          <td>&nbsp;</td>
          <td>
            <select class="form-control" name="module" id="module">
            <?php 
                echo "<option value=".$module.">Module ".$module."</option>";
                for($i=1; $i<3; $i++)
                {
                  echo "<option value=".$i.">Module ".$i."</option>";
                }
            ?> 
            </select>
          </td>
          <td></td>
          <td><input name="search" value="Search" type="Submit" id="button" class="btn btn-primary" formaction="module.php"></td>
        </tr>
        <tr>
          <td>&nbsp;</td>
        </tr>
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
              <input name="export" value="Export" type="Submit" id="export" class="btn btn-primary" formaction="module_excel.php">
            </div>
          </td>
        </tr>
      </table>
      <br>
    </div>
    <!-- <div class="container table-responsive">
      <?php echo '<center><h4>Data '.$final_module.'</h4></center>'; ?>
      <div class="col-md-3" style="background-color: #f9f9f9; border-radius: 15px; margin-right: 5%; margin-bottom: 2%;">
        <fieldset>
          <legend>General</legend>
          <table>
            <tr>
              <td width="110px;"><label>Voltage</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Voltage; ?> readonly></td>
              <td><label>Volt</label></td>
            </tr>
            <tr>
              <td><label>Current</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Current; ?> readonly></td>
              <td><label>Ampere</label></td>
            </tr>
            <tr>
              <td><label>DC</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->DC; ?> readonly></td>
              <td><label>%</label></td>
            </tr>
            <tr>
              <td><label>FCC</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->FCC; ?> readonly></td>
              <td><label>%</label></td>
            </tr>
            <tr>
              <td><label>RC</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->RC; ?> readonly></td>
              <td><label>%</label></td>
            </tr>
            <tr>
              <td><label>SOC</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->SOC; ?> readonly></td>
              <td><label>%</label></td>
            </tr>
            <tr>
              <td><label>SOH</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->SOH; ?> readonly></td>
              <td><label>%</label></td>
            </tr>  
            <tr>
              <td><label>Cycle Count</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Cycle_Count; ?> readonly></td>
              <td><label>Cycle</label></td>
            </tr>
          </table>
          
        </fieldset>
      </div>
      <div class="col-md-3" style="background-color: #f9f9f9; border-radius: 15px; margin-right: 5%; margin-bottom: 2%;">
        <fieldset>
          <legend>Temperatures</legend>
          <table>
            <tr>
              <td width="110px;"><label>Max Cell Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Max_Cell_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>Min Cell Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Min_Cell_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>Max FET Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Max_FET_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>Max PCB Parts Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Max_PCB_Parts_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>Cell Temp1</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Cell_Temp1; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>

            <tr>
              <td><label>Cell Temp2</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Cell_Temp2; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>Cell Temp3</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->Cell_Temp3; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>FET Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->FET_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
            <tr>
              <td><label>PCB Parts Temp</label></td>
              <td><input type="text" class="form-control" style="width: 90%; height: 80%; margin-bottom: 3px;" value=<?php echo $json_object->PCB_Parts_Temp; ?> readonly></td>
              <td><label>Celcius</label></td>
            </tr>
          </table>
          
        </fieldset>
      </div>
      <div class="col-md-4" style="background-color: #f9f9f9; border-radius: 15px;">
        <fieldset>
          <legend>Profile</legend>
          <table>
            <tr>
              <td width="110px;"><label>Manufacture_Name</label></td>
              <td><textarea class="form-control" rows="1" cols="50" style="margin-bottom: 3px;" readonly=""><?php echo $json_object->Manufacture_Name; ?></textarea></td>
            </tr>
            <tr>
              <td width="110px;"><label>Device_Name</label></td>
              <td><textarea class="form-control" rows="1" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->Device_Name; ?></textarea></td>
            </tr>
            <tr>
              <td width="110px;"><label>Serial_Number</label></td>
              <td><textarea class="form-control" rows="1" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->Serial_Number; ?></textarea></td>
            </tr>
            <tr>
              <td width="110px;"><label>Barcode</label></td>
              <td><textarea class="form-control" rows="1" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->BarCode; ?></textarea></td>
            </tr>
          </table>
          
        </fieldset>
      </div>

      <div class="col-md-12" style="background-color: #f9f9f9; border-radius: 15px;">
        <fieldset>
          <legend>Notification</legend>
          <table>
            <tr>
              <td width="110px;"><label>Status</label></td>
              <td><textarea class="form-control" rows="6" cols="50" style="margin-bottom: 3px;" readonly=""><?php echo $json_object->Status; ?></textarea></td>
              <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
              <td width="110px;"><label>Alarm</label></td>
              <td><textarea class="form-control" rows="6" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->Alarm; ?></textarea></td>
            </tr>
            <tr>
              <td width="110px;"><label>Warning</label></td>
              <td><textarea class="form-control" rows="6" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->Warning; ?></textarea></td>
              <td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
              <td width="110px;"><label>Error</label></td>
              <td><textarea class="form-control" rows="6" cols="50" readonly="" style="margin-bottom: 3px;"><?php echo $json_object->Error; ?></textarea></td>
            </tr>
          </table>
          
        </fieldset>
      </div>

      <div class="col-md-12" style="background-color: #f9f9f9; border-radius: 15px; margin-top: 1%; margin-bottom: 2%; font-size: 12px;">
        <fieldset>
          <legend>Cell Voltage (Volt)</legend>
          <table>
            <thead>
              <tr style="font-weight: bold;">
                <td style="width: 6%;">Min</td>
                <td style="width: 6%;">Max</td>
                <td style="width: 6%;">1</td>
                <td style="width: 6%;">2</td>  
                <td style="width: 6%;">3</td>
                <td style="width: 6%;">4</td>
                <td style="width: 6%;">5</td>
                <td style="width: 6%;">6</td>  
                <td style="width: 6%;">7</td>
                <td style="width: 6%;">8</td>
                <td style="width: 6%;">9</td>
                <td style="width: 6%;">10</td>
                <td style="width: 6%;">11</td>
                <td style="width: 6%;">12</td>
                <td style="width: 6%;">13</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->Min_Cell_Voltage; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->Max_Cell_Voltage; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C1V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C2V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C3V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C4V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C5V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C6V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C7V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C8V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C9V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C10V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C11V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C12V; ?> readonly></td>
                <td><input type="text" class="form-control" style="width: 75%; height: 80%; font-size: 12px;" name="" value=<?php echo $json_object->C13V; ?> readonly></td>
              </tr>
            </tbody>
          </table>
          
        </fieldset>
      </div>
    </div> -->
  </form>
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