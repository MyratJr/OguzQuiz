from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


import io
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from django.contrib import admin
from reportlab.lib import colors

from django.contrib.auth.models import Group, User

admin.site.unregister(Group)


def generate_pdf(modeladmin, request, queryset):
    buffer = io.BytesIO()
    queryset = queryset.order_by("-point")

    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 18)
    p.setFillColor(colors.blue) 
    p.drawString(200, 790, f"ALL EXAM RESULTS")
    p.drawImage("D:\\2024\\static\\brand\\logo.png", 100, 760, width=75, height=75, mask='auto')
    p.drawImage("D:\\2024\\static\\brand\\Flag_of_Turkmenistan.svg.png", 410, 770, width=90, height=60, mask='auto')
    p.setFont("Helvetica", 14)
    p.setFillColor(colors.black) 
    p.drawString(70, 750, "____________________________________________________________")
    p.drawString(75, 730, f"No")
    p.drawString(107, 730, f"Exam")
    p.drawString(155, 730, f"Firstname")
    p.drawString(270, 730, f"Surname")
    p.drawString(385, 730, f"Wrong")
    p.drawString(440, 730, f"Correct")
    p.drawString(500, 730, f"Point")
    p.drawString(70, 46, "____________________________________________________________")
    a=738
    for i in range(0,55):
        p.drawString(68, a, f"""|""")
        p.drawString(100, a, f"""|""")
        p.drawString(148, a, f"""|""")
        p.drawString(263, a, f"""|""")
        p.drawString(378, a, f"""|""")
        p.drawString(433, a, f"""|""")
        p.drawString(493, a, f"""|""")
        p.drawString(535, a, f"""|""")
        a-=12.8
    col = 710
    row_counter = 0
    no = 0
    for obj in queryset:
        no += 1
        p.setFont("Helvetica", 10)
        row_counter += 1
        p.drawString(70, col+17, "____________________________________________________________________________________")
        p.drawString(75, col, str(no))
        p.drawString(107, col, obj.parent.code)
        p.drawString(155, col, obj.firstname)
        p.drawString(270, col, obj.surname)
        p.drawString(385, col, str(obj.wrong))
        p.drawString(440, col, str(obj.correct))
        p.drawString(500, col, str(obj.point))
        col-=20
        if row_counter == 34 and p.getPageNumber() == 1 or row_counter == 37 and p.getPageNumber() > 1:
            p.showPage()
            row_counter = 0
            col = 760
            p.setFont("Helvetica", 14)
            p.drawString(70, 800, "____________________________________________________________")
            p.drawString(75, 780, f"No")
            p.drawString(107, 780, f"Exam")
            p.drawString(155, 780, f"Firstname")
            p.drawString(270, 780, f"Surname")
            p.drawString(385, 780, f"Wrong")
            p.drawString(440, 780, f"Correct")
            p.drawString(500, 780, f"Point")
            p.drawString(70, 31, "____________________________________________________________")
            a=787
            for i in range(0,60):
                p.drawString(68, a, f"""|""")
                p.drawString(100, a, f"""|""")
                p.drawString(148, a, f"""|""")
                p.drawString(263, a, f"""|""")
                p.drawString(378, a, f"""|""")
                p.drawString(433, a, f"""|""")
                p.drawString(493, a, f"""|""")
                p.drawString(535, a, f"""|""")
                a-=12.8

    p.save()

    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="model_data.pdf"'
    return response

generate_pdf.short_description = "Download selected as PDF"


class AnswerAdmin(admin.TabularInline):
    model = models.Answers
    extra = 4


@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]
    list_display = ['question', 'group']


@admin.register(models.Results)
class ResultAdmin(admin.ModelAdmin):
    actions = [generate_pdf]
    search_fields = ["parent__code"]


class QuizInline(admin.TabularInline):
    model = models.Quiz
    extra = 1 


class ResultInline(admin.TabularInline):
    model = models.Results
    fields = ["firstname", "surname", "point", "correct", "wrong"]
    readonly_fields = ["firstname", "surname", "point", "correct", "wrong"]
    max_num = 0


@admin.register(models.QuizGroup)
class QuizGroupAdmin(admin.ModelAdmin):
    inlines = [QuizInline, ResultInline]
    list_display = ['code'] 


admin.site.site_header = 'OguzQuiz Admin'


admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin, admin.ModelAdmin):
    list_display = ["username"]
    fieldsets = (
        ("Important datas", {'fields': ('username', 'password')}),
        ('Important dates', {'fields': ('last_login',"date_joined")}),
    )    