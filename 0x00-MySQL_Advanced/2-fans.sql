-- ranks county origins of bands by no of non-unique fana
-- Columns: id band_name fans formed origin split style

SELECT origin, SUM(fans) AS nb_fans FROM metal_bands
  GROUP BY origin
  ORDER BY nb_fans DESC;
