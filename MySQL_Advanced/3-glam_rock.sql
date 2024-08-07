-- Lists all bands with Glam rock as their main style, ranked by longevity
SELECT name AS band_name,
IF(split IS NULL, YEAR(CURDATE()) - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;