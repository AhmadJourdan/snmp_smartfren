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
  <form name="form1" method="post" action="">
    <div class="wrapper table-responsive">
      <table>
        <tr>
          <td><label>Filter by Devices</label></td>
          <td><label>:</label></td>
          <td>&nbsp;</td>
          <td>
            <select class="form-control" name="device" id="device">
              <option value="pilih">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- PILIH DEVICE ---</option>
              <?php
                $query=pg_query($conn, "SELECT id, name from device");
                while ($data = pg_fetch_array($query))
                {
                   echo '<option value="'.$data['id'].'">'.$data['name'].'</option>';       
                }
              ?>
            </select>
          </td>
        </tr>
        <tr>
          <td>&nbsp;</td>
        </tr>
        <!-- <tr>
          <td><label>Filter by Date</label></td>
          <td><label>:</label></td>
          <td>&nbsp;</td>
          <td>
            <div class="form-group">
              <div class="input-group date form_date" data-date="" data-date-format="mm dd yyyy" data-link-field="dari" data-link-format="dd-mm-yyyy hh:mm:ss">
                    <input class="form-control" id="dari" name="dari" size="16" type="text">
                          <span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>
                <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
                      </div>
            </div>
          </td>
          <td>&nbsp;-&nbsp;</td>
          <td>
            <div class="form-group">
              <div class="input-group date form_date" data-date="" data-date-format="mm dd yyyy" data-link-field="sampai" data-link-format="dd-mm-yyyy hh:mm:ss">
                      <input class="form-control" id="sampai" name="sampai" size="16" type="text">
                          <span class="input-group-addon"><span class="glyphicon glyphicon-remove"></span></span>
                <span class="input-group-addon"><span class="glyphicon glyphicon-calendar"></span></span>
                      </div>
            </div>
          </td>
        </tr> -->
        <tr>
          <td></td>
          <td></td>
          <td></td>
          <td><input name="search" value="Search" type="Submit" id="button" class="btn btn-primary"></td>
        </tr>
      </table>
      <br>
    </div>
    <div class="wrapper table-responsive">
      <table id="table" class="table table-hover">
            <thead>
              <tr class="info">
                <th width="8%">No</th>
                <th>Entity ID</th>
                <th>Entity Type</th>
                <th>Key</th>
                <th>Timestamp</th>
                <th>bool_value</th>
                <th>str_value</th>
                <th>long_value_bigint</th>
                <th>dbl_value</th>
              </tr>
            </thead>
            <tbody>
              <?php
              $dari = $_POST["dari"];
              $ts_dari = strtotime($dari)*1000;
              $sampai = $_POST["sampai"];
              $ts_sampai = strtotime($sampai)*1000;

              if(isset($_POST['search'])){
                $result = pg_query($conn, "SELECT * FROM ts_kv where entity_id='".$_POST['device']."' and (ts between $ts_dari and $ts_sampai)");
              }else{
                $result = pg_query($conn, "SELECT * FROM ts_kv limit 200");
              }
                $i=0;
                while($data=pg_fetch_array($result)){
                  $i++;
                  $entity_id = $data['entity_id'];
                  $entity_type = $data['entity_type'];
                  $key = $data['key'];
                  $ts = $data['ts'];
                  $bool_v = $data['bool_v'];
                  $str_v = $data['str_v'];
                  $long_v = $data['long_v'];
                  $dbl_v = $data['dbl_v'];
                  echo '<tr class="">';
                      echo '<td>'.$i.'</td>';
                      echo '<td>'.$entity_id.'</td>';
                      echo '<td>'.$entity_type.'</td>';
                      echo '<td>'.$key.'</td>';
                      echo '<td>'.date('d-m-Y H:i:s', $ts/1000).'</td>';
                      echo '<td>'.$bool_v.'</td>';
                      echo '<td>'.$str_v.'</td>';
                      echo '<td>'.$long_v.'</td>';
                      echo '<td>'.$dbl_v.'</td>';
                  echo '</tr>';     
                }
              ?>
            </tbody>
          </table>
    </div>
  </form>
</body>
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