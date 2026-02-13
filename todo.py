tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)

add_task("Sample Task")
view_tasks()

def mark_complete(index):
    if 0 <= index < len(tasks):
        tasks[index] = tasks[index] + " (Done)"
