--Caso 1
select 'El empleado ' || nombre_emp ||' '||appaterno_emp ||' '||apmaterno_emp ||' nacio el '|| to_char(fecnac_emp,'dd/mm/yyyy')
    as "Listado De Cumpleños"
from empleado
where to_char(fecnac_emp,'mm')= '&mes'
order by fecnac_emp asc;

--Caso 2
select to_char(numrut_cli,'99g999g999')||'-'||dvrut_cli as rut_cliente, INITCAP(appaterno_cli ||' '||apmaterno_cli||' '||nombre_cli) as "Nombre Cliente",
        renta_cli as Renta,fonofijo_cli as Telefono,nvl(celular_cli,0)as "Celular Cliente"   
from cliente
order by appaterno_cli,apmaterno_cli;

--Caso 3
select nombre_emp ||' '||appaterno_emp ||' '|| apmaterno_emp as "NOMBRE EMPLEADO",sueldo_emp as SUELDO,
        sueldo_emp*0.5 as BONIFICACION
from empleado
order by sueldo_emp*0.5 desc;

--Caso 4
select nro_propiedad as "NRO PROPIEDAD",numrut_prop as "RUT PROPIETARIO",
        direccion_propiedad as DIRECCION,valor_arriendo as "VALOR ARRIENDO",
        (valor_arriendo*5.4)/100 as "VALOR COMPENSACION"
from propiedad
order by numrut_prop asc;

--Caso 5
select numrut_emp ||'-'|| dvrut_emp as "RUN EMPLEADO",
        nombre_emp ||' '||appaterno_emp ||' '|| apmaterno_emp as "NOMBRE EMPLEADO",
        sueldo_emp as "SALARIO ACTUAL",
        ((sueldo_emp*0.13)+sueldo_emp)as "SALARIO REAJUSTADO",
        (sueldo_emp*0.13) as REAJUSTE
from empleado
order by "REAJUSTE" desc,appaterno_emp asc;

--Caso 6
select nombre_emp ||' '||appaterno_emp ||' '|| apmaterno_emp as "NOMBRE EMPLEADO",
        sueldo_emp as SALARIO,
        ((sueldo_emp*0.55)/10)as COLACION,
        ((sueldo_emp*0.178)/1) as MOVILIZACION,
        ((sueldo_emp*0.78)/10) as SALUD,
        ((sueldo_emp*0.65)/10) as AFP,
        (sueldo_emp+((sueldo_emp*0.55)/10)+((sueldo_emp*0.178)/1)
        -((sueldo_emp*0.78)/10)-((sueldo_emp*0.65)/10) ) as "ALCANCE LIQUIDO" 
from empleado
order by appaterno_emp asc,apmaterno_emp desc;