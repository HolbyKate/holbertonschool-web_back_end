-- Lists all bands with Glam rock as their main style, ranked by longevity
SELECT name AS band_name, IFNULL(YEAR(CURDATE()) - formed, 0) -
IFNULL(YEAR(CURDATE()) - split, 0) AS lifespan
FROM metal_bands
WHERE style = Glam rock
ORDER BY lidfespan DESC;