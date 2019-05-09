<!DOCTYPE html>
<html>
    <head>
        <title>Tapped In</title>
        <link rel = "stylesheet" type = "text/css" href = "table.css">
        <link rel = "stylesheet" type = "text/css" href = "trial.css">
        
    </head>
    <body>
        <div class="wrapper">
                <header class="header">
                    <img src = Logo.png img-align = center>
                    <p>    
                        Welcome to Tapped In Spokane
                        <br>
                        <br>
                        <br>
                        Your One Stop Shop For All The Brewery News In Spokane
                    </p>
                    <a href="brew_user.html">Register With Us</a>
                </header>
            <article class = "main">
                <div class = divTable>
                    <div class = "drinkTable">
                        <div class = "divTableHeading">
                            <div class = "divTableRow"></div>
                            <!--<div class = "divTableHead">ID</div> -->
                            <div class = "divTableHead">Type</div>
                            <div class = "divTableHead">Name</div>
                            <div class = "divTableHead">Brewery</div>
                            <div class = "divTableHead">IBU's</div>
                            <div class = "divTableHead">ABV</div>
                            <div class = "divTableHead">Description</div>
                        </div>
                        <?php
                            
                            // PHP Data Objects(PDO) Sample Code:
                            try {
                                $conn = new PDO("sqlsrv:server = tcp:tappedin.database.windows.net,1433; Database = TappedIn", "cfrench23",
                                "Sh33pG1rl!0987");
                                $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                            }
                            catch (PDOException $e){
                                print("Error connecting to SQL Server.");
                                die(print_r($e));
                            }
                            
                            $sql = "SELECT DISTINCT BeerType, BeerName, Brewery, IBU, ABV, BeerDesc FROM Beer ORDER BY Brewery";
                            // echo "<p>".$sql."</p>";
                            $result = $conn->query($sql) or print_r($conn->errorInfo());

                            while ($row = $result->fetch(PDO::FETCH_ASSOC)) {
                                echo "<div class = 'divTableBody'><div class = 'divTableRow><div class = 'divTableCell'>". $row["BeerType"] ."</div>";
                                echo "<div class = 'divTableCell'>". $row["BeerName"] ."</div><div class = 'divTableCell'>". $row["Brewery"] ."</div>";
                                echo "<div class = 'divTableCell'>". $row["IBU"] ."</div><div class = 'divTableCell'>". $row["ABV"] ."</div>";
                                echo "<div class = 'divTableCell'>". $row["BeerDesc"] ."</div></div>";
                            }
                            echo "</div>";
                        
                            $conn-> close();
                        ?>
                    </div>
                </div>
            </div>
            </article>
            <aside class="aside aside-1">Aside 1</aside>
            <aside class="aside aside-2">Aside 2</aside>
            <footer class="footer">
                <p style="color:white; font-size: 100%;">
                    Footer
                </p>
            </footer>
        </div>
    </body>
</html>