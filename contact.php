<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: POST, OPTIONS");
header("Access-Control-Allow-Headers: Content-Type");
header("Content-Type: application/json");

require __DIR__ . '/vendor/autoload.php'; // PhpSpreadsheet

use PhpOffice\PhpSpreadsheet\Spreadsheet;
use PhpOffice\PhpSpreadsheet\Writer\Xlsx;
use PhpOffice\PhpSpreadsheet\IOFactory;

error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $first_name = $_POST['first_name'] ?? '';
    $last_name  = $_POST['last_name'] ?? '';
    $email      = $_POST['email'] ?? '';
    $phone      = $_POST['phone'] ?? '';
    $comments   = $_POST['comments'] ?? '';
    $dateTime   = date("Y-m-d H:i:s");

    $fileName = __DIR__ . "/contact_data.xlsx";

    try {
        if (file_exists($fileName)) {
            $spreadsheet = IOFactory::load($fileName);
            $sheet = $spreadsheet->getActiveSheet();
        } else {
            $spreadsheet = new Spreadsheet();
            $sheet = $spreadsheet->getActiveSheet();
            $sheet->setCellValue('A1', 'First Name')
                  ->setCellValue('B1', 'Last Name')
                  ->setCellValue('C1', 'Email')
                  ->setCellValue('D1', 'Phone')
                  ->setCellValue('E1', 'Comments')
                  ->setCellValue('F1', 'Date & Time');
        }

        $row = $sheet->getHighestRow() + 1;

        $sheet->setCellValue("A$row", $first_name)
              ->setCellValue("B$row", $last_name)
              ->setCellValue("C$row", $email)
              ->setCellValue("D$row", $phone)
              ->setCellValue("E$row", $comments)
              ->setCellValue("F$row", $dateTime);

        $writer = new Xlsx($spreadsheet);
        $writer->save($fileName);

        echo json_encode(["status" => "success", "message" => "Data saved successfully in Excel"]);
    } catch (Exception $e) {
        echo json_encode(["status" => "error", "message" => "Error: " . $e->getMessage()]);
    }
    exit();
}

echo json_encode(["status" => "error", "message" => "Invalid request"]);
exit();
