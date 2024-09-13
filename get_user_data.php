<?php
$telegram_id = $_GET['telegram_id'];

$mysqli = new mysqli("localhost", "username", "n@1234mine@4321", "token_system");

if ($mysqli->connect_error) {
    die("Connection failed: " . $mysqli->connect_error);
}

// Получаем данные пользователя
$user_result = $mysqli->query("SELECT * FROM users WHERE telegram_id = '$telegram_id'");
$user_data = $user_result->fetch_assoc();

// Получаем оставшиеся токены
$token_result = $mysqli->query("SELECT total_tokens FROM token_supply WHERE id = 1");
$token_data = $token_result->fetch_assoc();

// Отправляем данные в формате JSON
echo json_encode([
    "balance" => $user_data['tokens'],
    "referrals_count" => $user_data['referrals_count'],
    "referral_link" => $user_data['referral_link'],
    "remaining_tokens" => $token_data['total_tokens']
]);

$mysqli->close();
?>
