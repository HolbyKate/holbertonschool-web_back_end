-- creates a stored procedure AddBonus that adds a new correction for a student
DELIMITER //
--  Changes the delimiter from ; to // to allow the creation of the stored
-- procedure without prematurely ending it.
CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT;

    -- Check if the project already exists
    SELECT id INTO v_project_id
    FROM projects
    WHERE name = p_project_name;

    -- If the project does not exist, create it
    IF v_project_id IS NULL THEN
        INSERT INTO projects(name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the new correction record
    INSERT INTO corrections(user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);
END //

DELIMITER ;

