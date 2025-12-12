# Pawp

Aplicación para potenciar la adopción y el voluntariado en protectoras de animales

Documento de Requisitos del Sistema  
Desarrollo de Aplicaciones Multiplataforma – Proyecto de DAM

## Introducción

### Propósito del documento

Este documento tiene como objetivo definir los requisitos del sistema para potenciar la adopción y el voluntariado en protectoras de animales, dando a conocer los centros afiliados a la app y los animales que se encuentran en ellos.

### Alcance del sistema

El sistema permitirá a los diversos usuarios dar a conocer a aquellos animales que se encuentran de paso en centros de acogida. Los usuarios podrán ver diversos aspectos de los animales como fotos, ubicación, salud e incluso realizar voluntariado en dichos centros y, además, subir sus experiencias con los animales.

## Descripción general

El sistema permitirá a las protectoras hacer publicaciones de los animales que tienen en acogida. Estas publicaciones contendrán información importante sobre ellos como edad, raza, tamaño, salud, entre otros.

Por otro lado, los usuarios podrán realizar diversas acciones sobre los animales que han sido publicados, como realizar consultas simples, agregarlos a favoritos para seguir su evolución, comentar sus publicaciones y, para aquellos usuarios que hagan voluntariado, poder subir sus propias publicaciones contando sus experiencias con los animales.

## Actores principales

- **Super Admin**: gestiona usuarios, protectoras y controla el sistema.
- **Usuario (Voluntario)**: busca animales, puede marcar favoritos, comentar y solicitar adopciones. Además, puede reservar horas para pasear o ayudar en la protectora.
- **Admin (Refugio/Protectora)**: gestiona su panel, publica animales y controla solicitudes y reservas.

## Objetivos del sistema

- Dar más visibilidad a animales en situación de adopción.
- Facilitar la comunicación entre usuarios y protectoras.
- Potenciar el voluntariado y la participación activa en los centros.
- Ofrecer una experiencia social tipo red, con fotos, likes y comentarios.

## Casos de uso principales

1. Usuario se registra e inicia sesión (Usuario/Protectora).
2. Usuario busca un animal y consulta su ficha.
3. Usuario guarda un animal en favoritos.
4. Usuario solicita la adopción de un animal.
5. Usuario (voluntario) reserva un paseo o turno en la protectora.
6. Usuario consulta protectoras.
7. Admin publica un nuevo animal con fotos y descripción.
8. Usuario sube fotos propias con animales.
9. Super Admin revisa y modera contenido.

## Requisitos funcionales

- **RF1**: El sistema permitirá registrar usuarios con distintos roles.
- **RF2**: Los refugios podrán crear, editar y eliminar animales asociados a su protectora.
- **RF3**: Los usuarios podrán buscar animales por especie, edad, ubicación y estado.
- **RF4**: Los usuarios podrán guardar animales como favoritos.
- **RF5**: Los usuarios podrán solicitar la adopción de un animal.
- **RF6**: Los voluntarios podrán reservar horas de paseo o actividades en protectoras.
- **RF7**: El sistema mostrará información de salud del animal (vacunas, castrados, etc.).
- **RF8**: Los usuarios podrán subir fotos de experiencias con los animales.
- **RF9**: Los usuarios podrán comentar publicaciones de animales.
- **RF10**: El sistema enviará notificaciones de confirmación para adopciones o reservas.

## Requisitos no funcionales

- **RNF1**: El sistema constará de dos partes bien diferenciadas: frontend Android nativo y backend con FastAPI que incluirá una base de datos.
- **RNF2**: El backend estará dockerizado.
- **RNF3**: La aplicación para Android estará escrita en Kotlin con Jetpack Compose.
- **RNF4**: La interfaz de usuario deberá ser intuitiva y fácil de usar, con tiempos de carga bajos.
- **RNF5**: El sistema deberá cumplir con los estándares de seguridad para proteger la información sensible.
- **RNF6**: El sistema deberá estar cubierto con tests; cada nueva funcionalidad deberá tener, como mínimo, tests unitarios y también de integración.

## Requisitos de interfaz

La interfaz gráfica de usuario será desarrollada con Jetpack Compose, el framework para la creación de interfaces para aplicaciones Android.

## Requisitos de sistema

La aplicación de Android será desarrollada para teléfonos móviles con Android 12 o superior (API 31). Se utilizará Kotlin junto con Jetpack Compose.

El backend usará FastAPI, en su última versión disponible en el momento del desarrollo.

El motor de base de datos será MySQL, en su última versión. Se utilizará el ORM SQLModel, basado en SQLAlchemy, que usa Pydantic y está bien integrado con FastAPI.

El backend deberá ser desplegado mediante contenedores Docker, al menos dos: uno para FastAPI y otro para MySQL.

## Modelo de datos

El sistema contará con tablas principales para Usuarios, Protectoras y Animales, y tablas secundarias como Fotos, Comentarios, Favoritos, Adopciones y Reservas de voluntariado.

Se utilizará un modelo relacional y el diagrama entidad-relación reflejará las conexiones entre usuarios, animales y protectoras.

## Restricciones y reglas de negocio

- Un animal solo puede estar asociado a una protectora.
- Un usuario no puede reservar dos paseos en el mismo horario.
- Una adopción debe pasar siempre por la aprobación de la protectora.
- Los comentarios podrán ser eliminados si incumplen las normas de uso.

## Criterios de aceptación

- Un usuario podrá completar el registro si introduce al menos nombre, email y contraseña.
- Al guardar un favorito, el animal deberá aparecer en la lista personal de favoritos.
- Al crear una adopción, el sistema debe cambiar su estado a “pendiente” hasta que la protectora la procese.
- Al reservar voluntariado, el sistema confirmará fecha y hora y enviará una notificación.
- Al subir una foto, debe mostrarse asociada al animal correspondiente.

