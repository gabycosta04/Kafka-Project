CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100)
);

INSERT INTO clientes (nombre, email) VALUES
('Ana', 'ana@example.com'),
('Luis', 'luis@example.com');
('Cristian', 'cristian@example.com'),
('Gabriel', 'gabriel@example.com');