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
$excelku->getActiveSheet()->getColumnDimension('B')->setWidth(20);
$excelku->getActiveSheet()->getColumnDimension('C')->setWidth(20);
// Buat Kolom judul tabel
$SI = $excelku->setActiveSheetIndex(0);
$SI->setCellValue('A1', 'Begin'); 
$SI->setCellValue('B1', 'End'); 
$SI->setCellValue('C1', 'Duration');

// Mengambil data dari tabel
$sql = mysqli_query($con, "SELECT * FROM `BackupEvent` where(Begin between '".$_POST["dari"]."' and '".$_POST["sampai"]."') ") or die(mysqli_error());
$baris  = 2;

while($data=mysqli_fetch_array($sql)){
  $SI->setCellValue("A".$baris,$data['Begin']); 
  $SI->setCellValue("B".$baris,$data['End']); 
  $SI->setCellValue("C".$baris,$data['Duration']); 
  
  $baris++; //looping untuk barisnya
}

//Memberi nama sheet
$excelku->getActiveSheet()->setTitle('Backup Event');
$excelku->getActiveSheet()->getProtection()->setSheet(true);
$excelku->getActiveSheet()->getProtection()->setSort(true);
$excelku->getActiveSheet()->getProtection()->setInsertRows(true);
$excelku->getActiveSheet()->getProtection()->setFormatCells(true);
$excelku->setActiveSheetIndex(0);

// untuk excel 2007 atau yang berekstensi .xlsx
header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
header('Content-Disposition: attachment;filename=BackupEvent'.date('dmY').'.xlsx');
header('Cache-Control: max-age=0');
 
$objWriter = PHPExcel_IOFactory::createWriter($excelku, 'Excel2007');
$objWriter->save('php://output');
exit;

?>