-- creates an index on the table names and the first letter of name.

ALTER TABLE names
ADD COLUMN firstLetterOfNames VARCHAR(5) GENERATED ALWAYS AS SUBSTR(name, 1, 1);

CREATE INDEX idx_name_first ON names (firstLetterOfNames);
