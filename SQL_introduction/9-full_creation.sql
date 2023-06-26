-- comment
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
)
INSERT INTO (id, name, score)
SELECT 1, "John", 10
UNION ALL
SELECT 2, "Alex", 3
UNION ALL
SELECT 3, "Bob", 14
UNION ALL
SELECT 4, "George", 8
UNION ALL;
