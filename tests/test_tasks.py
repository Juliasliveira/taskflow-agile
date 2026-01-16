import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app import create_task, get_tasks, update_task, delete_task

def test_create_task():
    task = create_task("Estudar", "Revisar Engenharia de Software", "Alta")
    assert task.priority == "Alta"
    assert len(get_tasks()) == 1

def test_update_task():
    task = update_task(1, "Estudar Python", "Revisar Pytest", "Média")
    assert task.priority == "Média"

def test_delete_task():
    delete_task(1)
    assert len(get_tasks()) == 0
