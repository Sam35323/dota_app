from django import forms
from .models import Hero


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = (
            'name', 'disc', 'top_class', 'top_position', 'bio', 'ultimate', 'ultimate_disc', 'skill_1', 'skill_1_disc',
            'skill_2', 'skill_2_disc', 'skill_3', 'skill_3_disc')
