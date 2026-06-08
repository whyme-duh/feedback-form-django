import base64
from django.contrib import admin
from django.http import HttpResponse
from website import settings
from . models import FeedbackForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from xhtml2pdf.files import pisaFileObject
from django.contrib.staticfiles import finders
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os



@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'ip_number', 'bed_no')
    actions = ['download_pdf_action']

    @admin.action(description="Download selected forms as PDF")
    def download_pdf_action(self, request, queryset):
       
        

        if queryset.count() ==1:
            feedback = queryset.first()

            pisaFileObject.getNamedFile = lambda self: self.uri

            font_path = finders.find('font/Noto_Sans_Devanagari/static/NotoSansDevanagari-Regular.ttf')

            if not font_path:
                font_path = os.path.join(settings.BASE_DIR, 'app', 'static', 'font', 'Noto_Sans_Devanagari', 'static', 'NotoSansDevanagari-Regular.ttf')
            try:
                print("1st path" , font_path)
                font_path = font_path.replace('\\', '/')

                print("after replace", font_path)
                pdfmetrics.registerFont(TTFont('NotoSansDevanagari', font_path))
            except Exception as e:
                print(e)
                pass

            
            html_string = render_to_string('app/feedback_export_pdf.html', {'feedback': feedback, 'nepali_font_path': font_path})

            response = HttpResponse(content_type ="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="Everest_Admin_Feedback_{feedback.id}.pdf"'
            pisa.CreatePDF(html_string, dest=response, encoding='utf-8')
            return response
        else:
            self.message_user(request, "Please select exaclty one feedback form at a time!")
            return None

