-- a script that creates the table id_not_null on your MySQL server.
-- id_not_null description:
-- id INT must be unique
-- name VARCHAR(256)
CREATE TABLE IF NOT EXISTS unique_id
(id INT DEFAULT 1 UNIQUE,
name VARCHAR(256) NOT NULL
);
