import typer
from rich.console import Console
from rich.table import Table
from model import Todo
from database import insert_todo, delete_todo, get_all_todos, update_todo, complete_todo



console = Console()

app = typer.Typer()

def main():
    typer.echo("Welcome to the TODO List App (CLI)")
    app()


@app.command(short_help="adds an item")
def add(task: str, category: str):
    typer.echo("adding an item")
    todo = Todo(task, category)
    insert_todo(todo)
    show()


@app.command(short_help="deletes an item")
def delete(position: int):
    typer.echo("deleting an item")
    delete_todo(position - 1)
    show()


@app.command(short_help="updates an item")
def update(position: int, task: str = None, category: str = None):
    typer.echo("updating an item")
    update_todo(position - 1, task, category)
    show()


@app.command(short_help="completes an item")
def complete(position: int):
    typer.echo("completing an item")
    complete_todo(position - 1)
    show()


@app.command(short_help="shows a list of todos")
def show():
    tasks = get_all_todos()  # List of tasks
    console.print("[bold magenta]Todos[/bold magenta]!")

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Task", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category: str):
        COLORS = {"Study": "green", "Shopping": "cyan", "Working": "blue", "Sports": "yellow"}

        if category in COLORS:
            return COLORS[category]
        return "snow"

    for idx, task_row in enumerate(tasks, start=1):

        color = get_category_color(task_row.category)
        is_done = "✅" if task_row.status == 2 else "❌"

        table.add_row(str(idx), task_row.task, f"[{color}]{task_row.category}[/{color}]", is_done)

    console.print(table)


if __name__ == "__main__":
    main()
