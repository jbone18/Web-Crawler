<?php
    // PHP Data Objects(PDO) Sample Code:
    try {
        $conn = new PDO("sqlsrv:server = tcp:tappedin.database.windows.net,1433; Database = TappedIn", "cfrench23", "{your_password_here}");
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    }
    catch (PDOException $e) {
        print("Error connecting to SQL Server.");
        die(print_r($e));
    }

    /* 
    // SQL Server Extension Sample Code:
    $connectionInfo = array("UID" => "cfrench23@tappedin", "pwd" => "{your_password_here}", "Database" => "TappedIn", "LoginTimeout" => 30, "Encrypt" => 1, "TrustServerCertificate" => 0);
    $serverName = "tcp:tappedin.database.windows.net,1433";
    $conn = sqlsrv_connect($serverName, $connectionInfo);
    */


    $sql = "SELECT BeerID, BeerType, BeerName, Brewery, IBU, ABV, BeerDesc FROM dbo.Beer";
    $result = $conn-> query($sql);

    if ($result-> num_rows > 0) {
        while ($row = $result-> fetch_assoc()) {
            echo "<tr><td>". $row["BeerID"] . "</td><td>". $row["BeerType"] ."</td>";
            echo "<td>". $row["BeerName"] ."</td><td>". $row["Brewery"] ."</td>";
            echo "<td>". $row["IBU"] ."</td><td>". $row["ABV"] ."</td>";
            echo "<td>". $row["BeerDesc"] ."</td></tr>";
        }
        echo "</table>";
    }
    else {
        echo "0 Results";
    }

    $conn-> close();
?>