import tkinter as tk

# Quiz Program
MainWindow = tk.Tk()
MainWindow.geometry('420x420')
MainWindow.title('Quiz Program')

# Function to switch between frames
def show_frame(frame):
    
    start_frame.pack_forget()
    quiz_frame.pack_forget()
    result_frame.pack_forget()
    frame.pack(fill='both', expand=1)

# Create Frames
start_frame = tk.Frame(MainWindow)
quiz_frame = tk.Frame(MainWindow)
result_frame = tk.Frame(MainWindow)

# Widgets (Start Frame)
start_label = tk.Label(start_frame, text='Welcome to the General Knowledge Quiz', font=('Arial', 18),
                       bg = 'purple', fg = 'white')
start_label.pack(padx=20, pady=20)

start_button = tk.Button(start_frame, text='START QUIZ', command=lambda: show_frame(quiz_frame))
start_button.pack()

# Widgets (Quiz Frame)
quiz_label = tk.Label(quiz_frame, text='Insert Question', font=('Arial', 20))
quiz_label.grid(row = 0, column = 0, padx=20, pady=20)

next_button = tk.Button(quiz_frame, text='Next Question', command=lambda: show_frame(result_frame))
next_button.grid()

# Widgets (Result Frame)
result_label = tk.Label(result_frame, text='You have managed to complete the quiz!',
                        font=('Arial', 20))
result_label.pack(pady=20)

# Show the start frame first
start_frame.pack(fill='both', expand=1)

MainWindow.mainloop()
