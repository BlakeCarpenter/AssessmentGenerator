#THIS IS THE PDF GEN MAIN THING
import ho.pisa as pisa
import json
from assessmentgenerator.models import Question

def generate(title, date, question_array):
    print(title)
    print(date)
    print(question_array)
    return 1

def parseQuestion(question):
    ret = ""
    q_body = json.loads(question.question_body)['choices']
    for x in body:
        ret += '<li class="answer-choice">'+x['choice']+'</li>'
    return ret
