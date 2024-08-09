-- Creates trigger that resets attribute valid_email 
-- only when email has been changed
DELIMITER $$
-- allow the use of semicolons within the trigger body without ending
-- the trigger creation prematurely.
CREATE TRIGGER before_email_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER ;


