from django import forms

checked = [0,0,0,0,0,0,0,0]

class check_form(forms.Form):
    checked[0] = forms.BooleanField(label='1')
    checked[1] = forms.BooleanField(label='2')
    checked[2] = forms.BooleanField(label='3')
    checked[3] = forms.BooleanField(label='4')
    checked[4] = forms.BooleanField(label='5')
    checked[5] = forms.BooleanField(label='6')
    checked[6] = forms.BooleanField(label='7')
    checked[7] = forms.BooleanField(label='8')

    def water_cups(request):
        print(checked)
        cups = sum(checked)
        print(cups)
        return cups