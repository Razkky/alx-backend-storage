-- List all band with Glam Rock as mainstyle ranked by longivity

SELECT band_name, 
       (2022 - formed) - (CASE WHEN split = 0 THEN 2022 ELSE split END) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
