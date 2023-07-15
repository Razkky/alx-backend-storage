-- Create a function that divides first number by second number

DELIMITER $$
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL
DETERMINISTIC
BEGIN
    DECLARE result DECIMAL;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END$$
DELIMITER ;