-- Task 13: Show and compute average weighted score for all users
SELECT * FROM users;
SELECT * FROM projects;
SELECT * FROM corrections;

CALL ComputeAverageWeightedScoreForUsers();

SELECT "--";
SELECT * FROM users;
