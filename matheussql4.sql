#create database escola

/*create table curso(
codigo_curso varchar(255) primary key,
nome_curso varchar(255) not null
);

create table turma(
codigo_turma varchar(255) primary key,
nome_turma varchar(255) not null,
codigo_curso varchar(255),
constraint fk_codigo_curso foreign key(codigo_curso) references curso(codigo_curso)
);

create table materia(
codigo_materia varchar(255) primary key,
nome_materia varchar(255) not null,
codigo_turma varchar(255),
constraint fk_codigo_turma foreign key(codigo_turma) references turma(codigo_turma)
);

create table professor(
registro_prof varchar(255) primary key,
nome_prof varchar(255) not null
);

create table aluno(
registro_aluno varchar(255) primary key,
nome_aluno varchar(255) not null,
endereco_aluno varchar(255) not null
)*/

insert into curso values (4, "Informática");
insert into turma values (2, "Turma 01", 3);
insert into materia values (4, "SQL", 2);
insert into professor values (5, "Vinicius");
insert into aluno values ("1", "Matheus", "Xique-Xique, Bahia");

/*create table cursa(
bimestre_cursa varchar(255) not null,
nota_cursa varchar(255) not null,
registro_aluno varchar(255),
constraint fk_registro_aluno foreign key(registro_aluno) references aluno(registro_aluno),
codigo_materia varchar(255),
constraint fk_codigo_materia foreign key(codigo_materia) references materia(codigo_materia)
);*/

/*create table leciona(
codigo_materia varchar(255),
constraint fk_codigo_materia2 foreign key(codigo_materia) references materia(codigo_materia),
registro_prof varchar(255),
constraint fk_registro_prof foreign key(registro_prof) references professor(registro_prof)
)*/

insert into cursa values (2, 10, 1, 4);
insert into leciona values (4, 5)