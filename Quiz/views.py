from django.shortcuts import render
from . import models
from random import randint
import decimal


def Question(request,firstname,surname,code,id, user_id):
 
    if id == 0:
        try:
            group = models.QuizGroup.objects.get(code=request.POST.get("group"))
        except:
            return render(request, "home.html", {"error":"No such quiz!", "n1":request.POST.get("firstname"), "n2":request.POST.get("surname"), "n3":request.POST.get("group")})

        www = models.UserGroup.objects.filter(group=group.code, firstname=request.POST.get('firstname'), surname=request.POST.get('surname')).first()

        if www:
            return render(request, "home.html", {"error":"U have completed this quiz!", "n1":request.POST.get("firstname"), "n2":request.POST.get("surname"), "n3":request.POST.get("group")})
        user_id = randint(10000, 99999)
        models.Results.objects.create(parent=group, firstname=request.POST.get("firstname"), surname=request.POST.get("surname"), point=0, exam_id=user_id)
        models.UserGroup.objects.create(group=group.code, firstname=request.POST.get('firstname'), surname=request.POST.get('surname'))
        first_question = models.Quiz.objects.filter(group=group).first()
        answers = first_question.answers.all() if first_question else []
        return render(request, 'index.html', {'queryset': first_question, 
                                              "answers":answers, 
                                              "duration":first_question.duration, 
                                              "id":first_question.id, 
                                              "firstname":request.POST.get("firstname"), 
                                              "surname":request.POST.get("surname"), 
                                              "code": request.POST.get("group"), 
                                              "user_id": user_id
                                              })
    else:
        selected_answer = request.POST.get('answer')
        current_question = models.Quiz.objects.get(id=id)
        correct_answer = models.Answers.objects.get(parent=current_question, is_correct=True)
        obj, created = models.UserAnswer.objects.get_or_create(answer=id, firstname=firstname, surname=surname)
        if  created:
            if selected_answer == correct_answer.answer:
                user = models.Results.objects.get(exam_id=user_id)
                user.point = user.point + decimal.Decimal(100) /models.Quiz.objects.filter(group=models.QuizGroup.objects.get(code=code)).count()
                user.correct = user.correct+1
                user.save()
            else:
                user = models.Results.objects.get(exam_id=user_id)
                user.wrong = user.wrong+1
                user.save()
        group = models.QuizGroup.objects.get(code=code)
        first_question = models.Quiz.objects.filter(group=group, id__gt=id).first()
        if first_question:
            answers = first_question.answers.all() if first_question else []
            return render(request, 'index.html', {'queryset': first_question, 
                                                "answers":answers, 
                                                "duration":first_question.duration, 
                                                "id":first_question.id, 
                                                "firstname":firstname, 
                                                "surname":surname, 
                                                "code": code, 
                                                "user_id": user_id
                                                })
        else:
            username = models.Results.objects.get(exam_id=user_id).firstname+"  "+models.Results.objects.get(exam_id=user_id).surname
            quiz_total = models.Quiz.objects.filter(group=models.QuizGroup.objects.get(code=code)).count()
            user_point = models.Results.objects.get(exam_id=user_id).point
            correct = models.Results.objects.get(exam_id=user_id).correct
            wrong = models.Results.objects.get(exam_id=user_id).wrong
            if user_point > 99.8:
                user_point = 100
                stat = models.Results.objects.get(exam_id=user_id)
                stat.point = 100
                stat.save()
            return render(request, "result.html", {"username":username, "quiz_total":quiz_total, "user_point":user_point, "correct":correct, "wrong":wrong}) 
    

def Home(request):
    return render(request, "home.html")


def Index(request):
    return render(request, "homehome.html")


def Practice(request):
    return render(request, "practice.html")