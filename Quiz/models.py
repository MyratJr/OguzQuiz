from django.db import models
from django.core.exceptions import ValidationError


class QuizGroup(models.Model):
    code = models.CharField(max_length=6)


class Quiz(models.Model):
    group = models.ForeignKey(QuizGroup, on_delete=models.CASCADE, related_name="questions")
    question = models.CharField(max_length=555)
    duration = models.IntegerField(default=60)

    def __str__(self):
        return self.question
    

class Answers(models.Model):
    parent = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="answers")
    answer = models.CharField(max_length=55)
    is_correct = models.BooleanField(default=False)

    def clean(self):
        if self.is_correct:
            correct_answers = Answers.objects.filter(parent=self.parent, is_correct=True).exclude(id=self.id)
            if correct_answers.exists():
                raise ValidationError("There can only be one correct answer per question.")
        return super().clean()
    

class Results(models.Model):
    parent = models.ForeignKey(QuizGroup, on_delete=models.CASCADE, related_name="results")
    exam_id = models.IntegerField(default=0)
    firstname = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    point = models.DecimalField(max_digits=5, decimal_places=0)

    def __str__(self):
        return self.firstname+""+self.surname
    

class UserGroup(models.Model):
    group = models.IntegerField()
    firstname = models.CharField(max_length=55, blank=True, null=True)
    surname = models.CharField(max_length=55, blank=True, null=True)


class UserAnswer(models.Model):
    answer = models.IntegerField()
    firstname = models.CharField(max_length=55, blank=True, null=True)
    surname = models.CharField(max_length=55, blank=True, null=True)