SET @luminy = POINT(43.2317362 ,5.432227);
SELECT id, address , city  , ST_Distance(gps, @luminy) *11000 as distance FROM Station
ORDER BY distance
LIMIT 1;