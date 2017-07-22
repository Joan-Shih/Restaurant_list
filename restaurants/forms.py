from django import forms

class  CommentForm(forms.Form):
	"""docstring for  CommentForm"""
	visitor = forms.CharField(max_length = 20)
	email = forms.EmailField(max_length = 20,required = False)
	content = forms.CharField(max_length = 200, widget = forms.Textarea())
	def clean_content(self):
		content = self.cleaned_data['content']
		if ('幹' in content):
			raise forms.ValidationError('請勿使用不雅文字')

		return content