 # Personal To-Do List Application
This project is a Personal To-Do List Application built using Python and the Tkinter library for the graphical user interface (GUI). It allows users to manage their tasks by adding, viewing, marking as completed, and deleting tasks. The application supports task categorization (e.g., Work, Personal, Urgent) and saves tasks locally in a tasks.json file, enabling persistence between sessions.

 # Features :

  1. Add Tasks: Users can input a task title, description, and select a category from predefined options.
  2. Mark as Completed: Users can select a task from the list and mark it as completed.
  3. Delete Tasks: Users can remove tasks from the list.
  4. Task Categories: Tasks can be categorized as "Work", "Personal", "Urgent", or "Other".
  5. Task Status: Tasks are marked as ✔️ (completed) or ❌ (pending).
  6. Persistence: All tasks are saved in tasks.json to ensure that progress is not lost between application runs.
  7. Simple and Interactive GUI: The application is easy to use with an intuitive interface and responsive controls.

 # Project Structure: 

   /todo_app
   ├── todo.py         # Main application code (GUI + logic)
   ├── tasks.json      # File to store tasks (created after first run)
   ├── README.md       # Documentation file

 # Installation :
   Prerequisites
    
   .  Python 3.x must be installed on your system. You can download Python from here.
   
   .  The Tkinter library is part of the Python Standard Library, so no external installations are required for it.


 # Steps to Install and Run:

    1. Clone or Download the repository containing this project.
    2. Open a terminal or command prompt and navigate to the project directory.
    3. Run the application by executing the following command:

                                          python todo.py
The To-Do List GUI will appear, allowing you to manage your tasks.

 # Usage
 
  Main Features:
  
 1. Adding a Task:

   .  Enter the Task Title and Description in the provided text fields.
   
   .  Select a Category from the dropdown menu (Work, Personal, Urgent, Other).
   
   .  Click the "Add Task" button to add the task to the list.

 2. Marking a Task as Completed:

   .  Select a task from the list by clicking on it.
   
   .  Click the "Mark Completed" button. The task’s status will be updated to ✔️.

 3. Deleting a Task:

   .  Select a task from the list.
   
   .  Click the "Delete Task" button to remove it.

 4.  Saving and Exiting:

    . Click the "Save and Exit" button to save the current task list and close the application. The tasks are saved to  (tasks.json).

 # Interface Overview:

     1.   Task List: Displays tasks along with their categories and completion status.
     
     2.  Input Fields: Allows the user to enter task details (title, description) and choose a category.
     
     3.  Buttons:

                .    Add Task: Adds the task to the list.
                .    Mark Completed: Marks the selected task as completed.
                .    Delete Task: Deletes the selected task.
                .    Save and Exit: Saves the current tasks and exits the application.

 # Data Persistence :
   All tasks are stored in a local file called tasks.json. When you add, delete, or mark tasks as completed, this file is updated. The next time you open the application, tasks are 
    loaded from this file so you can continue where you left off.

 # Customization : 
        You can easily modify this application to suit your needs:

       . Categories: Add or remove categories by modifying the category_options list in the code.
       
       . Task Display: Change how tasks are represented in the Listbox by modifying the __repr__ method in the Task class.               

 # Example Task JSON Structure
 
       Here is an example of how tasks are stored in tasks.json:
       

       [
    {
        "title": "Finish project report",
        "description": "Complete the final report for the work project.",
        "category": "Work",
        "completed": false
    },
    {
        "title": "Grocery shopping",
        "description": "Buy milk, eggs, and bread.",
        "category": "Personal",
        "completed": true
    }
 ]

 # Future Enhancements :
 Some potential improvements that could be made to this project:

   1.  Task Sorting: Allow users to sort tasks by title, category, or completion status.
   2.  Task Editing: Implement functionality to edit existing tasks.
   3.  Due Dates: Add due dates to tasks for better tracking.
   4.  Notification System: Notify the user when a task is due soon or overdue.


  # License
  
    This project is licensed under the MIT License. You are free to use, modify, and distribute it.
