# Imports
from Task import Task
from dotenv import load_dotenv
import os
from google import genai

# Load Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
print(api_key)
client = genai.Client(api_key=api_key)

# Dictionaries
task_names = {}
task_list = {}

# Functions
def get_query(task_name):
    task = task_names[task_name]
    query = "For the following task, return a priority value from a range of 0-100 (where 0 is lowest priority and 100 is highest priority):\n" + str(task) + "\n"
    query = query + "\nHere is a list of other tasks that must also be completed:\n"
    for name in task_names.keys():
        if name != task_name:
            query = query + "\n" + str(task_names[name]) + "\n"
    query = query + "NOTE: PLEASE RETURN ONLY AN INTEGER VALUE FROM 0 (INCLUSIVE) TO 100 (INCLUSIVE) FOR THE PRIORITY OF THE TASK"
    return query

def get_priority(task_name):

    prompt = get_query(task_name)

    response = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt
    )  

    result = response.text.strip()

    if result.strip("-").isdigit():
        return int(result)
    else:
        return 0

def add_task(name, description, due_date):
    task = Task(name, description, due_date)
    task_names[name] = task
    task_list[task] = get_priority(name)

def get_priority_list():
    try:
        return sorted(task_list, key=lambda k: task_list[k], reverse=True)
    except TypeError as e:
        raise ValueError(f"Dictionary values must be comparable: {e}")

# Main Functionality

# Functions that the user can use
# 1 - Create new task
# 2 - Edit progress for existing task
# 3 - Get priority list

while(True):
    print("Enter a number to select a task:\n\t1: Create a new task\n\t2: Change progress for an existing task\n\t3: Get priority list for tasks")
    choice = input("> ")
    print()
    match choice:
        case "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date or time left: ")
            add_task(name, description, due_date)
        case "2":
            name = input("Enter task name: ")
            if name in task_names.keys():
                progress = input("Enter new progress for " + name + ": ")
                task_names[name].update_progress(progress)
            else:
                print("That task does not exist")
        case "3":
            task_priority_list = get_priority_list()
            print("Tasks from highest to lowest priority:\n")
            for task in task_priority_list:
                print(str(task) + "\n")
        case _:
            print("Invalid Choice")
    print()