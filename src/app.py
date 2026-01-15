class Task:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

tasks = []

def create_task(title, description):
    task_id = len(tasks) + 1
    task = Task(task_id, title, description)
    tasks.append(task)
    return task

def get_tasks():
    return tasks

def update_task(task_id, title, description):
    for task in tasks:
        if task.id == task_id:
            task.title = title
            task.description = description
            return task
    return None

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
