import sqlite3

def connect():
    return sqlite3.connect('tasks.db')

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY, 
                       title TEXT, 
                       description TEXT, 
                       priority TEXT, 
                       deadline DATE)''')
    conn.commit()
    conn.close()

def add_task(title, description, priority, deadline):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO tasks (title, description, priority, deadline) 
                      VALUES (?, ?, ?, ?)''', (title, description, priority, deadline))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task(task_id, title, description, priority, deadline):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks 
        SET title = ?, description = ?, priority = ?, deadline = ?
        WHERE id = ?
    ''', (title, description, priority, deadline, task_id))
    conn.commit()
    conn.close()

def load_example_tasks():
    tasks = [
    ("Revisar inventario de libros", "Revisar y actualizar el inventario de todos los libros", "Alta", "2024-07-15"),
    ("Catalogar nuevos libros", "Catalogar y registrar nuevos libros recibidos", "Media", "2024-07-16"),
    ("Organizar estanterías", "Reorganizar los libros en las estanterías según el nuevo sistema", "Baja", "2024-07-17"),
    ("Preparar eventos", "Preparar el espacio y materiales para eventos de lectura", "Alta", "2024-07-18"),
    ("Responder correos", "Responder a los correos electrónicos de usuarios y proveedores", "Media", "2024-07-19"),
    ("Revisar devoluciones", "Verificar y registrar las devoluciones de libros", "Alta", "2024-07-20"),
    ("Capacitación de personal", "Realizar capacitación sobre el uso del nuevo sistema de catalogación", "Media", "2024-07-21"),
    ("Limpiar área de lectura", "Asegurarse de que el área de lectura esté limpia y ordenada", "Baja", "2024-07-15"),
    ("Reparar libros dañados", "Reparar libros que hayan sido devueltos en mal estado", "Alta", "2024-07-16"),
    ("Actualizar catálogo digital", "Añadir nuevos libros al catálogo digital", "Media", "2024-07-17"),
    ("Atender consultas telefónicas", "Responder llamadas y consultas de los usuarios", "Media", "2024-07-18"),
    ("Configurar equipo audiovisual", "Configurar el equipo para presentaciones y eventos", "Alta", "2024-07-19"),
    ("Supervisar pasantes", "Supervisar y guiar a los pasantes en sus tareas diarias", "Media", "2024-07-20"),
    ("Realizar inventario de revistas", "Actualizar el inventario de revistas y publicaciones periódicas", "Baja", "2024-07-21"),
    ("Organizar libros por autor", "Reorganizar los libros en las estanterías por autor", "Media", "2024-07-15"),
    ("Actualizar sitio web", "Añadir noticias y eventos próximos al sitio web de la biblioteca", "Media", "2024-07-16"),
    ("Preparar boletín informativo", "Preparar y enviar el boletín informativo mensual a los usuarios", "Alta", "2024-07-17"),
    ("Evaluar sugerencias de usuarios", "Revisar y evaluar las sugerencias de compra de los usuarios", "Media", "2024-07-18"),
    ("Realizar encuestas de satisfacción", "Llevar a cabo encuestas para evaluar la satisfacción de los usuarios", "Media", "2024-07-19"),
    ("Inventario de material multimedia", "Actualizar el inventario de películas, CDs y otros materiales multimedia", "Baja", "2024-07-20"),
    ("Planificar club de lectura", "Organizar y planificar las sesiones del club de lectura", "Alta", "2024-07-21"),
    ("Gestionar reservas de salas", "Gestionar y coordinar las reservas de salas de estudio y eventos", "Media", "2024-07-15"),
    ("Revisar políticas de préstamo", "Actualizar y revisar las políticas de préstamo de la biblioteca", "Alta", "2024-07-16"),
    ("Coordinar con proveedores", "Comunicar y coordinar con proveedores de libros y servicios", "Media", "2024-07-17"),
    ("Realizar auditoría interna", "Llevar a cabo una auditoría interna del inventario y procesos", "Alta", "2024-07-18"),
    ("Actualizar bases de datos", "Actualizar y respaldar las bases de datos de usuarios y préstamos", "Alta", "2024-07-19"),
    ("Organizar actividades para niños", "Planificar y organizar actividades y talleres para niños", "Media", "2024-07-20"),
    ("Evaluar colecciones especiales", "Revisar y evaluar la necesidad de adquirir colecciones especiales", "Baja", "2024-07-21"),
    ("Organizar sesiones de estudio", "Coordinar y organizar sesiones de estudio en grupo", "Media", "2024-07-15"),
    ("Mantenimiento de equipos", "Realizar el mantenimiento de equipos informáticos y audiovisuales", "Alta", "2024-07-16"),
    ("Actualizar redes sociales", "Publicar y actualizar contenido en las redes sociales de la biblioteca", "Media", "2024-07-17"),
    ("Gestionar donaciones", "Revisar y gestionar las donaciones de libros y materiales", "Alta", "2024-07-18"),
    ("Promover servicios", "Promover los servicios de la biblioteca a través de diferentes medios", "Media", "2024-07-19"),
    ("Actualizar sistema de seguridad", "Actualizar y verificar el sistema de seguridad de la biblioteca", "Alta", "2024-07-20"),
    ("Revisar suscripciones", "Revisar y renovar suscripciones a revistas y publicaciones", "Baja", "2024-07-21"),
    ("Gestionar préstamos interbibliotecarios", "Coordinar y gestionar préstamos con otras bibliotecas", "Media", "2024-07-15"),
    ("Organizar exposiciones", "Planificar y montar exposiciones temporales en la biblioteca", "Alta", "2024-07-16"),
    ("Atender a usuarios con necesidades especiales", "Proveer asistencia y recursos a usuarios con necesidades especiales", "Media", "2024-07-17"),
    ("Actualizar señalización", "Actualizar la señalización y cartelería dentro de la biblioteca", "Baja", "2024-07-18"),
    ("Realizar talleres de formación", "Organizar talleres de formación sobre el uso de recursos de la biblioteca", "Alta", "2024-07-19"),
    ("Coordinar eventos comunitarios", "Coordinar y promover eventos comunitarios en la biblioteca", "Media", "2024-07-20"),
    ("Gestionar archivo histórico", "Revisar y actualizar el archivo histórico de la biblioteca", "Alta", "2024-07-21"),
    ("Realizar estudios de usuarios", "Realizar estudios para comprender mejor las necesidades de los usuarios", "Media", "2024-07-15"),
    ("Preparar informes de gestión", "Preparar informes mensuales de gestión y estadísticas", "Alta", "2024-07-16"),
    ("Organizar campañas de lectura", "Planificar y ejecutar campañas de fomento de la lectura", "Media", "2024-07-17"),
    ("Gestionar reservas de libros", "Coordinar y gestionar las reservas de libros por parte de los usuarios", "Alta", "2024-07-18"),
    ("Actualizar recursos electrónicos", "Revisar y actualizar los recursos electrónicos disponibles", "Media", "2024-07-19")
]

    
    conn = connect()
    cursor = conn.cursor()
    cursor.executemany('''INSERT INTO tasks (title, description, priority, deadline) 
                          VALUES (?, ?, ?, ?)''', tasks)
    conn.commit()
    conn.close()

create_table()
load_example_tasks()
