import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) == 3 and sys.argv[1] in ["-m", "--mark"]:
        
        # read tasks from file:
        file_data = read_tasks("tasks.csv")

        # change tasks:
        modified_data = tick_task(sys.argv[2], file_data)

        # write tasks in file:
        write_tasks("tasks.csv", modified_data, file_exist=True)

        # show the changes:
        print(show_tasks("tasks.csv"))

    if len(sys.argv) == 2 and sys.argv[1] in ["-n", "--new"]:
        # get tasks and with ctrl + D end that:
        tasks = get_tasks()

        # write tasks:
        write_tasks("tasks.csv", tasks)
        
        # read tasks:
        tasks = read_tasks("tasks.csv")

        # show tasks:
        print(show_tasks("tasks.csv")) 


def tick_task(task, tasks):
        counter = 0
        for row in tasks:
            if row["task"] == task:
                row["tick"] = "ticked"
                tasks.pop(counter)
                tasks.insert(counter, row)
                return tasks
            counter += 1


def get_tasks():
    tasks = []
    print("press ctrl-D when finished")
    while True:
        try:
            tasks.append(input("Task: "))
        except EOFError:
            break
    return tasks


def write_tasks(file_path, tasks, file_exist=False):
    with open(file_path, "w",) as file:
        writer = csv.DictWriter(file, fieldnames=["tick", "task", "tag"])
        writer.writeheader()

        # if file exist just update the changes
        if file_exist:
            for row in tasks:
                writer.writerow({"tick": row["tick"], "task": row["task"], "tag": row["tag"],})
        
        # if it's a new file defult value for tick and tag and just write tasks in file
        else:
            for task in tasks:
                writer.writerow({"tick": "unticked", "task": task, "tag": "None",})


def read_tasks(file_path):
    tasks=[]
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            tasks.append(row)
    return tasks


def show_tasks(file_path):
    file_data = read_tasks(file_path)
    modified_data = []
    for row in file_data:

        # use Ballot Box ☐ for unticked
        if row["tick"] == "unticked":
            row["tick"] = "☐"

        # use Ballot Box with Check ☑ for ticked
        elif row["tick"] == "ticked":
            row["tick"] = "☑"

        modified_data.append(row)
    
    return tabulate(modified_data, tablefmt="grid")



if __name__ == "__main__":
    main()
