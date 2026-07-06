# Sistema de Gestión de Veterinaria

## Descripción del proyecto

Este proyecto consiste en un sistema de gestión para una veterinaria desarrollado en Python. El programa funciona por consola y permite registrar mascotas, visualizar mascotas cargadas, solicitar turnos, registrar atenciones médicas, ver servicios realizados y consultar estadísticas básicas.

El objetivo del trabajo es aplicar los contenidos vistos en el laboratorio de Python, utilizando variables, estructuras condicionales, estructuras repetitivas, funciones, listas, validaciones, manejo de errores, acumuladores y contadores.

## Integrantes

- Drago Valdez Picech
- Juan Pablo Almiron
- Juan Cruz Singh Ressia
- Octavio Nuñez

## Comisión

Comision k1.2

## Funcionalidades del sistema

El sistema permite:

1. Registrar mascotas.
2. Ver mascotas registradas.
3. Solicitar turnos.
4. Registrar atención médica.
5. Ver servicios realizados.
6. Ver estadísticas.
7. Salir del sistema.

## Detalle de funcionalidades

### Registrar mascota

Permite cargar los datos básicos de una mascota:

- Nombre de la mascota.
- Especie.
- Edad.
- Nombre del dueño.

Además, se validan los datos ingresados para evitar campos vacíos y edades negativas o no numéricas.

### Ver mascotas registradas

Muestra todas las mascotas cargadas en el sistema.

### Solicitar turno

Permite registrar un turno para una mascota previamente cargada. Se solicita:

- Nombre de la mascota.
- Día del turno.
- Horario.
- Motivo de consulta.

El sistema valida que la mascota exista antes de registrar el turno.

### Registrar atención médica

Permite cargar una atención realizada a una mascota registrada. Se solicita:

- Nombre de la mascota.
- Tipo de servicio.
- Descripción de la atención.
- Costo del servicio.

Tipos de servicio disponibles:

1. Consulta general.
2. Vacunación.
3. Desparasitación.
4. Control médico.
5. Urgencia.

### Ver servicios realizados

Muestra los servicios médicos registrados, indicando mascota, tipo de servicio, descripción y costo.

### Ver estadísticas

Muestra estadísticas básicas del sistema:

- Cantidad de mascotas registradas.
- Cantidad de turnos solicitados.
- Cantidad de servicios realizados.
- Total recaudado.
- Cantidad de servicios por tipo.

## Tecnologías utilizadas

- Python.
- Visual Studio Code.
- GitHub o GitLab.

## Cómo ejecutar el programa

Para ejecutar el sistema, se debe abrir una terminal en la carpeta del proyecto y escribir:

python main.py


## Reparto de tareas

Drago Valdez Picech

Menú principal, estructura general del programa y validación de opciones.

Juan Pablo Almiron

Registro de mascotas y visualización de mascotas registradas.

Juan Cruz Singh Ressia

Solicitud de turnos y registro de atención médica.

Octavio Nuñez

Visualización de servicios realizados, estadísticas, README, repositorio y video demo.

## Uso de inteligencia artificial

Para el desarrollo del trabajo se utilizó inteligencia artificial como apoyo para organizar la estructura del programa, corregir errores, mejorar validaciones y redactar el README.

La IA se usó como herramienta de asistencia, pero el grupo revisó y probó el código para comprender su funcionamiento.

## Estado del proyecto

El sistema se encuentra funcional y permite realizar las operaciones principales solicitadas para la gestión básica de una veterinaria.