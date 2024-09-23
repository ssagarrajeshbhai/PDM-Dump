DO $$
DECLARE
    rec RECORD;
    random_a_id INT;
    random_b_id INT;
BEGIN
    FOR rec IN SELECT * FROM table_c WHERE foreign_key_a IS NULL OR foreign_key_b IS NULL
    LOOP
        SELECT id INTO random_a_id FROM table_a ORDER BY RANDOM() LIMIT 1;
        SELECT id INTO random_b_id FROM table_b ORDER BY RANDOM() LIMIT 1;
        
        UPDATE table_c
        SET 
            foreign_key_a = random_a_id,
            foreign_key_b = random_b_id
        WHERE 
            c.id = rec.id;  -- use the primary key of table_c
    END LOOP;
END $$;
