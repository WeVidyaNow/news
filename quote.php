<?php
// Only needed because the quote application doesn't put out content served with SSL
$json = file_get_contents("http://wevidyanow.com:7000/quote");
header("Content-Type: application/json");
echo $json;
?>
