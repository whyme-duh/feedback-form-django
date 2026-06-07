from django import forms
from .models import FeedbackForm

class FeedbackFormField(forms.ModelForm):
    
    class Meta:
        model = FeedbackForm
        exclude = ["user"]
        fields = "__all__"
        widgets = {
            'sex': forms.RadioSelect,
            'hospital_sanitaion': forms.RadioSelect,
            'care_co_opp_of_administrator': forms.RadioSelect,
            'promptness_of_service': forms.RadioSelect,
            'doctor_response': forms.RadioSelect,
            'satisfied_with_doctor_explanation': forms.RadioSelect,
            'satisfied_by_nurse_service': forms.RadioSelect,
            'room_sanitation': forms.RadioSelect,
            'bathroom_cleanliness': forms.RadioSelect,
            'everythin_clean_or_not': forms.RadioSelect,

            'ward_cleanliness': forms.RadioSelect,
            'service_promptness_emegency_service': forms.RadioSelect,
            'arrival_of_ambulance': forms.RadioSelect,
            'satisfaction_with_ambulance_internal_service': forms.RadioSelect,
            'pharmacy': forms.RadioSelect,
            'x_ray_usg_echo_pathology_endoscopy_physio': forms.RadioSelect,
            'ICU_OT': forms.RadioSelect,
            'problem_during_stay': forms.RadioSelect,
            'if_yes_problem_solved_promptly_or_not': forms.RadioSelect,
            'satisfied_with_overall_aspect_of_hospital': forms.RadioSelect,
            'would_you_share_or_not': forms.RadioSelect,
            
            'if_no_specify_reason': forms.Textarea(attrs={'rows': 3}),
            'if_not_room_clean': forms.Textarea(attrs={'rows': 3}),
            'if_yes_specify_reason': forms.Textarea(attrs={'rows': 3}),
            'sharing_with_friend_if_yes': forms.Textarea(attrs={'rows': 3}),
            'recommendation_for_hospital': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Loop through all form fields dynamically
        for field_name, field in self.fields.items():
            # Target any choice-based field (like CharFields with choices)
            if hasattr(field, 'choices'):
                # If the first option is a blank choice, slice it out safely
                if field.choices and field.choices[0][0] == '':
                    field.choices = field.choices[1:]

    

    