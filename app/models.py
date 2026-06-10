from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


alphabetic_validator = RegexValidator(
    regex=r'^[a-zA-Z]+$',
    message = "Only alphabetic characters are allowed.",
    code = 'invalid_alphabet'
)

class FeedbackForm(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    QUALITY_CHOICES = [
        ("Excellent", "Excellent"),
        ("Good", "Good"),
        ("Satisfactory", "Satisfactory"),
        ("Poor", "Poor"),
    ]

    GENERAL_YES_NO_CHOICE = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = False, null = False)
    full_name = models.CharField(max_length=100, blank = False,validators=[alphabetic_validator] )
    sex = models.CharField(choices = GENDER_CHOICES, blank = False)
    bed_no = models.CharField(max_length=5, blank = False)
    ip_number = models.IntegerField(blank = False)
    Signature = models.CharField(max_length=50, blank = False)

    # about hospital quality
    
    hospital_sanitaion = models.CharField(choices = QUALITY_CHOICES, blank = False)
    care_co_opp_of_administrator = models.CharField(choices = QUALITY_CHOICES, blank = False)
    promptness_of_service = models.CharField(choices = QUALITY_CHOICES, blank = False)

    # about medical staff

    doctor_response = models.CharField(choices = QUALITY_CHOICES, blank = False)
    satisfied_with_doctor_explanation = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    satisfied_by_nurse_service = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    if_no_specify_reason = models.TextField(blank = True, null= True)

    #about room

    room_sanitation = models.CharField(choices = QUALITY_CHOICES, blank = False)
    bathroom_cleanliness = models.CharField(choices = QUALITY_CHOICES, blank = False)
    everythin_clean_or_not = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    if_not_room_clean = models.TextField(blank = True, null= True)

    # about emergency service

    ward_cleanliness =  models.CharField(choices = QUALITY_CHOICES, blank = False)
    service_promptness_emegency_service =  models.CharField(choices = QUALITY_CHOICES, blank = False)

    # ambulance service

    arrival_of_ambulance = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    satisfaction_with_ambulance_internal_service = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)

    # general service

    pharmacy = models.CharField(choices = QUALITY_CHOICES, blank = False)
    x_ray_usg_echo_pathology_endoscopy_physio = models.CharField(choices = QUALITY_CHOICES, blank = False)
    ICU_OT = models.CharField(choices = QUALITY_CHOICES, blank = False)
    problem_during_stay = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    if_yes_specify_reason = models.TextField(blank = True, null= True)

    if_yes_problem_solved_promptly_or_not = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    satisfied_with_overall_aspect_of_hospital = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = False)
    would_you_share_or_not = models.CharField(choices= GENERAL_YES_NO_CHOICE, blank = False)
    sharing_with_friend_if_yes = models.TextField(blank = True, null= True)

    # other

    recommendation_for_hospital = models.TextField(blank = True, null = True)