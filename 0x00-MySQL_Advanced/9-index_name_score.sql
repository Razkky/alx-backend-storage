-- Creates an index on table names using name and score
DELIMITER $$
CREATE INDEX idx_name_first_score ON names (LEFT(name, 1), score)$$
DELIMITER ;
