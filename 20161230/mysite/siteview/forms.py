from django import newforms as forms

TOPIC_CHOICES = (
	('general','Genaral enquiry'),
	('bug','Bug report'),
	('suggestion','Suggestion'),
	)

class ContactForm(forms.Form):
	topic = forms.ChoiceFiled(choice=TOPIC_CHOICES)
	message = forms.CharFiled()
	sender = forms.EmailField(required=False)
	