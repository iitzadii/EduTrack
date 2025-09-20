import customtkinter as ctk,os,csv
from tkinter import messagebox, filedialog
from tkinter import ttk

# ------------------- Page 1: Login Selection -------------------
class MainPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Title Label
        title = ctk.CTkLabel(self, text="Login Page", font=("Arial", 18, "bold"))
        title.pack(pady=20)

        # Consistent button style
        btn_width = 180
        btn_height = 40

        ctk.CTkButton(
            self, text="Teacher Login", width=btn_width, height=btn_height,
            font=("Arial", 15),
            command=lambda: controller.show_frame("PasswordPage")
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Student Login", width=btn_width, height=btn_height,
            font=("Arial", 15),
            command=lambda: controller.show_frame("StudentLoginPage")
        ).pack(pady=10)

        ctk.CTkButton(
            self, text="Exit", width=btn_width, height=btn_height,
            font=("Arial", 15),
            command=controller.destroy
        ).pack(pady=10)


# ------------------- Page 2: Teacher Password -------------------
class PasswordPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label
        ctk.CTkLabel(self, text="Enter Password", font=("Arial", 15)).grid(row=0, column=0, padx=10, pady=20)

        # Entry box
        self.entry_password = ctk.CTkEntry(self, font=("Arial", 14), width=200, show="*")
        self.entry_password.grid(row=0, column=1, padx=10, pady=20)

        # Button
        ctk.CTkButton(
            self, text="Submit", width=150, height=35,
            font=("Arial", 15),
            command=self.submit_password
        ).grid(row=1, column=0, columnspan=2, pady=10)


    def submit_password(self):
        password = self.entry_password.get()
        if password == "aditya":
            self.controller.show_frame("MainMenuPage")
        else:
            messagebox.showerror("Error", "Wrong password")


# ------------------- Page 3: Student Login -------------------
class StudentLoginPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Student Login", font=("Arial", 18, "bold")).pack(pady=20)

        ctk.CTkButton(
            self, text="View Records", width=180, height=40,
            font=("Arial", 15),
            command=self.view_records
        ).pack(pady=20)

        # Back button
        ctk.CTkButton(
            self, text="Back to Login", width=180, height=40,
            font=("Arial", 15), command=lambda: controller.show_frame("MainPage")
        ).pack(pady=15)

    def view_records(self):
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            # here you’d show the "view_edit_window" frame instead of new Toplevel
            view_edit_window(file)

# ------------------- Main App Controller -------------------
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EduTrack")
        self.geometry("400x340")

        # container for all pages
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (MainPage, PasswordPage, StudentLoginPage,MainMenuPage,CreateFilePage):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.show_frame("MainPage")  # default page

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.lift()

# ------------------- Teacher Main Menu Page -------------------
class MainMenuPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Teacher Main Menu", font=("Arial", 18, "bold")).pack(pady=15)

        btn_width = 200
        btn_height = 40

        # View Records
        ctk.CTkButton(
            self, text="View Records", width=btn_width, height=btn_height,
            font=("Arial", 15), command=self.open_view_edit
        ).pack(pady=8)

        # Edit Records
        ctk.CTkButton(
            self, text="Edit Records", width=btn_width, height=btn_height,
            font=("Arial", 15), command=self.open_edit
        ).pack(pady=8)

        # Add Records
        ctk.CTkButton(
            self,
            text="Add Records",
            width=btn_width,
            height=btn_height,
            font=("Arial", 15),
            command=self.open_add_record
            ).pack(pady=8)

        # Create New Record File
        ctk.CTkButton(
            self, text="Create New Record File", width=btn_width, height=btn_height,
            font=("Arial", 15), command=lambda: controller.show_frame("CreateFilePage")
        ).pack(pady=8)

        # Back button
        ctk.CTkButton(
            self, text="Back to Login",
            font=("Arial", 15), command=lambda: controller.show_frame("MainPage")
        ).pack(pady=15)


    # ----------------- Actions -----------------
    def open_add_record(self):
        open_add_record_window()

    def open_view_edit(self):
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            view_edit_window(file)

    def open_edit(self):
        file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file:
            os.startfile(file)

    def create_new_file(self):
        # your create_new_record_file_window() will stay a popup
        messagebox.showinfo("New File", "New record file creation window will open.")


# ------------------- Improved View Records Window -------------------
def view_edit_window(filename):
    window = ctk.CTkToplevel()
    window.title("View Records")
    window.geometry("800x400")

    # Frame for Treeview + Scrollbars
    frame = ctk.CTkFrame(window)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Scrollbars
    vsb = ctk.CTkScrollbar(frame, orientation="vertical")
    vsb.pack(side="right", fill="y")
    hsb = ctk.CTkScrollbar(frame, orientation="horizontal")
    hsb.pack(side="bottom", fill="x")

    # Treeview
    columns = ("Name", "English", "Hindi", "Maths", "Science", "SST", "Percentage")
    tree = ttk.Treeview(frame, columns=columns, show="headings", yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center", width=100)  # fixed column width for better visibility

    tree.pack(fill="both", expand=True)

    # Attach scrollbars
    vsb.configure(command=tree.yview)
    hsb.configure(command=tree.xview)

    # Load CSV into table
    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                continue  # skip header row if already present
            tree.insert("", "end", values=row)

# ------------------- Create File Page -------------------
class CreateFilePage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ctk.CTkLabel(self, text="Enter filename:", font=("Arial", 14)).pack(pady=10)

        self.entry_filename = ctk.CTkEntry(self, font=("Arial", 14), width=300)
        self.entry_filename.pack(pady=10)

        ctk.CTkButton(
            self,
            text="Create File",
            font=("Arial", 14),
            command=self.create_file
        ).pack(pady=10)

        # Back button
        ctk.CTkButton(
            self, text="Back",
            font=("Arial", 15), command=lambda: controller.show_frame("MainMenuPage")
        ).pack(pady=15)

    def create_file(self):
        filename = self.entry_filename.get()
        if filename:
            if not filename.endswith('.csv'):
                filename += '.csv'

            script_dir = os.path.dirname(os.path.abspath(__file__))
            filepath = os.path.join(script_dir, filename)

            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Name", "English", "Hindi", "Maths", "Science", "SST", "Percentage"])

            messagebox.showinfo("Success", f"File '{filename}' created successfully in:\n{script_dir}")

            # Go back to main menu after success
            self.controller.show_frame("MainMenuPage")
        else:
            messagebox.showerror("Error", "Please enter a filename")

# ------------------- Create File Page -------------------
def open_add_record_window():
    file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file:  # only open if user selects a file
        window = ctk.CTkToplevel()
        app = StudentPerformanceMonitor(window)
        app.csv_filename = file
        window.grab_set()  # modal window

class StudentPerformanceMonitor:
    def __init__(self, master):
        self.master = master
        self.master.title("EduTrack")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.label_name = ctk.CTkLabel(master, text="Student Name:", font=("Arial", 15))
        self.label_name.grid(row=0, column=0, padx=10, pady=5)

        self.entry_name = ctk.CTkEntry(master, font=("Arial", 14), width=300)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5)

        self.label_marks1 = ctk.CTkLabel(master, text="Marks Obtained English:", font=("Arial", 14))
        self.label_marks1.grid(row=1, column=0, padx=10, pady=5)

        self.label_marks2 = ctk.CTkLabel(master, text="Marks Obtained Hindi:", font=("Arial", 14))
        self.label_marks2.grid(row=2, column=0, padx=10, pady=5)

        self.label_marks3 = ctk.CTkLabel(master, text="Marks Obtained Maths:", font=("Arial", 14))
        self.label_marks3.grid(row=3, column=0, padx=10, pady=5)

        self.label_marks4 = ctk.CTkLabel(master, text="Marks Obtained Science:", font=("Arial", 14))
        self.label_marks4.grid(row=4, column=0, padx=10, pady=5)

        self.label_marks5 = ctk.CTkLabel(master, text="Marks Obtained SST:", font=("Arial", 14))
        self.label_marks5.grid(row=5, column=0, padx=10, pady=5)

        self.entry_marks1 = ctk.CTkEntry(master, font=("Arial", 12), width=100)
        self.entry_marks1.grid(row=1, column=1, padx=10, pady=5)

        self.entry_marks2 = ctk.CTkEntry(master, font=("Arial", 12), width=100)
        self.entry_marks2.grid(row=2, column=1, padx=10, pady=5)

        self.entry_marks3 = ctk.CTkEntry(master, font=("Arial", 12), width=100)
        self.entry_marks3.grid(row=3, column=1, padx=10, pady=5)

        self.entry_marks4 = ctk.CTkEntry(master, font=("Arial", 12), width=100)
        self.entry_marks4.grid(row=4, column=1, padx=10, pady=5)

        self.entry_marks5 = ctk.CTkEntry(master, font=("Arial", 12), width=100)
        self.entry_marks5.grid(row=5, column=1, padx=10, pady=5)

        self.button_submit = ctk.CTkButton(master, text="Submit", font=("Arial", 15), command=self.submit)
        self.button_submit.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.text_output = ctk.CTkTextbox(master, height=300, width=500, font=("Arial", 12))
        self.text_output.grid(row=7, column=0, columnspan=2, padx=10, pady=5)
        self.text_output.configure(state=ctk.DISABLED)  # Make the display box read-only

    def submit(self):
        name = self.entry_name.get()
        marks1 = self.entry_marks1.get()
        marks2 = self.entry_marks2.get()
        marks3 = self.entry_marks3.get()
        marks4 = self.entry_marks4.get()
        marks5 = self.entry_marks5.get()
        
        if name and marks1 and marks2 and marks3 and marks4 and marks5:
            try:
                marks1 = float(marks1)
                marks2 = float(marks2)
                marks3 = float(marks3)
                marks4 = float(marks4)
                marks5 = float(marks5)

                if (0 <= marks1 <= 100 and 0 <= marks2 <= 100 and
                    0 <= marks3 <= 100 and 0 <= marks4 <= 100 and
                    0 <= marks5 <= 100):
                    
                    total_marks = marks1 + marks2 + marks3 + marks4 + marks5
                    percentage = (total_marks / 500) * 100

                    self.text_output.configure(state=ctk.NORMAL)  
                    self.text_output.insert(ctk.END, f"Name: {name}, Percentage: {percentage:.2f}%\n")
                    self.text_output.configure(state=ctk.DISABLED) 

                    self.write_to_csv(name, marks1, marks2, marks3, marks4, marks5, percentage)

                    self.entry_name.delete(0, ctk.END)
                    self.entry_marks1.delete(0, ctk.END)
                    self.entry_marks2.delete(0, ctk.END)
                    self.entry_marks3.delete(0, ctk.END)
                    self.entry_marks4.delete(0, ctk.END)
                    self.entry_marks5.delete(0, ctk.END)
                else:
                    messagebox.showerror("Error", "Marks should be between 0 and 100")
            except ValueError:
                messagebox.showerror("Error", "Marks should be a number")
        else:
            messagebox.showerror("Error", "Please enter both name and marks")

    def write_to_csv(self, name, marks1, marks2, marks3, marks4, marks5, percentage):
        if hasattr(self, 'csv_filename') and self.csv_filename:
            with open(self.csv_filename, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([name, marks1, marks2, marks3, marks4, marks5, percentage])
        else:
            messagebox.showerror("Error", "No file selected for saving records")

if __name__ == "__main__":
    app = App()
    app.mainloop()