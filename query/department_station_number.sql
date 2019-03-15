-- SELECT  COUNT(*) as NombreDeStation FROM Station WHERE postalcode LIKE '';

SELECT DISTINCT LEFT(postalcode,2) as departement, COUNT(*) as Stations FROM Station GROUP BY departement;

