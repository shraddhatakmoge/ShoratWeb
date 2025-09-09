<?php
header("Content-Type: application/json");
error_reporting(0);
ini_set('display_errors', 0);

require_once 'vendor/autoload.php'; // PHPWord required

use PhpOffice\PhpWord\PhpWord;
use PhpOffice\PhpWord\IOFactory;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $first_name = $_POST['first_name'] ?? '';
    $last_name  = $_POST['last_name'] ?? '';
    $email      = $_POST['email'] ?? '';
    $phone      = $_POST['phone'] ?? '';
    $comments   = $_POST['comments'] ?? '';
    $dateTime   = date("Y-m-d H:i:s");

    // Folder for storage
    $folder = "submissions/";
    if (!is_dir($folder)) {
        mkdir($folder, 0777, true);
    }

    $fileName = $folder . "contact_data.docx";

    // ✅ Check if file exists
    if (file_exists($fileName)) {
        // Load existing file
        $phpWord = IOFactory::load($fileName);
        $section = $phpWord->getSections()[0];
        $tables  = $section->getElements();

        // Find first table in the section
        $table = null;
        foreach ($tables as $element) {
            if ($element instanceof \PhpOffice\PhpWord\Element\Table) {
                $table = $element;
                break;
            }
        }
    } else {
        // Create new Word document
        $phpWord = new PhpWord();
        $section = $phpWord->addSection();

        // Add title
        $section->addTitle("Contact Form Submissions", 1);

        // Create new table with header row
        $table = $section->addTable([
            'borderSize' => 6,
            'borderColor' => '999999',
            'cellMargin' => 80
        ]);

        $table->addRow();
        $table->addCell(2000)->addText("First Name");
        $table->addCell(2000)->addText("Last Name");
        $table->addCell(3000)->addText("Email");
        $table->addCell(2000)->addText("Phone");
        $table->addCell(5000)->addText("Comments");
        $table->addCell(3000)->addText("Date & Time");
    }

    // ✅ Add new row for submission
    if ($table) {
        $table->addRow();
        $table->addCell(2000)->addText($first_name);
        $table->addCell(2000)->addText($last_name);
        $table->addCell(3000)->addText($email);
        $table->addCell(2000)->addText($phone);
        $table->addCell(5000)->addText($comments);
        $table->addCell(3000)->addText($dateTime);
    }

    // Save back to file
    $writer = IOFactory::createWriter($phpWord, 'Word2007');
    $writer->save($fileName);

    echo json_encode(["status" => "success", "message" => "Data added to Word table", "file" => $fileName]);
    exit();
}

echo json_encode(["status" => "error", "message" => "Invalid request"]);
exit();
?>
