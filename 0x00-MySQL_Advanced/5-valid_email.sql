-- Creates trigger that reset valid_email Only wen email has been validated


DELIMITER $$
CREATE TRIGGER validate_email
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF OLD.email <> NEW.email THEN
    SET NEW.valid_email = 0;
    END IF;
END$$
DELIMITER ;