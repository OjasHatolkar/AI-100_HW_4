class Task:
    
    def __init__(self, name, description, due_date):
        self.name = name
        self.description = description
        self.due_date = due_date
        self.progress = 0
    
    def update_progress(self, total_progress):
        self.progress = self.total_progress

    def __str__(self):
        if self.progress >= 100:
            return "completed"
        s = "Task Name: " + self.name + "\nTask Description: " + self.description + "\nDue Date/Time Left: " + self.due_date + "\nProgress (from 0-100): " + str(self.progress)
        return s