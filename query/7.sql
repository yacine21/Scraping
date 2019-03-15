SELECT LEFT(postalcode,2) as departement , COUNT(*) as stationCount FROM Station 
INNER JOIN StationService ON Station.id = stationId
INNER JOIN Service ON Service.id = serviceId
WHERE name='Station de gonflage'
GROUP BY departement
ORDER BY departement;
-- Station FROM Station GROUP BY departement;

