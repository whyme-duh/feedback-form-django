from django.db import models
from django.contrib.auth.models import User


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

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank = True, null = True)
    full_name = models.CharField(max_length=100, blank = True)
    sex = models.CharField(choices = GENDER_CHOICES)
    bed_no = models.IntegerField()
    ip_number = models.IntegerField()
    Signature = models.CharField(max_length=50, blank =True)

    # about hospital quality
    
    hospital_sanitaion = models.CharField(choices = QUALITY_CHOICES)
    care_co_opp_of_administrator = models.CharField(choices = QUALITY_CHOICES)
    promptness_of_service = models.CharField(choices = QUALITY_CHOICES)

    # about medical staff

    doctor_response = models.CharField(choices = QUALITY_CHOICES)
    satisfied_with_doctor_explanation = models.CharField(choices = GENERAL_YES_NO_CHOICE)
    satisfied_by_nurse_service = models.CharField(choices = GENERAL_YES_NO_CHOICE)
    if_no_specify_reason = models.TextField(blank = True, null= True)

    #about room

    room_sanitation = models.CharField(choices = QUALITY_CHOICES, blank = True)
    bathroom_cleanliness = models.CharField(choices = QUALITY_CHOICES, blank = True)
    everythin_clean_or_not = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)
    if_not_room_clean = models.TextField(blank = True, null= True)

    # about emergency service

    ward_cleanliness =  models.CharField(choices = QUALITY_CHOICES, blank = True)
    service_promptness_emegency_service =  models.CharField(choices = QUALITY_CHOICES, blank = True)

    # ambulance service

    arrival_of_ambulance = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)
    satisfaction_with_ambulance_internal_service = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)

    # general service

    pharmacy = models.CharField(choices = QUALITY_CHOICES, blank = True)
    x_ray_usg_echo_pathology_endoscopy_physio = models.CharField(choices = QUALITY_CHOICES, blank = True)
    ICU_OT = models.CharField(choices = QUALITY_CHOICES, blank = True)
    problem_during_stay = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)
    if_yes_specify_reason = models.TextField(blank = True, null= True)

    if_yes_problem_solved_promptly_or_not = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)
    satisfied_with_overall_aspect_of_hospital = models.CharField(choices = GENERAL_YES_NO_CHOICE, blank = True)
    would_you_share_or_not = models.CharField(choices= GENERAL_YES_NO_CHOICE, blank = True)
    sharing_with_friend_if_yes = models.TextField(blank = True, null= True)

    # other

    recommendation_for_hospital = models.TextField(blank = True, null = True)