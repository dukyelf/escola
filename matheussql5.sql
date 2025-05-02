#create database vendas;

#create table cliente(
#id_cliente int primary key auto_increment,
#nome varchar(255) not null,
#cpf varchar(11) not null
#);

#create table produto(
#id_produto int primary key auto_increment,
#nome_produto varchar(255) not null,
#preco decimal(10,2) not null
#);

/*create table compra(
id_compra int primary key auto_increment,
id_produto int,
id_cliente int,
constraint fk_id_prod foreign key(id_produto)
references produto(id_produto),
constraint fk_id_cli foreign key(id_cliente)
references cliente(id_cliente)
);*/

insert into cliente
values (null, 'Matheus da Nóbrega', '11214122322');

insert into produto
values (null, 'AOC 24G2E1', 629.99);

insert into compra
values (null, 1, 1);

select * from compra