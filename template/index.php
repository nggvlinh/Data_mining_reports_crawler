
<?php
// connect to a database
$dbConn = pg_connect("host=<ec2-35-169-254-43.compute-1.amazonaws.com> port=<5432> dbname=<daerabpc01h014> user=<halepmhfxnkrni> password=<48e8d7e4ed72113de1dad744a6a3be7380d7602df430187473ed6decae2d2d6f>");
if (!$dbConn) {
    echo "An error occurred.\n";
    exit;
}
// Query data
$result = pg_query($dbConn, 'SELECT * FROM dmnganh');
if (!$result) {
    echo "An error occurred.\n";
    exit;
}
// Show value
while ($row = pg_fetch_assoc($result)) {
    var_dump($row);
}

?>