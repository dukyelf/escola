/*create database teste_escola*/

/*create table estudantes(
estudante_id int primary key auto_increment,
nome varchar(100) not null,
curso varchar(50) not null
);

create table disciplinas(
disciplina_id int primary key auto_increment,
nome varchar(100) not null,
carga_horaria int not null
);

create table professores(
professor_id int primary key auto_increment,
nome varchar(100) not null,
departamento varchar(50) not null
);

create table matriculas(
matricula_id int primary key auto_increment,
estudante_id int not null,
disciplina_id int not null,
semestre varchar(10) not null,
foreign key (estudante_id) references estudantes(estudante_id),
foreign key (disciplina_id) references disciplinas(disciplina_id)
);*/

/*INSERT INTO estudantes (nome, curso) VALUES
('João Silva', 'Engenharia de Computação'),
('Maria Oliveira', 'Ciência da Computação'),
('Ana Santos', 'Sistemas de Informação'),
('Pedro Costa', 'Engenharia de Software'),
('Lucas Lima', 'Análise e Desenvolvimento de Sistemas');

INSERT INTO disciplinas (nome, carga_horaria) VALUES
('Algoritmos', 60),
('Banco de Dados', 80),
('Engenharia de Software', 40),
('Redes de Computadores', 70),
('Inteligência Artificial', 50);

INSERT INTO professores (nome, departamento) VALUES
('Carlos Mendes', 'Computação'),
('Luciana Braga', 'Engenharia de Software'),
('Roberto Farias', 'Redes e Sistemas'),
('Fernanda Tavares', 'Inteligência Artificial'),
('Paulo César', 'Banco de Dados');

INSERT INTO matriculas (estudante_id, disciplina_id, semestre) VALUES
(1, 1, '2023.1'),
(1, 2, '2023.1'),
(2, 3, '2023.1'),
(2, 4, '2023.1'),
(3, 1, '2023.2'),
(3, 5, '2023.2'),
(4, 2, '2023.1'),
(4, 4, '2023.1'),
(5, 3, '2023.2'),
(5, 5, '2023.2');*/

select nome, curso from estudantes
where curso like "%o";
