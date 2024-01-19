-- creates a stored procedure that computes and store the average score for a student.

DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (user_id INT)
  BEGIN
    SET @average := (SELECT AVG(corrections.score) FROM corrections
     WHERE corrections.user_id = user_id);
    UPDATE users SET average_score = @average WHERE id = user_id;
  END;//
