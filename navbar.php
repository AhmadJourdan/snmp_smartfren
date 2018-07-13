<!DOCTYPE html>
<html lang="en">
<head>
  <title>Panasonic DCB 105 ZK</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="assets/css/bootstrap.min.css">
  <script src="assets/js/jquery-1.11.0.min.js"></script>
  <script src="assets/js/bootstrap.min.js"></script>
  <script src="assets/js/jquery.dataTables.min.js"></script>
  <script src="assets/js/dataTables.bootstrap.js"></script>
  <script type="text/javascript">
    $(function() {
      $('#table').dataTable();
    });
  </script>
  <link href="assets/css/bootstrap-datetimepicker.min.css" rel="stylesheet" media="screen">
  <script type="text/javascript" src="assets/js/bootstrap-datetimepicker.js" charset="UTF-8"></script>
  <script type="text/javascript" src="assets/js/bootstrap-datetimepicker.id.js" charset="UTF-8"></script>
  <style type="text/css">
    .navbar-default .navbar-nav>li>a {
      color: white;
    }
    .navbar-default .navbar-nav>li>a:hover {
      color: #337ab7;
    }
    footer{
      color:white;
      margin-top: 4.1%;
      background-color: white;
    }
  </style>
</head>
<nav class="navbar navbar-default" style="background-color: #1d388c; color:white;">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#"></a>
    </div>
    <div id="navbar" class="navbar-collapse collapse">
      <ul class="nav navbar-nav">
        <li><a href="generaldata.php">Overview</a></li>
        <li><a href="communication.php">Communication</a></li>
        <li><a href="module.php">Module</a></li>
      </ul>
      <ul class="nav navbar-nav navbar-right">
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Settings <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="set_profile.php">Profile</a></li>
            <!-- <li><a href="set_network.php">Network</a></li> -->
            <li><a href="documentation/documentation.pdf" target="_blank">Documentation</a></li>
            <li><a href="logout.php">Logout</a></li>
          </ul>
        </li>
      </ul>
    </div><!--/.nav-collapse -->
  </div><!--/.container-fluid -->
</nav>
