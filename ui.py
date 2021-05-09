from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#325288"

class QuizInterface():


	def __init__(self, quiz_brain):

		self.quiz = quiz_brain
		# Score counter. Starts off as 0
		self.score = 0

		# Creating the root/window
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(pady=20, padx=20, bg=THEME_COLOR)
		self.window.geometry("350x500")

		# Creating the score label
		self.score_label = Label(text="Score: 0", 
			bg=THEME_COLOR, fg="white", 
			font=("Ariel", 15, "bold"))
		self.score_label.grid(row=0, column=1)

		# Creating the white in the canvas middle
		self.canvas = Canvas(width=300, height=250, bg="white")
		self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
		self.question_text = self.canvas.create_text(150, 125, text="Hey you! How are you today?", 
			font=("Ariel", 15, "italic"), 
			width=210, 
			anchor="center")

		# Creating the buttons
		right_img = PhotoImage(file="./images/true.png")
		self.check_mark = Button(self.window, image=right_img, 
			bd=0, bg=THEME_COLOR)
		self.check_mark.grid(row=2, column=1)

		wrong_img = PhotoImage(file="./images/false.png")
		self.cross = Button(self.window, image=wrong_img, bd=0, bg=THEME_COLOR)
		self.cross.grid(row=2, column=0)


		self.get_next_question()

		self.window.mainloop()

	def get_next_question(self):
		q_text = self.quiz.next_question()
		self.canvas.itemconfig(self.question_text, text=q_text)

		



