-- creates a stored procedure that adds a new correction for a student.

DELIMITER //
CREATE PROCEDURE AddBonus (user_id INT, project_name VARCHAR(255), score FLOAT)
BEGIN
  IF NOT EXISTS (SELECT 1 FROM projects WHERE name = project_name) THEN
    INSERT INTO projects (name) VALUES (project_name);
  END IF;

  INSERT INTO corrections(user_id, project_id, score)
	SELECT user_id, id, score FROM projects WHERE projects.name = project_name;
END;//
