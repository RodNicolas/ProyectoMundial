# ProyectoMundial
Entrega intermedia Proyecto Final
<p>Este proyecto es realizado para el curso Python de CoderHouse por los alumnos Nicolas Rodriguez, Maximiliano Barraza y Nicolas Finetti <p/>
<p>En esta entrega intermedia se crea un proyecto para cargar datos a una base de datos con información del Mundial Qatar 2022 <p/>
<p>Para esto se crearon cuatro clases en el modelo con sus respectivos atributos:<p/>
<ol>
  <li>Paises: nombre, continente, grupo</li>
  <li>Jugadores: nombre, apellido, edad, pais, equipo</li>
  <li>Estadios: nombre, capacidad</li>
  <li>Partidos: instancia, pais1, pais2, resultado</li>
</ol>

<p>Para cada clase se creo un formulario de carga para insertar datos <p/>
<p>Para la clase Pais se crearon dos busquedas: <p/>
<ol>
  <li>Buscar paises por continente: permite ingresar un continente (Europa, Asia, Africa, Oceania, America del Sur, America del norte) y enlistar todos los paises de ese continente/li>
  <li>Buscar paises por grupo: permite ingresar un grupo y obtener todos los paises de ese grupo</li>
 </ol>
<p> Para la clase Jugadores se crearon dos busquedas: <p/>
<ol>
  <li>Buscar jugadores por pais: permite ingresar un pais y enlistar todos los jugadores de ese pais</li>
  <li>Buscar jugadores por equipo: permite ingresar un equipo y enlistar todos los jugadores de ese equipo</li>
 </ol>
<p>En cuanto a la navegacion, el proyecto tiene una pagina de inicio y una pagina de contenido por cada clase. Dentro de la pagina de cada clase se observan los botones que llevan tanto a la carga de datos como a las busquedas cuando corresponda. Todos los templates estan heredados de un template padre. <p/>
<p> Hasta el momento en la base de datos se cargaron todos los paises del Mundial y todos los estadios. Se probó la carga de un partido inventando un resultado. Para probar la clase Jugadores se cargaron algunos jugadores de la seleccion Argentina <p/>
