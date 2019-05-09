<?php

$UserName = filter_input(INPUT_POST, 'UserName');
$LastName = filter_input(INPUT_POST, 'LastName');
$FirstName = filter_input(INPUT_POST, 'FirstName');
$UserPass = filter_input(INPUT_POST, 'UserPass');
$Email = filter_input(INPUT_POST, 'Email');
$BirthDate = filter_input(INPUT_POST, 'BirthDate');
if (!empty($UserName)){
    if (!empty($UserPass)){
        $host = "tcp:tappedin.database.windows.net,1433";
        $dbusername = "cfrench23";
        $dbpassword = "Sh33pG1rl!0987";
        $dbname = "TappedIn";

        // Create connection
        $conn = new mysqli($host, $dbusername, $dbpassword, $dbname);

        if (mysqli_connect_error()){
            die('Connection Error ('.mysqli_connect_errno() .')'
            .mysqli_connect_error());
        }
        else {
            $sql = "INSERT INTO Users (UserName, LastName, FirstName, UserPass, Email, BirthDate)
            values ('$UserName', '$FirstName', '$LastName', '$UserPass', '$Email', '$BirthDate')";
            if ($conn->query($sql)){
                echo "New record inserted successfully";
            }
            else {
                echo "Error: ".$sql ."<br>". $conn->error;
            }
            $conn->close();
        }
    }
    else{
        echo "Password should not be empty";
        die();
    }
}
else {
    echo "Username should not be empty";
    die();
}

?>