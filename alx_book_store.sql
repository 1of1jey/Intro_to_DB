CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;

    -- Create Authors table
CREATE TABLE Authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL
);

