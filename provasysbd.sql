-- Active: 1735772609456@@127.0.0.1@3306@cursoinfinity
CREATE DATABASE IF NOT EXISTS cursoinfinity;
USE cursoinfinity;

CREATE TABLE IF NOT EXISTS Produtos (
	ID INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR (50) NOT NULL UNIQUE,
    Descricao TEXT,
    Quantidade_disponivel INT NOT NULL,
    Preco DECIMAL (10, 2) NOT NULL
)

CREATE TABLE IF NOT EXISTS Vendas (
	ID_Vendas INT PRIMARY KEY AUTO_INCREMENT,
    ID_Produto_Vendido INT NOT NULL,
    Quantidade_Vendida INT NOT NULL,
    Data_venda DATE NOT NULL,
    CONSTRAINT fk_produto FOREIGN KEY (ID_Produto_Vendido) REFERENCES Produtos (ID)
)

select * from Produtos;
select * from Vendas;