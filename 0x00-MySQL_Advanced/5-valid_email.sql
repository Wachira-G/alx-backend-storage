-- creates a trigger that resets the attribute 'valid_email' only when the email has been changed


DELIMITER //

CREATE TRIGGER resetEmail
BEFORE UPDATE ON users
FOR EACH ROW
  BEGIN
    IF NEW.email <> old.email THEN
      SET NEW.valid_email = IF(NEW.valid_email = 0, 1, 0);
    END IF;
  END;//

DELIMITER ;
