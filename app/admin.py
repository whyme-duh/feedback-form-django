import base64

from django.contrib import admin
from django.http import HttpResponse

from website import settings
from . models import FeedbackForm
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
import os



@admin.register(FeedbackForm)
class FeedbackFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'ip_number', 'bed_no')
    actions = ['download_pdf_action']

    @admin.action(description="Download selected forms as PDF")
    def download_pdf_action(self, request, queryset):
        # font_path = finders.find('font/Noto_Sans_Devanagari/static/NotoSansDevanagari-Regular.ttf')


        # if not font_path:
        #     font_path = os.path.join(settings.BASE_DIR, 'app', 'static', 'font', 'Noto_Sans_Devanagari', 'static', 'NotoSansDevanagari-Regular.ttf')


        if queryset.count() ==1:
            feedback = queryset.first()
            # with open(font_path, "rb") as font_file:
            #     encoded_string = base64.b64encode(font_file.read()).decode('utf-8')

            #  font_base64 = f"data:font/ttf;base64,{encoded_string}"
            # print(font_path, font_base64)
            html_string = render_to_string('app/feedback_export_pdf.html', {'feedback': feedback})

            response = HttpResponse(content_type ="application/pdf")
            response["Content-Disposition"] = f'attachment; filename="Everest_Admin_Feedback_{feedback.id}.pdf"'
            pisa.CreatePDF(html_string, dest=response)
            return response
        else:
            self.message_user(request, "Please select exaclty one feedback form at a time!")
            return None

