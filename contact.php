<?php
header("Content-Type: application/json");
error_reporting(0);
ini_set('display_errors', 0);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $first_name = $_POST['first_name'] ?? '';
    $last_name = $_POST['last_name'] ?? '';
    $email = $_POST['email'] ?? '';
    $phone = $_POST['phone'] ?? '';
    $comments = $_POST['comments'] ?? '';
    $dateTime = date("Y-m-d H:i:s");

    $fileName = "contact_data.csv";
    $fileExists = file_exists($fileName);

    if ($file = fopen($fileName, "a")) {
        if (!$fileExists) {
            fputcsv($file, ['First Name', 'Last Name', 'Email', 'Phone', 'Comments', 'Date & Time']);
        }
        fputcsv($file, [$first_name, $last_name, $email, $phone, $comments, $dateTime]);
        fclose($file);

        echo json_encode(["status" => "success", "message" => "Data saved successfully"]);
        exit();
    } else {
        echo json_encode(["status" => "error", "message" => "Failed to save data"]);
        exit();
    }
}

echo json_encode(["status" => "error", "message" => "Invalid request"]);
exit();
?>
