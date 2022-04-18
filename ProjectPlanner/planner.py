from binascii import Incomplete
import csv
from collections import namedtuple
Task = namedtuple("Task", ["title", "duration", "prerequisites"])
def read_tasks(filename):
    tasks = {}
    for row in csv.reader(open(filename)):
        number = int(row[0])
        title = row[1]
        duration = float(row[2])
        prerequisites = set(map(int, row[3].split()))
        tasks[number] = Task(title, duration, prerequisites)
    return tasks

tasks = read_tasks("project.csv")
print(tasks)

def order_tasks(tasks):
    Incomplete = set(tasks)
    completed = set()
    start_days = {}
    while Incomplete:
        for task_number in Incomplete:
            task = tasks[task_number]
            if task.prerequisites.issubset(completed):
                earliest_start_day = 0
                for prereq_number in task.prerequisites:
                    