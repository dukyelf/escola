#create database firma

/*create table funcionario(
cpf varchar(11) primary key,
nome varchar(255) not null,
salario decimal(10,2) not null
)*/

/*CREATE TABLE empresa(
cnpj varchar(30) primary key,
razao_social varchar(255) not null,
endereco varchar(255) not null
)*/

/*create table trabalho(
tempo_servico varchar(255) not null,
cnpj_fk varchar(255),
cpf_fk varchar(11),
constraint fk_cpf_func foreign key (cpf_fk)
references funcionario(cpf),
constraint fk_cnpj_emp foreign key (cnpj_fk)
references empresa(cnpj)
)*/

alter table funcionario rename column Farrokh Bulsara to Freddie Mercury;