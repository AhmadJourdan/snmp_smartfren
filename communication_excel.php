<?php

include ('config/connect.php');
include "PHPExcel-1.8/Classes/PHPExcel.php";
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
date_default_timezone_set("Asia/Jakarta");
// session_start();
// if (!isset($_SESSION['ID'])){
// // Jika Tidak Arahkan Kembali ke Halaman Login
//   header("location: login.php");
// } 

$excelku = new PHPExcel();

// Set lebar kolom
$excelku->getActiveSheet()->getColumnDimension('A')->setWidth(20);
$excelku->getActiveSheet()->getColumnDimension('B')->setWidth(15);
$excelku->getActiveSheet()->getColumnDimension('C')->setWidth(17);
$excelku->getActiveSheet()->getColumnDimension('D')->setWidth(17);
$excelku->getActiveSheet()->getColumnDimension('E')->setWidth(17);
$excelku->getActiveSheet()->getColumnDimension('F')->setWidth(17);
$excelku->getActiveSheet()->getColumnDimension('G')->setWidth(17);
$excelku->getActiveSheet()->getColumnDimension('H')->setWidth(20);
$excelku->getActiveSheet()->getColumnDimension('I')->setWidth(17);
// Buat Kolom judul tabel
$SI = $excelku->setActiveSheetIndex(0);
$SI->setCellValue('A1', 'Timestamp'); 
$SI->setCellValue('B1', 'Active Code'); 
$SI->setCellValue('C1', 'Gateway'); 
$SI->setCellValue('D1', 'SNMP Community'); 
$SI->setCellValue('E1', 'Sys OID'); 
$SI->setCellValue('F1', 'IP Address'); 
$SI->setCellValue('G1', 'SNMP Version'); 
$SI->setCellValue('H1', 'Netmask'); 
$SI->setCellValue('I1', 'SNMP Port'); 

// Mengambil data dari tabel
$sql = mysqli_query($con, "SELECT * FROM BackupEvent WHERE BackupEvent.`Begin` > '".$_POST["dari"]."' AND BackupEvent.`Begin` < '".$_POST["sampai"]."' ") or die(mysqli_error());
$baris  = 2;

while($data=mysqli_fetch_array($sql)){
  $SI->setCellValue("A".$baris,$data['Timestamp']); 
  $SI->setCellValue("B".$baris,$data['Active_Code']); 
  $SI->setCellValue("C".$baris,$data['gateway']); 
  $SI->setCellValue("D".$baris,$data['snmpCommunity']); 
  $SI->setCellValue("E".$baris,$data['sysOID']); 
  $SI->setCellValue("F".$baris,$data['ipAddress']); 
  $SI->setCellValue("G".$baris,$data['snmpVersion']);
  $SI->setCellValue("H".$baris,$data['netMask']);  
  $SI->setCellValue("I".$baris,$data['snmpPort']);  

  $baris++; //looping untuk barisnya
}

//Memberi nama sheet
$excelku->getActiveSheet()->setTitle('Communication');
$excelku->getActiveSheet()->getProtection()->setSheet(true);
$excelku->getActiveSheet()->getProtection()->setSort(true);
$excelku->getActiveSheet()->getProtection()->setInsertRows(true);
$excelku->getActiveSheet()->getProtection()->setFormatCells(true);
$excelku->setActiveSheetIndex(0);

// untuk excel 2007 atau yang berekstensi .xlsx
header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
header('Content-Disposition: attachment;filename=Communication'.date('dmY').'.xlsx');
header('Cache-Control: max-age=0');
 
$objWriter = PHPExcel_IOFactory::createWriter($excelku, 'Excel2007');
$objWriter->save('php://output');
exit;

?>