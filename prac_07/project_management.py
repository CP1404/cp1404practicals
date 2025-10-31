"""
CP1404/CP5632 Practical 07 - Project Management Program.
Allows user to load projects, display by status, filter by date, add new projects, update projects, and save to file.
Estimate: 20 min
Actual: 30 min
"""
import datetime
from project import Project

MENU = """Menu:
[L] - Load projects  
[S] - Save projects  
[D] - Display projects  
[F] - Filter projects by date  
[A] - Add new project  
[U] - Update project  
[Q] - Quit
"""

FILENAME = "projects.txt"

def main():
    projects = []
    header = ""
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != 'Q':
        if choice == 'L':
            try:
                filename = input("Filename to load (press Enter for default projects.txt): ").strip()
                if filename == "":
                    filename = FILENAME
                projects, header = load_projects(filename)
                print(f"{len(projects)} projects loaded from {filename}.")
            except FileNotFoundError:
                print("File not found. Please ensure the file exists.")
        elif choice == 'S':
            filename = input("Filename to save to (press Enter for default projects.txt): ").strip()
            if filename == "":
                filename = FILENAME
            save_projects(filename, projects, header)
            print(f"{len(projects)} projects saved to {filename}.")
        elif choice == 'D':
            display_projects(projects)
        elif choice == 'F':
            date_string = input("Show projects that start after date (dd/mm/yyyy): ").strip()
            try:
                filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            except ValueError:
                print("Invalid date format. Please use dd/mm/yyyy.")
            else:
                show_filtered_projects(projects, filter_date)
        elif choice == 'A':
            name = input("Project name: ").strip()
            if name == "":
                print("Project name cannot be blank.")
            else:
                start_date = get_valid_date("Start date (dd/mm/yyyy): ")
                priority = get_valid_int("Priority: ")
                cost_estimate = get_valid_float("Cost estimate: $")
                completion = get_valid_int("Completion percentage: ")
                new_project = Project(name, start_date, priority, cost_estimate, completion)
                projects.append(new_project)
                print(f"Project '{new_project.name}' added.")
        elif choice == 'U':
            if not projects:
                print("No projects to update. Please load or add projects first.")
            else:
                incomplete_projects = [p for p in projects if not p.is_complete()]
                if not incomplete_projects:
                    print("No incomplete projects to update.")
                else:
                    incomplete_projects.sort()
                    print("Incomplete projects:")
                    for i, proj in enumerate(incomplete_projects):
                        print(f"{i} - {proj}")
                    index = get_valid_int("Project number to update: ")
                    if 0 <= index < len(incomplete_projects):
                        project_to_update = incomplete_projects[index]
                        new_percentage = get_valid_int("New completion percentage: ")
                        new_priority = get_valid_int("New priority: ")
                        project_to_update.completion_percentage = new_percentage
                        project_to_update.priority = new_priority
                        print(f"Project '{project_to_update.name}' updated (priority {new_priority}, completion {new_percentage}%).")
                    else:
                        print("Invalid project number.")
        else:
            print("Invalid menu choice.")
        print()
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Goodbye!")

def load_projects(filename):
    projects = []
    with open(filename, 'r') as file:
        header_line = file.readline().strip()
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split('\t')
            name = parts[0]
            start_date_str = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion = int(parts[4])
            start_date = datetime.datetime.strptime(start_date_str, "%d/%m/%Y").date()
            project = Project(name, start_date, priority, cost_estimate, completion)
            projects.append(project)
    return projects, header_line

def save_projects(filename, projects, header_line):
    with open(filename, 'w') as file:
        print(header_line, file=file)
        for project in projects:
            start_date_str = project.start_date.strftime("%d/%m/%Y")
            print(f"{project.name}\t{start_date_str}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=file)

def display_projects(projects):
    if not projects:
        print("No projects to display. Please load or add projects first.")
        return
    incomplete_projects = [p for p in projects if not p.is_complete()]
    completed_projects = [p for p in projects if p.is_complete()]
    incomplete_projects.sort()
    completed_projects.sort()
    print("Incomplete projects:")
    for i, project in enumerate(incomplete_projects):
        print(f"  {i}. {project}")
    print("Completed projects:")
    for i, project in enumerate(completed_projects):
        print(f"  {i}. {project}")

def show_filtered_projects(projects, date_after):
    filtered_projects = [p for p in projects if p.start_date > date_after]
    if not filtered_projects:
        print(f"No projects start after {date_after.strftime('%d/%m/%Y')}.")
    else:
        filtered_projects.sort(key=lambda proj: proj.start_date)
        print(f"Projects starting after {date_after.strftime('%d/%m/%Y')}:")
        for project in filtered_projects:
            print(f"  {project.name}, start: {project.start_date.strftime('%d/%m/%Y')}, priority {project.priority}, cost: ${project.cost_estimate:.2f}, completion: {project.completion_percentage}%")

def get_valid_date(prompt):
    while True:
        date_str = input(prompt).strip()
        try:
            return datetime.datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            print("Invalid date format. Please enter date as dd/mm/yyyy.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")

def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input; enter a valid number.")

if __name__ == "__main__":
    main()
