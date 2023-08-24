from django import forms
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    """Форма для добавления пользователем новой темы."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    """Форма для добавления пользователем новой записи по конкретной теме."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}