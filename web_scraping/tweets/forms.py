from django import forms

from .models import Tweet
MAX_TWEET_LENGTH=240
class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['content']

    def clean_content(self):
        content=self.cleaned_data.get("content")
        if len(content)>MAX_TWEET_LENGTH:
            raise forms.ValidationError("The maximum of 240 characters may use for a tweet and there been depleted.")
        return content