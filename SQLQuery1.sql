create table animes(
rota_anime varchar(255) not null primary key,
nome_anime varchar(80) not null,
logo_anime varchar(80) not null,
descricao_anime varchar(120) not null,
trailer_anime varchar(80) not null
)

create table temporadas(
rota_anime varchar(255) not null foreign key references animes,
id_temporada int not null,
id_capitulos int not null foreign key references capitulos,
)

create table capitulos(
id_capitulo int not null primary key,
rota_anime varchar(255) not null foreign key references animes 
)

create table grupo_generos(
rota_anime varchar(255) not null foreign key references animes,
id_generos int not null foreign key references generos
)

create table generos(
id_genero int not null primary key,
nome_genero varchar(20) not null
)

select * from animes
select * from temporadas
select * from capitulos
select * from grupo_generos

select * from generos
insert into generos values(1,'Ação')
insert into generos values(2,'Artes Marciais')
insert into generos values(3,'Aventura')
insert into generos values(4,'Comédia')
insert into generos values(5,'Drama')
insert into generos values(6,'Escolar')
insert into generos values(7,'Esporte')
insert into generos values(8,'Ecchi')
insert into generos values(9,'Harém')
insert into generos values(10,'Hentai')
insert into generos values(11,'Isekai')
insert into generos values(12,'Iyashikei')
insert into generos values(13,'Josei')
insert into generos values(14,'Magia')
insert into generos values(15,'Mecha')
insert into generos values(16,'Mistério')
insert into generos values(17,'Música')
insert into generos values(18,'Psicológico')
insert into generos values(19,'Romance')
insert into generos values(20,'Sci-Fi')
insert into generos values(21,'Seinen')
insert into generos values(22,'Shoujo')
insert into generos values(23,'Shounen')
insert into generos values(24,'Slice of Life')
insert into generos values(25,'Sobrenatural')
insert into generos values(26,'SuperPoderes')
insert into generos values(27,'Terror')
insert into generos values(28,'Yaoi')
insert into generos values(29,'Yuri')


