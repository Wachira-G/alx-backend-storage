-- creates a trigger that decreases the quantity of an item after adding a new order

DELIMITER //

CREATE PROCEDURE proc_decreaseItems(item_name_param VARCHAR(255), quantity_decreased_param INT)
BEGIN
  UPDATE items SET quantity = quantity - quantity_decreased_param WHERE name = item_name_param;
END//


CREATE TRIGGER decreaseQuantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  CALL proc_decreaseItems(NEW.item_name, NEW.number);
END;//

DELIMITER ;
