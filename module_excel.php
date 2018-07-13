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

// Set lebar kolom
// $excelku->getActiveSheet()->getColumnDimension('A')->setWidth(20);
// $excelku->getActiveSheet()->getColumnDimension('B')->setWidth(15);
// $excelku->getActiveSheet()->getColumnDimension('C')->setWidth(17);
// $excelku->getActiveSheet()->getColumnDimension('D')->setWidth(17);
// $excelku->getActiveSheet()->getColumnDimension('E')->setWidth(17);
// $excelku->getActiveSheet()->getColumnDimension('F')->setWidth(17);
// $excelku->getActiveSheet()->getColumnDimension('G')->setWidth(17);
// $excelku->getActiveSheet()->getColumnDimension('H')->setWidth(20);

// Buat Kolom judul tabel
$SI = $excelku->setActiveSheetIndex(0);
$SI->setCellValue('A1', 'Timestamp'); 
$SI->setCellValue('B1', 'DC'); 
$SI->setCellValue('C1', 'FCC'); 
$SI->setCellValue('D1', 'RC'); 
$SI->setCellValue('E1', 'SOC'); 
$SI->setCellValue('F1', 'SOH'); 
$SI->setCellValue('G1', 'Cycle_Count'); 
$SI->setCellValue('H1', 'Voltage'); 

$SI->setCellValue('I1', 'Max Cell Voltage'); 
$SI->setCellValue('J1', 'Min Cell Voltage'); 
$SI->setCellValue('K1', 'Current'); 
$SI->setCellValue('L1', 'Max Cell Temp'); 
$SI->setCellValue('M1', 'Min Cell Temp'); 
$SI->setCellValue('N1', 'Max FET Temp'); 
$SI->setCellValue('O1', 'Max PCB Parts Temp'); 
$SI->setCellValue('P1', 'Cell Temp1');

$SI->setCellValue('Q1', 'Cell Temp2'); 
$SI->setCellValue('R1', 'Cell Temp3'); 
$SI->setCellValue('S1', 'FET Temp'); 
$SI->setCellValue('T1', 'PCBParts Temp'); 
$SI->setCellValue('U1', 'C1V'); 
$SI->setCellValue('V1', 'C2V'); 
$SI->setCellValue('W1', 'C3V'); 
$SI->setCellValue('X1', 'C4V');

$SI->setCellValue('Y1', 'C5V'); 
$SI->setCellValue('Z1', 'C6V'); 
$SI->setCellValue('AA1', 'C7V'); 
$SI->setCellValue('AB1', 'C8V'); 
$SI->setCellValue('AC1', 'C9V'); 
$SI->setCellValue('AD1', 'C10V'); 
$SI->setCellValue('AE1', 'C11V'); 
$SI->setCellValue('AF1', 'C12V');
$SI->setCellValue('AG1', 'C13V'); 
$SI->setCellValue('AH1', 'Manufacture Name');

$SI->setCellValue('AI1', 'Device Name'); 
$SI->setCellValue('AJ1', 'Serial Number'); 
$SI->setCellValue('AK1', 'BarCode'); 
$SI->setCellValue('AL1', 'Status'); 
$SI->setCellValue('AM1', 'Warning'); 
$SI->setCellValue('AN1', 'Alarm'); 
$SI->setCellValue('AO1', 'Error'); 

// Mengambil data dari tabel
$module = $_POST["module"];
$dari = $_POST["dari"];
$sampai = $_POST["sampai"];
$final_module = "Module".$module."";
$sql = mysqli_query($con, "SELECT * FROM $final_module where(Timestamp between '$dari' and '$sampai') ") or die(mysqli_error());
$baris  = 2;

while($data=mysqli_fetch_array($sql)){
  $SI->setCellValue("A".$baris,$data['Timestamp']); 
  $SI->setCellValue("B".$baris,$data['DC']); 
  $SI->setCellValue("C".$baris,$data['FCC']); 
  $SI->setCellValue("D".$baris,$data['RC']); 
  $SI->setCellValue("E".$baris,$data['SOC']); 
  $SI->setCellValue("F".$baris,$data['SOH']); 
  $SI->setCellValue("G".$baris,$data['Cycle_Count']);
  $SI->setCellValue("H".$baris,$data['Voltage']);   

  $SI->setCellValue("I".$baris,$data['Max_Cell_Voltage']); 
  $SI->setCellValue("J".$baris,$data['Min_Cell_Voltage']); 
  $SI->setCellValue("K".$baris,$data['Current']); 
  $SI->setCellValue("L".$baris,$data['Max_Cell_Temp']); 
  $SI->setCellValue("M".$baris,$data['Min_Cell_Temp']); 
  $SI->setCellValue("N".$baris,$data['Max_FET_Temp']); 
  $SI->setCellValue("O".$baris,$data['Max_PCB_Parts_Temp']);
  $SI->setCellValue("P".$baris,$data['Cell_Temp1']);  

  $SI->setCellValue("Q".$baris,$data['Cell_Temp2']); 
  $SI->setCellValue("R".$baris,$data['Cell_Temp3']); 
  $SI->setCellValue("S".$baris,$data['FET_Temp']); 
  $SI->setCellValue("T".$baris,$data['PCB_Parts_Temp']); 
  $SI->setCellValue("U".$baris,$data['C1V']); 
  $SI->setCellValue("V".$baris,$data['C2V']); 
  $SI->setCellValue("W".$baris,$data['C3V']);
  $SI->setCellValue("X".$baris,$data['C4V']); 

  $SI->setCellValue("Y".$baris,$data['C5V']); 
  $SI->setCellValue("Z".$baris,$data['C6V']); 
  $SI->setCellValue("AA".$baris,$data['C7V']); 
  $SI->setCellValue("AB".$baris,$data['C8V']); 
  $SI->setCellValue("AC".$baris,$data['C9V']); 
  $SI->setCellValue("AD".$baris,$data['C10V']);
  $SI->setCellValue("AE".$baris,$data['C11V']);  
  $SI->setCellValue("AF".$baris,$data['C12V']); 
  $SI->setCellValue("AG".$baris,$data['C13V']);
  $SI->setCellValue("AH".$baris,$data['Manufacture_Name']);

  $SI->setCellValue("AI".$baris,$data['Device_Name']); 
  $SI->setCellValue("AJ".$baris,$data['Serial_Number']); 
  $SI->setCellValue("AK".$baris,$data['BarCode']); 
  $SI->setCellValue("AL".$baris,$data['Status']);
  $SI->setCellValue("AM".$baris,$data['Warning']);  
  $SI->setCellValue("AN".$baris,$data['Alarm']); 
  $SI->setCellValue("AO".$baris,$data['Error']);
  
  $baris++; //looping untuk barisnya
}

//Memberi nama sheet
$excelku->getActiveSheet()->setTitle('Module'.$module.'');
$excelku->getActiveSheet()->getProtection()->setSheet(true);
$excelku->getActiveSheet()->getProtection()->setSort(true);
$excelku->getActiveSheet()->getProtection()->setInsertRows(true);
$excelku->getActiveSheet()->getProtection()->setFormatCells(true);
$excelku->setActiveSheetIndex(0);

// untuk excel 2007 atau yang berekstensi .xlsx
header('Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
header('Content-Disposition: attachment;filename=Module'.$module.'-'.date('dmY').'.xlsx');
header('Cache-Control: max-age=0');
 
$objWriter = PHPExcel_IOFactory::createWriter($excelku, 'Excel2007');
$objWriter->save('php://output');
exit;

?>