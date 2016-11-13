function dbQuery(tableName) {
  return $.ajax({
   url: 'https://sites.jmu.edu/exporttocsv.php',
   data: {'table':tableName},
   dataType: "text",
   type: 'GET',
   success: function(csvData) {},
   error: function(e, b, c) {}
  });
}