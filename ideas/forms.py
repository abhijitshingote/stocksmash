from .models import Idea
from django.forms import ModelForm

class IdeaForm(ModelForm):

	class Meta:
		
		model = Idea
		fields = ['tickersymbol','buyprice','targetprice','tradeenddate',
		'stoplossprice','shortthesis','longthesis',
		]	