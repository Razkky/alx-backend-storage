-- Rank country origin of bands
-- Order by number of unique fans
-- Column names are origin and nb_fans

SELECT origin AS origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
