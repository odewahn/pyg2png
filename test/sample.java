List<String> foo = sqlContext
   .sql("SELECT ipAddress, COUNT(*) AS total FROM logs GROUP BY ipAddress HAVING total > 10")
   .map(bar -> bar.getString(0))
   .collect();
System.out.println(String.format("%s", foo));