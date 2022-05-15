CREATE database eleicao;

use eleicao;

CREATE TABLE eleitor (
id INT auto_increment primary key,
nome varchar(100) not null,
cpf varchar (14) not null unique,
id_voto int not null
) ;

create table candidato (
id_candidato int primary key not null,
nome varchar(100) not null,
partido varchar(20) not null
);

create table urna (
id_urna int auto_increment primary key,
votos int not null
);

ALTER TABLE ELEITOR ADD FOREIGN KEY (id_voto) REFERENCES candidato(id_candidato);
ALTER TABLE urna ADD FOREIGN KEY (votos) REFERENCES candidato(id_candidato);

