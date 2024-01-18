-- lists all bands with 'Glam rock' as their main style, ranked by longevity.
-- columns: id band_name fans formed origin split style


SELECT band_name, IF(formed IS NULL, 0, IF(split IS NULL, 2022 - formed, split - formed)) AS lifespan FROM metal_bands
  WHERE style LIKE '%Glam rock%'
  ORDER BY lifespan DESC;
