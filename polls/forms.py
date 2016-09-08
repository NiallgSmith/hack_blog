from django import forms
from models import Poll, PollSubject


class PollForm(forms.ModelForm):
    question = forms.CharField(label='What is the poll about?')
    class Meta:
        model = Poll
        fields = ['question']

class PollSubjectForm(forms.ModelForm):
    name = forms.CharField(label='Poll subject field', required=True)

    def __init__(self, *args, **kwargs):
        super(PollSubjectForm, self).__init__(*args, **kwargs)

        self.empty_permitted = False

    class Meta:
        model = PollSubject
        fields = ['name']
