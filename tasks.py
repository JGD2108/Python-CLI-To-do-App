import json
from datetime import datetime

class Task:
    def __init__(self, name, description, due_date, completed=False, notes=""):
        self.name = name
        self.description = description
        self.due_date = due_date  # string format 'YYYY-MM-DD'
        self.completed = completed
        self.notes = notes

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "due_date": self.due_date,
            "completed": self.completed,
            "notes": self.notes
        }

    @staticmethod
    def from_dict(data):
        return Task(
            data["name"],
            data["description"],
            data["due_date"],
            data.get("completed", False),
            data.get("notes", "")
        )

class TaskManager:
    def sort_tasks(self, by="due_date"):
        if by == "due_date":
            self.tasks.sort(key=lambda t: t.due_date)
        elif by == "completed":
            self.tasks.sort(key=lambda t: t.completed)
        elif by == "name":
            self.tasks.sort(key=lambda t: t.name.lower())

    def export_tasks(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            for t in self.tasks:
                f.write(f"Name: {t.name}\nDescription: {t.description}\nDue: {t.due_date}\nCompleted: {t.completed}\nNotes: {t.notes}\n---\n")
    def __init__(self, tasks=None):
        self.tasks = tasks if tasks is not None else []

    def add_task(self, name, description, due_date):
        self.tasks.append(Task(name, description, due_date))

    def remove_task(self, name):
        self.tasks = [t for t in self.tasks if t.name != name]

    def edit_task(self, name, new_name=None, new_description=None, new_due_date=None):
        for t in self.tasks:
            if t.name == name:
                if new_name:
                    t.name = new_name
                if new_description:
                    t.description = new_description
                if new_due_date:
                    t.due_date = new_due_date
                return True
        return False

    def complete_task(self, name):
        for t in self.tasks:
            if t.name == name:
                t.completed = True
                return True
        return False

    def add_note(self, name, note):
        for t in self.tasks:
            if t.name == name:
                t.notes = note
                return True
        return False

    def remove_completed(self):
        self.tasks = [t for t in self.tasks if not t.completed]

    def list_tasks(self, show_completed=True):
        return [t.to_dict() for t in self.tasks if show_completed or not t.completed]

    def save_to_file(self, file_path, encrypt_func=None):
        data = json.dumps([t.to_dict() for t in self.tasks]).encode()
        if encrypt_func:
            data = encrypt_func(data)
        with open(file_path, 'wb') as f:
            f.write(data)

    def load_from_file(self, file_path, decrypt_func=None):
        with open(file_path, 'rb') as f:
            data = f.read()
        if decrypt_func:
            data = decrypt_func(data)
        tasks_list = json.loads(data.decode())
        self.tasks = [Task.from_dict(t) for t in tasks_list]
