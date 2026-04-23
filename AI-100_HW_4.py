#NOTE: PLEASE RETURN AN INTEGER VALUE FROM 0 (INCLUSIVE) TO 100 (INCLUSIVE) FOR THE PRIORITY OF THE TASK
from Task import Task

task_names = {}
task_list = {}

def get_query(task_name):
    task = task_names[task_name]
    query = "For the following task, return a priority value from a range of 0-100 (where 0 is lowest priority and 100 is highest priority):\n" + str(task) + "\n"
    query = query + "\nHere is a list of other tasks that must also be completed:\n"
    for name in task_names.keys():
        if name != task_name:
            query = query + "\n" + str(task_names[name]) + "\n"
    return query



task_1 = Task("AI 100 HW", "Gemini API", "1/1/1")
task_2 = Task("Math HW", "Matrices", "2/2/2")
task_3 = Task("Phys HW", "Electricity", "2/2/2")

task_names["AI 100 HW"] = task_1
task_names["MATH HW"] = task_2
task_names["Phys HW"] = task_3

print(get_query("AI 100 HW"))