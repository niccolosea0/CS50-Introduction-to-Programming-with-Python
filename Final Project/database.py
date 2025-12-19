import sqlite3
from rich.console import Console
import datetime
from typing import List
from model import Todo


console = Console()
conn = sqlite3.connect("todos.db")

c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS todos (
              task TEXT,
              category TEXT,
              date_added TEXT,
              date_completed TEXT,
              status INT,
              position INT
              ) """)


create_table()


def insert_todo(todo: Todo):
    c.execute("SELECT COUNT(*) FROM todos")
    # Get number of rows we have (fetchone() retursn tuple, fetchone()[0] gets number)
    count = c.fetchone()[0]
    todo.position = count if count else 0

    with conn:
        c.execute("INSERT INTO todos VALUES(:task, :category, :date_added, :date_completed, :status, :position)",
                  {"task": todo.task, "category": todo.category, "date_added": todo.date_added, "date_completed": todo.date_completed,
                   "status": todo.status, "position": todo.position})


def delete_todo(position: int):
    c.execute("SELECT COUNT(*) FROM todos")
    count = c.fetchone()[0]

    check_position(position)

    with conn:
        c.execute("DELETE FROM todos WHERE position = :position", {"position": position})
        for pos in range(position + 1, count):
            change_position(pos, pos - 1, False)


def change_position(old_position: int, new_position: int, commit=True):

    with conn:
        c.execute("UPDATE todos SET position = :position_new WHERE position = :position_old",
                  {"position_new": new_position, "position_old": old_position})
    if commit:
        conn.commit()


def get_all_todos() -> List[Todo]:
    c.execute("SELECT * FROM todos")
    results = c.fetchall()
    todos = []

    for result in results:
        todos.append(Todo(*result))

    return todos


def update_todo(position: int, task: str = None, category: str = None):

    check_position(position)

    with conn:
        if task is not None and category is not None:
            c.execute("UPDATE todos SET task = :task, category = :category WHERE position = :position",
                      {"task": task, "category": category, "position": position})
        elif task is not None:
            c.execute("UPDATE todos SET task = :task WHERE position = :position",
                      {"task": task, "position": position})
        elif category is not None:
            c.execute("UPDATE todos SET category = :category WHERE position = :position",
                      {"category": category, "position": position})


def complete_todo(position: int):
    check_position(position)

    with conn:
        c.execute("UPDATE todos SET status = 2, date_completed = :date_completed WHERE position = :position",
                  {"date_completed": datetime.datetime.now().isoformat(), "position": position})


# Check's if provided position is valid or not
def check_position(position: int):
    c.execute("SELECT COUNT(*) FROM todos")
    count = c.fetchone()[0]

    if position < 0 or position >= count:
        console.print(f"[red]Error: no task at that position {position + 1}[/red]")
        return
