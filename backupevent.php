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
              <input name="export" value="Export" type="Submit" id="export" class="btn btn-primary" formaction="backupevent_excel.php">
            </div>
          </td>
        </tr>
      </table>
      <br>
    </div>
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