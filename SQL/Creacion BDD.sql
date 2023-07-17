create table propietario(
    numero numeric(8) constraint PK_PROPIETARIO primary key,
    nombre varchar2(20) not null,
    apellido varchar2(20) not null,
    direccion varchar2(40) not null,
    sexo char(1) not null constraint SEXO_PROP_CK check (sexo in(  'M','F','O'))
    );
 
 create sequence seq_prop start with 150 increment by 1;
 
insert into propietario values (seq_prop.nextval,'Daniel','Bravo','Nos 37559','M');
insert into propietario values (seq_prop.nextval,'Rosa','Veloso','Las Perdices 375','F');
insert into propietario values (seq_prop.nextval,'Alberto','Martinez','Los Lirios 5762','M');
insert into propietario values (seq_prop.nextval,'Fabiola','Salazar','Pablo Rocka 8755','F');

commit;
 
 create table cliente(
    numero numeric(6) constraint PK_CLIENTE primary key,
    nombre varchar2(20) not null,
    apellido varchar2(20) not null,
    direccion varchar2(40) not null,
    telefono numeric(12)
 );

create sequence seq_client start with 10 increment by 1;

insert into cliente values (seq_client.nextval,'Juan','Pérez','Azucenas 345','225556778');
insert into cliente values (seq_client.nextval,'Daniela','Muñoz','Becker 200','227755398');
insert into cliente values (seq_client.nextval,'Luis','Aravena','Alameda Oriente 8764','229988776');
insert into cliente values (seq_client.nextval,'Ana','Silva','Lumina 8634','222815538');	

commit;
 
create table oficina(
    numero numeric(8) constraint PK_OFICINA primary key,
    calle varchar2(20) not null,
    ciudad varchar2(30) not null,
    codigo_postal numeric(10) not null
 );

create sequence sq_oficina start with 50 increment by 1;

insert into oficina values (sq_oficina.nextval,'Vicuña 7854','Santiago','3008530');
insert into oficina values (sq_oficina.nextval,'Jardin Alto 274','La Serena','4706968');
insert into oficina values (sq_oficina.nextval,'Puente Bajo 8485','Viña Del Mar','9470785');
insert into oficina values (sq_oficina.nextval,'Antúnez 22664','Rancagua','7433696');
commit;
  
 create table empleado(
	numero numeric(5) constraint PK_EMPLEADO primary key,
	nombre varchar2(20) not null,
	apellido varchar2(20) not null,
	cargo varchar2(20) not null,
	sexo char(1) not null constraint SEXO_EMPL_CK check (sexo in(  'M','F','O')),
	sueldo numeric(8) not null,
	oficina_num numeric(8) not null constraint FK_EMPLEADO references oficina (numero)
);

create sequence sq_emple start with 200 increment by 5;

insert into empleado values (sq_emple.nextval,'Lorenzo','Paredes','Conserje','M','450000','50');
insert into empleado values (sq_emple.nextval,'Ema','Allendes','Limpieza','F','250000','51');
insert into empleado values (sq_emple.nextval,'Braulio','Chavez','Administrador','M','750000','52');
insert into empleado values (sq_emple.nextval,'Paulina','Navarro','Seguridad','F','480000','52');
	
	
create table propiedad(
	numero numeric(8) constraint PK_PROPIEDAD primary key,
	calle varchar2(20) not null,
	ciudad varchar2(30) not null,
    codigo_postal numeric(10) not null,
	tipo varchar2(30) not null,
	habitacion numeric(3) not null,
	valor numeric(10) not null,
	propietario_num numeric(8) not null constraint FK_PROPIEDAD_PROPIETARIO references propietario(numero),
	empleado_numero numeric(5) not null constraint FK_PROPIEDAD_EMPLEADO references empleado(numero)
);

create sequence seq_propie start witg 100 increment by 10;

insert into propiedad values (seq_propie.nextval,'Carmelas 3747','Santiago','3889876','Oficina','0','80000000','150','200');
insert into propiedad values (seq_propie.nextval,'Numero 388','Viña Del Mar','9998877','Casa','3','120000000','151','205');  
insert into propiedad values (seq_propie.nextval,'Las Parcelas 8980','Santiago','45457667','Departamento','2','85000000','152','210'); 	
insert into propiedad values (seq_propie.nextval,'1 Norte 5446','La Serena','6008090','Casa','4','150000000','152','215'); 

create table visita(
	cliente_numero numeric(6) not null constraint FK_VISITA_CLIENTE references cliente (numero),
	propiedad_numero numeric(8) not null constraint FK_VISITA_PROPIEDAD references propiedad(numero),
	apellido varchar2(20) not null,
    direccion varchar2(40) not null,
    telefono numeric(12),
	constraint PK_VISITA primary key (cliente_numero,propiedad_numero)
	);

insert into visita values ('10','100','Pérez','Azucenas 345','225556778');	
insert into visita values ('11','110','Muñoz','Becker 200','227755398');	
insert into visita values ('12','120','Aravena','Alameda Oriente 8764','229988776');	
insert into visita values ('13','130','Silva','Lumina 8364','222815538');		