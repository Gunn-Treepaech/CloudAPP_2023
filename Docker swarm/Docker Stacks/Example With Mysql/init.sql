USE example;

CREATE TABLE IF NOT EXISTS example_data (
    test1 VARCHAR(50),
    test2 DECIMAL(4, 2),
    test3 DECIMAL(5, 2),
    PRIMARY KEY (test1)
);

INSERT INTO example_data (test1, test2, test3) VALUES
    ('SCB', 0, 7.300),
    ('UOB', 0, 8.800),
    ('KTB', 0, 7.570),
    ('Kbank', 0, 7.300);
