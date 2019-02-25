import tkinter as tk
from tkinter.filedialog import askopenfilename
#import threading
from subjectwise_passed_percent import subjectwise_passed_percentage
from subjectwise_grades import by_grade
from semester_comparision import compare

appcolor = "#4123d8"
class PEC(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("PEC_ANALYTICS")
        self.iconbitmap('1030.ico')

        container = tk.Frame(self, bg='white')
        container.pack(side=tk.TOP, fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # The following variable stores all the frame pages of the app
        self.frames = {}

        # main_window_blue is the page which contains widgets to run the application
        frame = main_window_blue(container, self)
        self.frames[main_window_blue] = frame
        frame.grid(row=0, column=0, sticky = 'nsew')

        frame1 = subject_wise_pass(container, self)
        self.frames[subject_wise_pass] = frame1
        frame1.grid(row=0, column=0, sticky = 'nsew')

        frame2 = subject_wise_grade(container, self)
        self.frames[subject_wise_grade] = frame2
        frame2.grid(row=0, column=0, sticky = 'nsew')

        frame3 = semester_comparision(container, self)
        self.frames[semester_comparision] = frame3
        frame3.grid(row=0, column=0, sticky = 'nsew')

        frame4 = select_semesters(container, self)
        self.frames[select_semesters] = frame4
        frame4.grid(row=0, column=0, sticky = 'nsew')

        # the following call puts the main_window_blue page as the visible frame of PEC APP
        self.show_frame(main_window_blue)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class main_window_blue(tk.Frame):
    # below 3 lines are common
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.can = tk.Canvas(self, bg='blue', height = 800, width = 2000, relief = tk.RAISED)

        # My Widgets
        self.functionality = tk.StringVar()

        self.OPTIONS = ["Subjectwise Pass% of Students", "Subjectwise Grades",  "Performance in Previous Semesters"     ]
        self.functionality.set("Select a Analysis") # default value
        self.functionality_box = tk.OptionMenu(self.can, self.functionality, *self.OPTIONS)
        self.functionality_box.configure(font=("Helvetica",15))
        self.functionality_box.pack()
        self.functionality_box.place(relx=0.270, rely=0.4, height=44, relwidth=0.49)
        #self.functionality_name = self.functionality.get()
        #self.functionality_box.place(x=280, y=300)

        self.button = tk.Button(self.can, text="Select",font=("Helvetica",15), command = self.ok, bg= "red")
        self.button.pack()
        self.button.place(relx=0.400, rely=0.520, height=44, relwidth=0.25)

        self.can.pack(side=tk.TOP)

    def ok(self):
        print ("value is:" + self.functionality.get())
        global functionality_name
        functionality_name = self.functionality.get()
        if(functionality_name == "Subjectwise Pass% of Students"):
            self.controller.show_frame(subject_wise_pass)
        elif(functionality_name == "Subjectwise Grades"):
            self.controller.show_frame(subject_wise_grade)
        elif(functionality_name == "Performance in Previous Semesters"):
            self.controller.show_frame(semester_comparision)

class subject_wise_pass(tk.Frame):

    def __init__(self, parent, controller):
        #PEC.title("lol")
        #self.title("Subjectwise Pass% of Students in a Class")
        tk.Frame.__init__(self, parent)
        self.can = tk.Canvas(self, bg='blue', height = 800, width = 2000, relief = tk.RAISED)

        #self.browse = tk.StringVar()
        self.selected_file = tk.StringVar()

        self.controller = controller

        self.selection_box = tk.Button(self.can, text="Browse", font=("Helvetica",15), command=self.browse, relief = tk.RAISED, bg="lightgray")
        self.selection_box.pack()
        self.selection_box.place(relx=0.771, rely=0.303, height=43, width=176)
        #self.selection_box.place(x=380, y=350)
        self.can.pack(side=tk.TOP)

        self.back = tk.Button(self.can, text = "Back", font=("Helvetica",15),relief = tk.RAISED, command=self.return2main, bg="red")
        self.back.pack()
        self.back.place(relx=0.1, rely=0.500, height=33, width=111)
        self.can.pack(side=tk.TOP)

        self.visualize = tk.Button(self.can, text="Visualize", font=("Helvetica",15), command=self.visualize, bg="yellow")
        self.visualize.pack()
        #self.visualize.place(x=480, y=450)
        self.visualize.place(relx=0.422, rely=0.541, height=33, width=111)
        self.can.pack(side=tk.TOP)

        self.file_name = tk.Entry(self.can, textvariable = self.selected_file,  background="white", font=("Helvetica",10), foreground = "#000000", insertbackground = "black")
        self.file_name.pack(side=tk.RIGHT)
        self.file_name.place(relx=0.243, rely=0.303, height=44, relwidth=0.49)
        #self.file_name.place(x=600, y=450)
    
    def browse(self):
        print("Button clicked")
        print("hahah", functionality_name)
        #Tk().withdraw()
        self.selected_file.set(askopenfilename())
        #print(self.selected_file)

    def visualize(self):
        print("Visualization")
        print(self.selected_file.get())
        subjectwise_passed_percentage(self.selected_file.get())
    
    def return2main(self):
        self.controller.show_frame(main_window_blue)

class subject_wise_grade(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.can = tk.Canvas(self, bg='blue', height = 800, width = 2000, relief = tk.RAISED)

        #self.browse = tk.StringVar()
        self.selected_file = tk.StringVar()

        self.controller = controller

        self.selection_box = tk.Button(self.can, text="Browse", font=("Helvetica",15), command=self.browse, relief = tk.RAISED, bg="lightgray")
        self.selection_box.pack()
        #self.selection_box.place(x=380, y=350)
        self.selection_box.place(relx=0.771, rely=0.303, height=43, width=176)
        self.can.pack(side=tk.TOP)

        self.back = tk.Button(self.can, text = "Back", font=("Helvetica",15),relief = tk.RAISED, command=self.return2main, bg="red")
        self.back.pack()
        self.back.place(relx=0.1, rely=0.500, height=33, width=111)
        self.can.pack(side=tk.TOP)

        self.visualize = tk.Button(self.can, text="Visualize", font=("Helvetica",15), command=self.visualize, bg="yellow")
        self.visualize.pack()
        #self.visualize.place(x=480, y=450)
        self.visualize.place(relx=0.422, rely=0.541, height=33, width=111)
        self.can.pack(side=tk.TOP)

        self.file_name = tk.Entry(self.can, textvariable = self.selected_file,  background="white", font=("Helvetica",10), foreground = "#000000", insertbackground = "black")
        self.file_name.pack(side=tk.RIGHT)
        self.file_name.place(relx=0.243, rely=0.303, height=44, relwidth=0.49)

    def browse(self):
        print("Button clicked")
        print("hahah", functionality_name)
        #Tk().withdraw()
        self.selected_file.set(askopenfilename())
        #print(self.selected_file)

    def visualize(self):
        print("Visualization")
        print(self.selected_file.get())
        by_grade(self.selected_file.get())

    def return2main(self):
        self.controller.show_frame(main_window_blue)

class semester_comparision(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.can = tk.Canvas(self, bg='blue', height = 800, width = 2000, relief = tk.RAISED)

        self.controller = controller

        self.num_of_semesters = tk.StringVar()
        self.sem_no = tk.Label(self.can, text = "Total Number of Semesters: ", width=100, height=100, bg = "blue", font=("Helvetica",20))
        self.sem_no.place(x=480, y=450)
        self.sem_no.pack(side = tk.LEFT)

        self.num_sems = tk.Entry(self.can, textvariable = self.num_of_semesters, background="white", font="TkFixedFOnt", foreground = "#000000", insertbackground = "black")
        self.num_sems.pack(side=tk.RIGHT)
        self.num_sems.place(x=600, y=450)

        self.back = tk.Button(self.can, text = "Back", font=("Helvetica",15),relief = tk.RAISED, command=self.return2main, bg="red")
        self.back.pack()
        self.back.place(relx=0.1, rely=0.500, height=33, width=111)
        self.can.pack(side=tk.TOP)

        #self.browse = tk.StringVar()
        self.selected_file = tk.StringVar()

        self.visualize = tk.Button(self.can, text="Select", font=("Helvetica",20), command=self.select, bg="yellow")
        self.visualize.pack()
        self.visualize.place(relx=0.243, rely=0.303, height=44, relwidth=0.49)
        self.can.pack(side=tk.TOP)

    def select(self):
        global num_of_semesters
        num_of_semesters = self.num_of_semesters.get()

        #print("Num of Semesters are: ", self.num_of_semesters.get())
        self.controller.show_frame(select_semesters)
    
    def return2main(self):
        self.controller.show_frame(main_window_blue)

class select_semesters(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.can = tk.Canvas(self, bg='blue', height = 800, width = 2000, relief = tk.RAISED)
        self.controller = controller

        #self.no_of_semesters = num_of_semesters

        self.back = tk.Button(self.can, text = "Back", font=("Helvetica",15),relief = tk.RAISED, command=self.return2main, bg="red")
        self.back.pack()
        self.back.place(relx=0.1, rely=0.500, height=33, width=111)
        self.can.pack(side=tk.TOP)

        self.file_list = []

        self.select_files = tk.Button(self.can, text = "Select Files in order", font=("Helvetica",30),relief = tk.RAISED,command=self.selections, bg="red")
        self.select_files.pack()
        self.select_files.place(relx=0.243, rely=0.303, height=44, relwidth=0.49)
        self.can.pack(side=tk.TOP)

        self.selected_file = tk.StringVar()
    
    def selections(self):
        print("Num of semesters ", num_of_semesters)
        #browsing_thread = threading.Thread(target = self.browse)
        #browsing_thread.setDaemon=True
        #browsing_thread.start()
        #for i in range()
        for i in range(int(num_of_semesters)):
            self.browse()
        print("File List: ", self.file_list)
        compare(self.file_list)

    def browse(self):
        print("Button clicked")
        #Tk().withdraw()
        self.selected_file.set(askopenfilename())
        print(self.selected_file.get())
        self.file_list.append(self.selected_file.get())
        
        #print(self.selected_file)

    def return2main(self):
        self.controller.show_frame(semester_comparision)

my_app = PEC()
my_app.mainloop()







