SELECT address , city FROM Station 
INNER JOIN StationService ON Station.id = stationId
INNER JOIN Service ON Service.id = serviceId
WHERE Service.name='Station de gonflage';
--
-- WHERE EXISTS( Select * fro service station  where station.id = stationid and serviceId = (select id from service where service.name='station de ...)) ;


SELECT address , city FROM Station 
INNER JOIN StationService ON Station.id = stationId

WHERE serviceId=(SELECT id FROM Service WHERE Service.name='Station de gonflage' ) ;