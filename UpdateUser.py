import hashlib
import getpass

users_db = {}  
tasks_db = {} 

def secure_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
   
    username = input("Enter username: ").strip()
  
    if username in users_db:
        print("This username Exists, Create New User")
        return
   
    password = getpass.getpass("Enter your password: ").strip()
    users_db[username] = secure_password(password)
    tasks_db[username] = []  
    
    print(f"Registration successful! Welcome, {username}.")

def login_user():
    
    username = input("Enter your username: ").strip()
    password = getpass.getpass("Enter your password: ").strip()

    if username in users_db and users_db[username] == secure_password(password):
        print(f"Welcome User, {username}!")
        return username  
    else:
        print("Invalid credentials")
        return None  

def add_task_for_user(username):
   
    task_description = input("Enter the task description: ").strip()
   
    task_id = len(tasks_db[username]) + 1
   
    task = {"id": task_id, "description": task_description, "completed": False}
   
    tasks_db[username].append(task)
    
    print(f"Task added successfully: {task_description}")

def display_user_tasks(username):
    user_tasks = tasks_db.get(username, [])
    
    if not user_tasks:
        print("You don't have any tasks yet.")
        return
   
    for task in user_tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f"{task['id']}. {task['description']} - {status}")

def mark_task_as_done(username):
   
    display_user_tasks(username)
    
    try:
       
        task_id = int(input("Enter the task ID to mark completed: "))
      
        for task in tasks_db[username]:
            if task["id"] == task_id:
                task["completed"] = True
                print("Task marked as completed")
                return
        
        print("Task ID not found.")
    
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def delete_user_task(username):
    
    display_user_tasks(username)
    
    try:
        
        task_id = int(input("Enter the task ID to delete: "))
       
        tasks_db[username] = [task for task in tasks_db[username] if task["id"] != task_id]
       
        for idx, task in enumerate(tasks_db[username], start=1):
            task["id"] = idx
        
        print("Task deleted successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a valid task ID.")

def main():
    print("Welcome to the Task Management System!")
    
    while True:
        print("\nOptions:\n1. Register\n2. Login\n3. Exit")
        user_choice = input("Choose an option: ").strip()
        
        if user_choice == "1":
            register_user()  
        elif user_choice == "2":
            username = login_user()  
            
            if username:
              
                while True:
                    print("\nTask Options:\n1. Add Task\n2. View Tasks\n3. Mark Task as Completed\n4. Delete Task\n5. Logout")
                    action_choice = input("Choose an action: ").strip()
                    
                    if action_choice == "1":
                        add_task_for_user(username)
                    elif action_choice == "2":
                        display_user_tasks(username)
                    elif action_choice == "3":
                        mark_task_as_done(username)
                    elif action_choice == "4":
                        delete_user_task(username)
                    elif action_choice == "5":
                        print(f"{username}! You have been logged out.")
                        break
                    else:
                        print("Invalid option. Please try again.")
        elif user_choice == "3":
            print("Exiting the Task Management System")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
