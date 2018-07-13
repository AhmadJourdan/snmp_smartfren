<?php

include ('config/connect.php');
include "PHPExcel-1.8/Classes/PHPExcel.php";
error_reporting(E_ALL ^ (E_NOTICE | E_WARNING));
date_default_timezone_set("Asia/Jakarta");
session_start();
if (!isset($_SESSION['ID'])){
// Jika Tidak Arahkan Kembali ke Halaman Login
  header("location: login.php");
} 

$excelku = new PHPExcel();

// // Set lebar kolom
$excelku->getActiveSheet()->getColumnDimension('A')->setWidth(20);
$excelku->getActiveSheet()->getColumnDimension('B')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('C')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('D')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('E')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('F')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('G')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('H')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('I')->setWidth(10);
$excelku->getActiveSheet()->getColumnDimension('J')->setWidth(30);
$excelku->getActiveSheet()->getColumnDimension('K')->setWidth(40);
$excelku->getActiveSheet()->getColumnDimension('L')->setWidth(30);
$excelku->getActiveSheet()->getColumnDimension('M')->setWidth(20);
$excelku->getActiveSheet()->getColumnDimension('N')->setWidth(30);
// Buat Kolom judul tabel
$SI = $excelku->setActiveSheetIndex(0);
$SI->setCellValue('A1', 'Timestamp'); 
$SI->setCellValue('B1', 'CV'); 
$SI->setCellValue('C1', 'CCL'); 
$SI->setCellValue('D1', 'DCL'); 
$SI->setCellValue('E1', 'EDV'); 
$SI->setCellValue('F1', 'Bus Volt'); 
$SI->setCellValue('G1', 'Bus Curr'); 
$SI->setCellValue('H1', 'Detected Mod');
$SI->setCellValue('I1', 'Capacity'); 
$SI->setCellValue('J1', 'Backup Time'); 
$SI->setCellValue('K1', 'Status'); 
$SI->setCellValue('L1', 'Warning'); 
$SI->setCellValue('M1', 'Alarm'); 
$SI->setCellValue('N1', 'Error'); 

// Mengambil data dari tabel
$sql = mysqli_query($con, "SELECT * FROM `GeneralData` where(Timestamp between '".$_POST["dari"]."' and '".$_POST["sampai"]."') ") or die(mysqli_error());;
$baris  = 2;

while($data=mysqli_fetch_array($sql)){
  $SI->setCellValue("A".$baris,$data['Timestamp']); 
  $SI->setCellValue("B".$baris,$data['CV']); 
  $SI->setCellValue("C".$baris,$data['CCL']); 
  $SI->setCellValue("D".$baris,$data['DCL']); 
  $SI->setCellValue("E".$baris,$data['EDV']); 
  $SI->setCellValue("F".$baris,$data['Bus_Volt']); 
  $SI->setCellValue("G".$baris,$data['Bus_Curr']);
  $SI->setCellValue("H".$baris,$data['Detected_Mod']); 
  $SI->setCellValue("I".$baris,$data['Capacity']);
  $SI->setCellValue("J".$baris,$data['BackupTime']);
  $SI->setCellValue("K".$baris,$data['Status']);
  $SI->setCellValue("L".$baris,$data['Warning']);
  $SI->setCellValue("M".$baris,$data['Alarm']);
  $SI->setCellValue("N".$baris,$data['Error']);    

  $baris++; //looping untuk barisnya
}

//Memberi nama sheet
$excelku->getActiveSheet()->setTitle('General Data');
$excelku->getActiveSheet()->getProtection()->setSheet(true);
$excelku->getActiveSheet()->getProtection()->setSort(true);
$excelku->getActiveSheet()->getProtection()->setInsertRows(true);
$excelku->getActiveSheet()->getProtection()->setFormatCells(true);
$excelku->setActiveSheetIndex(0);

// untuk excel 2007 atau yang berekstensi .xlsx
header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
header('Content-Disposition: attachment;filename=Overview'.date('dmY').'.xlsx');
header('Cache-Control: max-age=0');
 
$objWriter = PHPExcel_IOFactory::createWriter($excelku, 'Excel2007');
$objWriter->save('php://output');
exit;

?>