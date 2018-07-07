from .models import Idea,Comment
from django.forms import ModelForm

class IdeaForm(ModelForm):

	class Meta:
		
		model = Idea
		fields = ['tickersymbol','long_short','buyprice','targetprice','tradeenddate',
		'stoplossprice','shortthesis','longthesis',
		]	



class CommentForm(ModelForm):

	class Meta:

		model=Comment
		fields=['comment_text']