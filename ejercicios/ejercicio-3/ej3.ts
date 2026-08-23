/*
    Definir una interfaz para una persona (nombre, edad).
    Crear un objeto que use la interfaz y mostrar sus propiedades.
*/

interface Persona {
    nombre: string;
    edad: number;
}

const estudiante: Persona = { nombre: "Santiago", edad: 22};



console.log(estudiante);

