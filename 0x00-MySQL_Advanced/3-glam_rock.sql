-- Task 3: List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, (2022 - formed) as lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
