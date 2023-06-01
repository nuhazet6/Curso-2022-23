from __future__ import annotations

import sqlite3

DB_PATH = 'todo.db'
TASK_DONE_SYMBOL = '✔'
TASK_PENDING_SYMBOL = '⎕'
SYMBOLS = [TASK_PENDING_SYMBOL,TASK_DONE_SYMBOL]

class Task:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    

    def __init__(self, name: str, done: bool = False, id: int = -1):
        '''Crea los atributos homónimos a los parámetros'''
        self.name = name
        self.done = done
        self.id = id

    def save(self):
        '''Guarda esta tarea en la base de datos.
        El identificador asignado en la base de datos se debe usar para actualizar el
        atributo id de la tarea.'''
        sql = f'''INSERT INTO
        tasks (name,done)
        VALUES ('{self.name}',{int(self.done)})'''
        Task.cur.execute(sql)
        Task.con.commit()
        self.id = Task.cur.lastrowid

    def update(self):
        '''Actualiza la tarea (nombre y estado) en la base de datos'''
        sql = f'UPDATE tasks SET name="{self.name}",done={int(self.done)} WHERE id={self.id}'
        self.cur.execute(sql)
        self.con.commit()

    def check(self):
        '''Marca la tarea como completada. Haz uso también de .update()'''
        self.done = True
        self.update()

    def uncheck(self):
        '''Marca la tarea como no completada. Haz uso también de .update()'''
        self.done = False
        self.update()

    def __repr__(self):
        '''Muestra la tarea en formato:
        <SYMBOL> <name> (id=<id>)'''
        return f'{SYMBOLS[int(self.done)]} {self.name} (id={self.id})'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row) -> Task:
        '''Construye una nueva tarea a partir de una fila de consulta devuelta por execute()'''
        new_id = row[0]
        new_name = row[1]
        new_done = bool(row[2])
        return Task(new_name,new_done,new_id)

    @classmethod
    def get(cls, task_id: int) -> Task:
        '''Devuelve un objeto Task desde la consulta a la base de datos'''
        res = cls.cur.execute(f'SELECT * FROM tasks WHERE id={task_id}')
        return cls.from_db_row(res.fetchone())
        #También se podría hacer new_id,new_name,new_done = res.fetchone() aunque habría que transformar posteriormente el done a bool (se tendría que quitar el row_factory)


class ToDo:
    '''Crear atributos de clase:
    - con: para la conexión a la base de datos. Establecer consultas como diccionarios.
    - cur: para el cursor de manejo.'''
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    def create_db(self):
        '''Crea la base de datos con los campos "id", "name" y "done"'''
        sql = '''CREATE TABLE tasks (
        id INTEGER PRIMARY KEY,
        name CHAR,
        done INTEGER'''
        ToDo.cur.execute(sql)
        ToDo.con.commit()

    def get_tasks(self, *, done: int = -1):
        '''Devuelve todas las tareas como objetos de tipo Task consultando la BBDD.
        - Si done = 0 se devuelven las tareas pendientes.
        - Si done = 1 se devuelven las tareas completadas.
        Ojo! Esto es una función generadora.'''
        for row in ToDo.cur.execute(f'SELECT * FROM tasks WHERE done={done}'):
            yield Task.from_db_row(row)

    def add_task(self, name: str):
        '''Añade la tarea con nombre "name"'''
        sql = f'''INSERT INTO
        tasks (name,done)
        VALUES ('{name}',0)'''
        ToDo.cur.execute(sql)
        ToDo.con.commit()

    def complete_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como completada'''
        ToDo.cur.execute(f'UPDATE tasks SET done=1 WHERE id={task_id}')
        ToDo.con.commit()

    def reopen_task(self, task_id: int):
        '''Marca la tarea con identificador "task_id" como pendiente'''
        ToDo.cur.execute(f'UPDATE tasks SET done=0 WHERE id={task_id}')
        ToDo.con.commit()
