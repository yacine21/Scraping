SET @productId := id FROM Product WHERE name="Gazole";
SET @date ='2019-01-13';
SET @stationId ='61500002' ;

SELECT value as prix FROM Price
WHERE Price.stationId =  @stationId
    AND Price.productId = @productId
    AND Price.start <= @date AND Price.end > @date
    AND NOT EXISTS (SELECT * FROM Shortage
                    WHERE Shortage.stationId = Price.stationId
                    AND Shortage.productId = @productId
                    AND Shortage.start <= @date
                    AND (Shortage.end IS NULL OR Shortage.end > @date)

)

AND NOT EXISTS (SELECT * FROM Closing
                WHERE Closing.stationId = Price.stationId
                AND Closing.start <= @date
                AND (Closing.end IS NULL OR Closing.end > @date)
);
