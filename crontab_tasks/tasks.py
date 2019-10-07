from crontab_tasks.celery import app
import json

@app.task
def remember_tasks_to_do():
    file_object = open('employees.json', 'r')
    # Load JSON file data to a list of python dict object.
    employees_list = json.load(file_object)
    for each_employee in employees_list:
        print("Good morning %s. This is your list of tasks to do %s"%(each_employee.get('username'),each_employee.get('tasks')))
