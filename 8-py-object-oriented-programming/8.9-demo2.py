# Question:
class Question:
    def __init__(self, text, choice, answer):
        self.text = text 
        self.choice = choice 
        self.answer = answer 

    def checkAnswer(self, answer):
        return self.answer == answer


# Quiz:
class Quiz:
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Question {self.questionIndex+1}: {question.text}")

        



q1 = Question("Which one is the best programming language" , ["python","C#","Javascript","C++"], "python")
q2 = Question("Which one is most popular programming language" , ["Javascript","C#","python","C++"], "python")
q3 = Question("Which one is the start with 'p' in programming language " , ["Javascript","C#","C++","python"], "python")
questions = [q1,q2,q3]

quiz = Quiz(questions)

quiz.displayQuestion()