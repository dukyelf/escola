#create database farmacia

/*;CREATE TABLE farmatable(
cnpj_farm varchar(11) primary key,
nome_farm varchar(255) not null,
end_farm varchar(255) not null,
tel_farm varchar(13) not null
)*/

/*create table produto(
cod_produto varchar(255) primary key,
qtd_produto varchar(255) not null,
valor_produto decimal(5,2) not null
)*/

/*create table farmaceutico(
rg_farmaceutico varchar(255) primary key,
nome_farmaceutico varchar(255) not null
)*/

/*create table vende(
cnpj_fk varchar(255),
constraint fk_cnpj_farm foreign key (cnpj_fk)
references farmatable(cnpj_farm)
)*/

create table trabalha(
cnpj_fk varchar(255),
constraint fk_cnpj_farm2 foreign key (cnpj_fk)
references farmatable(cnpj_farm)
)
