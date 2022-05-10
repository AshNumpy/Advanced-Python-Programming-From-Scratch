# Question:
from secrets import choice

class Question:

    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        return self.answer == answer

# print(q1.checkAnswer('python'))
# print(q1.checkAnswer('C#'))

# Quiz:

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input("Answer: ")
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 1

        self.questionIndex += 1

        self.displayQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore()
        else:
            self.displayQuestion()
            
    def showScore(self):
        print(f"Score: {self.score}")

q1 = Question('what is the best programming language?', ['C#','python','javascript','java'],'python')
q2 = Question('what is the second programming language?', ['C#','python','javascript','java'],'C#')
q3 = Question('what is the third programming language?', ['C#','python','javascript','java'],'javascript')

questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.displayQuestion()