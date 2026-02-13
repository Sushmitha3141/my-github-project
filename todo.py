tasks = []

def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)
def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
