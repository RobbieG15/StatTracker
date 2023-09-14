from django import forms

class GameCreationForm(forms.Form):
    homeTeam = forms.CharField(label = "Home Team")
    awayTeam = forms.CharField(label = "Away Team")
    dateTime = forms.DateTimeField(label = "Date and Time")