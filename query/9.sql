SELECT @productId := id FROM Product WHERE name="Gazole";
SET @date ='2019-01-13';
SET @stationId ='61500002' ;

SELECT AVG(value) as prix FROM Price
WHERE Price.stationId IN ( SELECT id FROM Station WHERE LEFT(Station.postalcode ,2) = @department)
AND Price.productId = @productId
AND 
    AND Price.productId = @productId
    AND Price.start <= @date AND Price.end > @date
    AND NOT EXISTS (SELECT * FROM Shortage
                    WHERE Shortage.stationId = Price.stationId
                    AND Shortage.productId = @productId
                    AND Shortage.start <= @date
                    AND Shortage.end > @date

)

AND NOT EXISTS (SELECT * FROM Closing
                WHERE Closing.stationId = Price.stationId
                AND Closing.start <= @date
                AND Closing.end > @date
);
