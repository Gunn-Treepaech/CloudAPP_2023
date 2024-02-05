USE example;

CREATE TABLE IF NOT EXISTS example_data (
    test_g VARCHAR(50),
    test_u DECIMAL(4, 2),
    test_n DECIMAL(5, 2),
    PRIMARY KEY (test_g)
);

INSERT INTO example_data (test_g, test_u, test_n) VALUES
    ('SCB', 0, 7.300),
    ('UOB', 0, 8.800),
    ('KTB', 0, 7.570),
    ('Kbank', 0, 7.300);
