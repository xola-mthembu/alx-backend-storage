-- Task 13: Create stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE user_cursor CURSOR FOR SELECT id FROM users;
	DECLARE done INT DEFAULT FALSE;
	DECLARE user_id INT;
	
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
	
	OPEN user_cursor;
	
	read_loop: LOOP
		FETCH user_cursor INTO user_id;
		IF done THEN
			LEAVE read_loop;
		END IF;
		
		CALL ComputeAverageWeightedScoreForUser(user_id);
	END LOOP;
	
	CLOSE user_cursor;
END;
//
DELIMITER ;
