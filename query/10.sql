SELECT @productId := id FROM Product WHERE name="Gazole";
SET @date = '2019-01-13'

SELECT LEFT(postalcode,2) as departement , AVG(value) as average FROM Price

INNER JOIN Station ON Price.stationId = stationId
WHERE productId = @productId
    AND Price.start <= @date AND Price.end > @date
    AND NOT EXISTS (SELECT * FROM Shortage
                    WHERE Shortage.stationId = Station.id
                    AND Shortage.productId = @productId
                    AND Shortage.start <= @date
                    AND (Shortage.end IS NULL OR Shortage.end >= @date)

                    )
    AND NOT EXISTS (SELECT * FROM Closing
                    WHERE Closing.stationId = Station.id
                    AND Closing.productId = @productId
                    AND Closing.start <= @date
                    AND (Closing.end IS NULL OR Shortage.end >= @date)

                    )
GROUP BY departement 
ORDER BY departement;




WITH 
    AvgPrice AS
    (SELECT stationId , AVG(value) as value FROM Price WHERE productId = @productId GROUP BY stationId) 
    SELECT stationId ,address, city , value FROM AvgPrice
    INNER JOIN Station ON Station.id = stationId
    WHERE value = (SELECT min(value)) FROM AvgPrice;


                    