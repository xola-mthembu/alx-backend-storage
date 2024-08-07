# 0x00. MySQL Advanced

This project covers advanced concepts in MySQL, including creating tables with constraints, optimizing queries with indexes, implementing stored procedures, functions, views, and triggers.

## Files and Descriptions

1. **0-uniq_users.sql**: SQL script to create a table `users` with unique email constraint.
2. **1-country_users.sql**: SQL script to create a table `users` with an enumeration type for `country`.
3. **2-fans.sql**: SQL script to rank countries of bands by the number of fans.
4. **3-glam_rock.sql**: SQL script to list all bands with Glam rock as their main style, ranked by their longevity.
5. **4-store.sql**: SQL script to create a trigger that decreases the quantity of an item after adding a new order.
6. **5-valid_email.sql**: SQL script to create a trigger that resets the `valid_email` attribute when the email has been changed.
7. **6-bonus.sql**: SQL script to create a stored procedure `AddBonus` that adds a new correction for a student.
8. **7-average_score.sql**: SQL script to create a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.
9. **8-index_my_names.sql**: SQL script to create an index on the first letter of the `name` in the table `names`.
10. **9-index_name_score.sql**: SQL script to create an index on the first letter of the `name` and the `score` in the table `names`.
11. **10-div.sql**: SQL script to create a function `SafeDiv` that performs safe division.
12. **11-need_meeting.sql**: SQL script to create a view `need_meeting` listing students with scores under 80 and no recent meeting.
13. **100-average_weighted_score.sql**: SQL script to create a stored procedure `ComputeAverageWeightedScoreForUser` that computes and stores the average weighted score for a student.
14. **101-average_weighted_score.sql**: SQL script to create a stored procedure `ComputeAverageWeightedScoreForUsers` that computes and stores the average weighted score for all students.

## Technologies Used
- MySQL 5.7
- Ubuntu 18.04 LTS
