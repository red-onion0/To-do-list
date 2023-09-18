import sys
from tabulate import tabulate
import csv


def main():
    # get tasks and with ctrl + D end that:
    tasks = get_tasks()

    # write tasks:
    write_tasks("tasks.csv", tasks)
    
    # read tasks:
    tasks = read_tasks("tasks.csv")

    # show tasks:
    print(tabulate(tasks, tablefmt="grid"))


def get_tasks():
    tasks = []
    print("press ctrl-D when finished")
    while True:
        try:
            tasks.append(input("Task: "))
        except EOFError:
            break
    return tasks


def write_tasks(file_path, tasks):
    with open(file_path, "w",) as file:
        writer = csv.DictWriter(file, fieldnames=["tick", "task", "tag"])
        writer.writeheader()
        for task in tasks:
            writer.writerow({"tick": "unticked", "task": task, "tag": "None",})


def read_tasks(file_path):
    tasks=[]
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:

            # use Ballot Box ☐ for unticked
            if row["tick"] == "unticked":
                row["tick"] = "☐"

            # use Ballot Box with Check ☑ for ticked
            elif row["tick"] == "ticked":
                row["tick"] == "☑"
            
            tasks.append(row)
    return tasks


if __name__ == "__main__":
    main()
