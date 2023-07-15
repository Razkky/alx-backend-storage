-- Create a procedure ComputeAverageScoreForUser
-- It computes the average score of a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    p_user_id INT
)
BEGIN
    DECLARE avg_score DECIMAL(10, 2);
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE user_id = p_user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = p_user_id;
END $$
DELIMITER ;