from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime, timedelta


class FlightForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(FlightForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'Flight-Form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'result'
        self.helper.add_input(Submit('submit', 'Submit'))

    from_ = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "From"}))
    to = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "To"}))
    outbound = forms.DateField(
        initial=datetime.today(),
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    inbound = forms.DateField(
        initial=datetime.today() + timedelta(days=1),
        widget=forms.DateInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
