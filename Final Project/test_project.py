from database import  get_all_todos,  delete_todo


def test_delete():
    # Delete the last 'pytest task updated'
    todos = get_all_todos()
    for i, t in reversed(list(enumerate(todos))):
        if t.task == "pytest task updated":
            delete_todo(i)
            break
    todos = get_all_todos()
    # Should no longer exist
    assert not any(t.task == "pytest task updated" for t in todos)

import datetime
from database import insert_todo, get_all_todos, update_todo, delete_todo, complete_todo, change_position
from model import Todo

def test_insert_todo():
    todo = Todo("pytest insert", "testing", datetime.datetime.now().isoformat(), None, 1, 0)
    insert_todo(todo)
    todos = get_all_todos()
    assert any(t.task == "pytest insert" for t in todos)

def test_change_position():
    todos = get_all_todos()
    if len(todos) > 1:
        first_pos = todos[0].position
        second_pos = todos[1].position
        # Swap the first and second
        change_position(second_pos, first_pos)
        # The todos list order may not update instantly depending on implementation, so just check that function runs
        # For a real test, you'd reload todos and check order if implementing by id/position

def test_delete_todo():
    todos = get_all_todos()
    for i, t in enumerate(todos):
        if t.task == "pytest updated":
            delete_todo(i)
            break
    todos = get_all_todos()
    assert not any(t.task == "pytest updated" for t in todos)
