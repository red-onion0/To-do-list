import sys
from tabulate import tabulate
import csv


def main():
    # get tasks and with ctrl + D end that:
    tasks = []
    print("press ctrl-D when finished")
    while True:
        try:
            tasks.append(input("Task: "))
        except EOFError:
            break

    # make a csv file:
    with open("tasks.csv", "w",) as file:
        writer = csv.DictWriter(file, fieldnames=["tick", "task", "tag"])
        writer.writeheader()

        # write task in csv file:
        for task in tasks:
            writer.writerow({"tick": "unticked", "task": task, "tag": "None",})
    
    # load tasks:
    tasks=[]
    with open("tasks.csv",) as file:
        reader = csv.DictReader(file)
        for row in reader:

            # use Ballot Box ☐ for unticked
            if row["tick"] == "unticked":
                row["tick"] = "☐"

            # use Ballot Box with Check ☑ for ticked
            elif row["tick"] == "ticked":
                row["tick"] == "☑"
            
            tasks.append(row)

    # show tasks:
    print(tabulate(tasks, headers="keys", tablefmt="grid"))

if __name__ == "__main__":
    main()
