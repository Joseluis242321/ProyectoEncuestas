# Sistema de Encuestas y Retroalimentación Simple

## Descripción
Este proyecto implementa una aplicación para crear y gestionar encuestas sencillas, permitiendo recopilar retroalimentación de usuarios sobre cursos, eventos u otros temas. Desarrollado con Python y Tkinter para la interfaz gráfica, utiliza MongoDB como base de datos para almacenar las encuestas y sus respuestas.

## Características Principales
- **Interfaz de Usuario Intuitiva**: Acceso mediante login y navegación sencilla entre módulos
- **Creación de Encuestas**: Herramientas para administradores para diseñar encuestas personalizadas
- **Respuesta a Encuestas**: Interfaz amigable para que usuarios respondan encuestas disponibles
- **Visualización de Resultados**: Análisis y resúmenes de las respuestas recibidas
- **Gestión de Usuarios**: Control de acceso a encuestas específicas (módulo opcional)

## Tecnologías Utilizadas
- **Frontend**: Python con Tkinter para interfaces gráficas
- **Backend**: Python
- **Base de Datos**: MongoDB
- **Control de Versiones**: Git
- **Contenedorización**: Docker y Docker Compose

## Estructura del Proyecto
El proyecto está dividido en varios módulos, cada uno implementado por un miembro diferente del equipo:

1. **Módulo de Login**: Ventana principal para acceso al sistema
2. **Módulo de Interfaz de Usuario**: Para ver y responder encuestas disponibles
3. **Módulo de Creación y Edición**: Para que administradores creen y modifiquen encuestas
4. **Módulo de Visualización de Resultados**: Para analizar las respuestas recopiladas
5. **Módulo de Gestión de Usuarios**: Para administrar permisos de acceso (opcional)

## Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- MongoDB instalado y en ejecución
- Las siguientes bibliotecas de Python:
  - tkinter
  - pymongo
  - pillow (para procesamiento de imágenes en la GUI)

## Uso
1. **Para Usuarios**:
   - Iniciar sesión con credenciales proporcionadas
   - Navegar al módulo de "Responder Encuestas"
   - Seleccionar una encuesta disponible y completarla
   - Enviar respuestas

2. **Para Administradores**:
   - Iniciar sesión con credenciales de administrador
   - Acceder a los módulos de creación o visualización
   - Crear nuevas encuestas o revisar resultados de encuestas existentes

## Estructura de la Base de Datos
- **Colección Users**: Almacena información de usuarios y administradores
- **Colección Surveys**: Contiene las encuestas creadas con sus preguntas
- **Colección Responses**: Guarda las respuestas de los usuarios a las encuestas

## Contribuciones
El proyecto está desarrollado por el Equipo 5 como parte de la actividad ExU5. Cada miembro es responsable de implementar un módulo específico y documentar su trabajo siguiendo la estructura establecida.

### Guía para Contribuidores
1. Crear una rama con tu nombre para tu módulo
2. Implementar las interfaces y funcionalidades asignadas
3. Documentar las GUIs con wireframes y capturas del diseño final
4. Grabar un video explicativo de tu implementación
5. Actualizar el documento principal con tu contribución
6. Solicitar revisión y fusión de tu rama

## Equipo de Desarrollo
- [Nombre Apellido 1] - [Módulo desarrollado]
- [Nombre Apellido 2] - [Módulo desarrollado]
- [Nombre Apellido 3] - [Módulo desarrollado]
- [Nombre Apellido 4] - [Módulo desarrollado]
- [Nombre Apellido 5] - [Módulo desarrollado]

## Licencia
Este proyecto es desarrollado con fines educativos como parte de una actividad académica.
