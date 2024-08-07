-- Task 12: Create stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_score FLOAT;
	DECLARE total_weight INT;
	
	SELECT SUM(score * weight) / SUM(weight) INTO weighted_score
	FROM corrections
	JOIN projects ON corrections.project_id = projects.id
	WHERE user_id = user_id;
	
	UPDATE users SET average_score = weighted_score WHERE id = user_id;
END;
//
DELIMITER ;
