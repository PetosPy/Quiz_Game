from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#325288"

class QuizInterface():

	def __init__(self, quiz_brain):

		self.quiz = quiz_brain

		# Creating the root/window
		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(pady=20, padx=20, bg=THEME_COLOR)
		self.window.geometry("350x500")

		# Creating the score label
		self.score_label = Label(text=f"Score: 0", 
			bg=THEME_COLOR, fg="white", 
			font=("Ariel", 15, "bold"))
		self.score_label.grid(row=0, column=1)

		# Creating the white in the canvas middle
		self.canvas = Canvas(width=300, height=250, bg="white")
		self.canvas.grid(row=1, column=0, columnspan=2, pady=40)
		self.question_text = self.canvas.create_text(150, 125, text="", 
			font=("Ariel", 15, "italic"), 
			width=210, 
			anchor="center")

		# Creating the buttons
		# check mark image to be used for button
		right_img = PhotoImage(file="./images/true.png")

		self.check_mark = Button(self.window, image=right_img, 
			bd=0, bg=THEME_COLOR, 
			command=self.true_pressed)
		self.check_mark.grid(row=2, column=1)

		# cross mark image to be used for button
		wrong_img = PhotoImage(file="./images/false.png")

		self.cross_mark = Button(self.window, 
			image=wrong_img, bd=0, 
			bg=THEME_COLOR, 
			command=self.false_pressed)
		self.cross_mark.grid(row=2, column=0)


		self.get_next_question()

		self.window.mainloop()


	def get_next_question(self):
		self.canvas.config(bg="white")

		if self.quiz.still_has_questions():
			self.score_label.config(text=f"Score: {self.quiz.score}")
			q_text = self.quiz.next_question()
			self.canvas.itemconfig(self.question_text, text=q_text)
		else:
			self.canvas.itemconfig(self.question_text, text="You have reached the end of the text")
			self.cross_mark.config(command=self.back_to_white)
			self.check_mark.config(command=self.back_to_white)


	def true_pressed(self):
		self.give_feedback(self.quiz.check_answer("True"))

			
	def false_pressed(self):
		self.give_feedback(self.quiz.check_answer("False"))
 

	def back_to_white(self):
		self.canvas.config(bg="white")


	def give_feedback(self, is_right):
		if is_right:
			self.canvas.config(bg="green")
		else:
			self.canvas.config(bg="red")

		self.window.after(1000, func=self.get_next_question)




			
		

		



