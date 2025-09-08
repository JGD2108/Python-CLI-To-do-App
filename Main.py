from Users import Users
from tasks import TaskManager

# Simple i18n system
LANGS = {
    'en': {
        'register': 'Register',
        'login': 'Login',
        'exit': 'Exit',
        'choose_option': 'Choose an option: ',
        'user_registered': 'User registered successfully.',
        'username_exists': 'Username already exists.',
        'invalid_user_pass': 'Invalid username or password.',
        'login_success': 'Login successful.',
        'task_menu': 'Task Menu:',
        'add_task': 'Add Task',
        'edit_task': 'Edit Task',
        'complete_task': 'Complete Task',
        'add_note': 'Add/Edit Note',
        'delete_task': 'Delete Task',
        'delete_completed': 'Delete All Completed Tasks',
        'list_tasks': 'List Tasks',
        'sort_tasks': 'Sort Tasks',
        'export_tasks': 'Export Tasks',
        'logout': 'Logout',
        'task_name': 'Task name: ',
        'description': 'Description: ',
        'due_date': 'Due date (YYYY-MM-DD): ',
        'task_added': 'Task added.',
        'task_edited': 'Task edited.',
        'task_completed': 'Task marked as completed.',
        'task_not_found': 'Task not found.',
        'note': 'Note: ',
        'note_added': 'Note added/edited.',
        'task_deleted': 'Task deleted.',
        'all_deleted': 'All completed tasks deleted.',
        'no_tasks': 'No tasks found.',
        'sort_by': 'Sort by: 1) Due Date 2) Completed 3) Name',
        'tasks_sorted': 'Tasks sorted.',
        'export_file': 'Enter export file name (e.g. export.txt): ',
        'exported': 'Tasks exported to',
        'export_failed': 'Export failed:',
        'logged_out': 'Logged out.',
        'invalid_option': 'Invalid option. Please try again.',
        'exiting': 'Exiting... (KeyboardInterrupt)',
        'exiting_menu': 'Exiting task menu... (KeyboardInterrupt)'
    },
    'es': {
        'register': 'Registrar',
        'login': 'Iniciar sesión',
        'exit': 'Salir',
        'choose_option': 'Elige una opción: ',
        'user_registered': 'Usuario registrado exitosamente.',
        'username_exists': 'El nombre de usuario ya existe.',
        'invalid_user_pass': 'Usuario o contraseña inválidos.',
        'login_success': 'Inicio de sesión exitoso.',
        'task_menu': 'Menú de tareas:',
        'add_task': 'Añadir tarea',
        'edit_task': 'Editar tarea',
        'complete_task': 'Completar tarea',
        'add_note': 'Añadir/Editar nota',
        'delete_task': 'Eliminar tarea',
        'delete_completed': 'Eliminar todas completadas',
        'list_tasks': 'Listar tareas',
        'sort_tasks': 'Ordenar tareas',
        'export_tasks': 'Exportar tareas',
        'logout': 'Cerrar sesión',
        'task_name': 'Nombre de la tarea: ',
        'description': 'Descripción: ',
        'due_date': 'Fecha máxima (YYYY-MM-DD): ',
        'task_added': 'Tarea añadida.',
        'task_edited': 'Tarea editada.',
        'task_completed': 'Tarea marcada como completada.',
        'task_not_found': 'Tarea no encontrada.',
        'note': 'Nota: ',
        'note_added': 'Nota añadida/editada.',
        'task_deleted': 'Tarea eliminada.',
        'all_deleted': 'Todas las tareas completadas eliminadas.',
        'no_tasks': 'No hay tareas.',
        'sort_by': 'Ordenar por: 1) Fecha máxima 2) Completadas 3) Nombre',
        'tasks_sorted': 'Tareas ordenadas.',
        'export_file': 'Nombre del archivo de exportación (ej. export.txt): ',
        'exported': 'Tareas exportadas a',
        'export_failed': 'Exportación fallida:',
        'logged_out': 'Sesión cerrada.',
        'invalid_option': 'Opción inválida. Intenta de nuevo.',
        'exiting': 'Saliendo... (KeyboardInterrupt)',
        'exiting_menu': 'Saliendo del menú de tareas... (KeyboardInterrupt)'
    }
}

def get_text(key):
    return LANGS[LANG][key]

LANG = 'es'  # Cambia a 'en' para inglés


def register(users):
    username = input(get_text('register') + " username: ")
    while True:
        password = input(get_text('register') + " password: ")
        if not users.is_strong_password(password):
            print(get_text('invalid_option'), "Password must be at least 8 characters, include a number, an uppercase and a lowercase letter.")
        else:
            break
    try:
        if users.add_user(username, password):
            users.create_encrypted_user_file(username, password, b"[]")
            print(get_text('user_registered'))
        else:
            print(get_text('username_exists'))
    except Exception as e:
        print(f"{get_text('invalid_option')} {e}")

def login(users):
    username = input(get_text('login') + " username: ")
    password = input(get_text('login') + " password: ")
    try:
        if not users.verify_user(username, password):
            print(get_text('invalid_user_pass'))
            return
        print(get_text('login_success'))
        data = users.read_encrypted_user_file(username, password)
        if data is None:
            print(get_text('invalid_option'), "Could not load tasks file. Wrong password or file missing.")
            return
        task_manager = TaskManager()
        try:
            task_manager.load_from_file(users.get_user_file_path(username),
                                       lambda d: users.read_encrypted_user_file(username, password))
        except Exception as e:
            print(f"{get_text('invalid_option')} {e}")
            task_manager.tasks = []
        task_menu(users, task_manager, username, password)
    except Exception as e:
        print(f"{get_text('invalid_option')} {e}")

def task_menu(users, task_manager, username, password):
    try:
        while True:
            print(f"\n{get_text('task_menu')}")
            print(f"1. {get_text('add_task')}")
            print(f"2. {get_text('edit_task')}")
            print(f"3. {get_text('complete_task')}")
            print(f"4. {get_text('add_note')}")
            print(f"5. {get_text('delete_task')}")
            print(f"6. {get_text('delete_completed')}")
            print(f"7. {get_text('list_tasks')}")
            print(f"8. {get_text('sort_tasks')}")
            print(f"9. {get_text('export_tasks')}")
            print(f"10. {get_text('logout')}")
            t_choice = input(get_text('choose_option'))

        if t_choice == '1':
            name = input(get_text('task_name'))
            desc = input(get_text('description'))
            due = input(get_text('due_date'))
            task_manager.add_task(name, desc, due)
            print(get_text('task_added'))
        elif t_choice == '2':
            name = input(get_text('edit_task') + " (name): ")
            new_name = input(get_text('edit_task') + " (new name, blank to keep): ")
            new_desc = input(get_text('edit_task') + " (new description, blank to keep): ")
            new_due = input(get_text('edit_task') + " (new due date, blank to keep): ")
            task_manager.edit_task(name,
                                  new_name if new_name else None,
                                  new_desc if new_desc else None,
                                  new_due if new_due else None)
            print(get_text('task_edited'))
        elif t_choice == '3':
            name = input(get_text('complete_task') + " (name): ")
            if task_manager.complete_task(name):
                print(get_text('task_completed'))
            else:
                print(get_text('task_not_found'))
        elif t_choice == '4':
            name = input(get_text('add_note') + " (name): ")
            note = input(get_text('note'))
            if task_manager.add_note(name, note):
                print(get_text('note_added'))
            else:
                print(get_text('task_not_found'))
        elif t_choice == '5':
            name = input(get_text('delete_task') + " (name): ")
            task_manager.remove_task(name)
            print(get_text('task_deleted'))
        elif t_choice == '6':
            task_manager.remove_completed()
            print(get_text('all_deleted'))
        elif t_choice == '7':
            tasks = task_manager.list_tasks()
            if not tasks:
                print(get_text('no_tasks'))
            else:
                print("\n--- TASK LIST ---")
                for idx, t in enumerate(tasks, 1):
                    status = "✅" if t['completed'] else "❌"
                    print(f"[{idx}] {status} {t['name']}")
                    print(f"    {get_text('description')} {t['description']}")
                    print(f"    {get_text('due_date')} {t['due_date']}")
                    if t['notes']:
                        print(f"    {get_text('note')} {t['notes']}")
                    print("    ---------------------------")
        elif t_choice == '8':
            print(get_text('sort_by'))
            sort_choice = input(get_text('choose_option'))
            if sort_choice == '1':
                task_manager.sort_tasks("due_date")
            elif sort_choice == '2':
                task_manager.sort_tasks("completed")
            elif sort_choice == '3':
                task_manager.sort_tasks("name")
            print(get_text('tasks_sorted'))
        elif t_choice == '9':
            export_path = input(get_text('export_file'))
            try:
                task_manager.export_tasks(export_path)
                print(f"{get_text('exported')} {export_path}")
            except Exception as e:
                print(f"{get_text('export_failed')} {e}")
        elif t_choice == '10':
            def encrypt_data(data):
                users.write_encrypted_user_file(username, password, data)
                return data
            task_manager.save_to_file(users.get_user_file_path(username), encrypt_data)
            print(get_text('logged_out'))
            return
        else:
            print(get_text('invalid_option'))
    except KeyboardInterrupt:
        print("\nExiting task menu... (KeyboardInterrupt)")

def main():
    users = Users()
    try:
        while True:
            print(f"1. {get_text('register')}")
            print(f"2. {get_text('login')}")
            print(f"3. {get_text('exit')}")
            choice = input(get_text('choose_option'))
            if choice == '1':
                register(users)
            elif choice == '2':
                login(users)
            elif choice == '3':
                break
            else:
                print(get_text('invalid_option'))
    except KeyboardInterrupt:
        print(f"\n{get_text('exiting')}")

if __name__ == "__main__":
    main()