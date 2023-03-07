CREATE DATABASE IF NOT EXISTS gestao;

USE gestao;

CREATE TABLE IF NOT EXISTS tblapartamento (
  id int unsigned NOT NULL AUTO_INCREMENT,
  ap_name varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  ap_status int NOT NULL,
  edificio_id int NOT NULL,
  valor_aluguel float,
  locatario_nome varchar(250) COLLATE utf8mb4_unicode_ci,
  locatario_contato varchar(250) COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS tbledificio (
  id int unsigned NOT NULL AUTO_INCREMENT,
  edificio_name varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;