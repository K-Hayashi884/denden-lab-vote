from django import forms

from .models import Vote


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = [
            "vote1",
            "vote2",
            "vote3",
            "vote4",
            "vote5",
            "vote6",
            "vote7",
            "year",
            "email",
        ]
        labels = {
            "vote1": "第１志望",
            "vote2": "第２志望",
            "vote3": "第３志望",
            "vote4": "第４志望",
            "vote5": "第５志望",
            "vote6": "第６志望",
            "vote7": "第７志望",
            "year": "配属年度",
            "email": "KUMOIメールアドレス",
        }

    def clean_email(self):
        # メールアドレスのvalidation
        email = self.cleaned_data.get("email")
        if "@st.kyoto-u.ac.jp" not in email:
            raise forms.ValidationError("st.kyoto-u.ac.jpドメインのKUMOIメールを入力してください")
        return email

    def clean(self):
        # 重複した投票がないかのvalidation
        cleaned_data = super().clean()
        votes = [
            cleaned_data.get("vote1"),
            cleaned_data.get("vote2"),
            cleaned_data.get("vote3"),
            cleaned_data.get("vote4"),
            cleaned_data.get("vote5"),
            cleaned_data.get("vote6"),
            cleaned_data.get("vote7"),
        ]
        print(votes)
        print(set(votes))
        if len(votes) != len(set(votes)):
            raise forms.ValidationError("重複した投票が存在します")
        return cleaned_data
