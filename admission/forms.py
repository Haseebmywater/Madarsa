from django import forms

class AdmissionForm(forms.Form):
    student_name = forms.CharField(label='نام طالب علم')
    birth_date = forms.DateField(label='تاریخ پیدائش', widget=forms.TextInput(attrs={'type': 'date'}))
    father_name = forms.CharField(label='ولدیت')
    guardian_name = forms.CharField(label='سرپرست', required=False)
    previous_school = forms.CharField(label='مدرسہ / سکول کا نام')
    contact_info = forms.CharField(label='رابطہ نمبر')
    address = forms.CharField(label='پتہ', widget=forms.Textarea(attrs={'rows': 2}))
    education_level = forms.ChoiceField(label='درجہ', choices=[('primary', 'ابتدائی'), ('secondary', 'ثانوی'), ('higher', 'اعلیٰ')])
    agreement = forms.BooleanField(label='اتفاق')

