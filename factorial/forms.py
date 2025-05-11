from django import forms

class FactorialForm(forms.Form):
    number = forms.IntegerField(
        label='Input number',
        min_value=0,
        help_text='Must be positive integer',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'For example: 5, 18, 95 ...'}),
        template_name='forms/text_field.html',
    )

    def clean_number(self):
        value = self.cleaned_data['number']
        if value > 100:
            raise forms.ValidationError("Too large number!")
        return value
