import datetime

from django.db import models


class Vote(models.Model):
    YEAR_CHOICES = [
        (r, r)
        for r in range(
            2022,
            datetime.date.today().year + 2
            if datetime.date.today().month > 3
            else datetime.date.today().year + 3,
        )
    ]

    vote1 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote1", null=True, blank=True
    )
    vote2 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote2", null=True, blank=True
    )
    vote3 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote3", null=True, blank=True
    )
    vote4 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote4", null=True, blank=True
    )
    vote5 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote5", null=True, blank=True
    )
    vote6 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote6", null=True, blank=True
    )
    vote7 = models.ForeignKey(
        "Lab", on_delete=models.CASCADE, related_name="vote7", null=True, blank=True
    )

    year = models.IntegerField(
        choices=YEAR_CHOICES,
        default=datetime.date.today().year + 1
        if datetime.date.today().month > 3
        else datetime.date.today().year,
    )  # 配属予定年度

    email = models.EmailField(max_length=50)

    is_active = models.BooleanField(default=False)


class Lab(models.Model):
    BELONG_CHOICES = [
        ("Engineering", "工学研究科"),
        ("Informatics", "情報学研究科"),
        ("Energy", "エネルギー科学研究科"),
        ("Humanosphere", "生存圏研究所"),
        ("Advanced Energy", "エネルギー理工学研究所"),
        ("Media", "学術情報メディアセンター"),
    ]
    CAMPUS_CHOICES = [("Yoshida", "吉田"), ("Katsura", "桂"), ("Uji", "宇治")]
    name = models.CharField(max_length=30, blank=False, null=False)  # 研究室名
    belongs_to = models.CharField(
        max_length=20, blank=False, null=False, choices=BELONG_CHOICES
    )  # 所属する研究科
    campus = models.CharField(max_length=10, blank=False, null=False, choices=CAMPUS_CHOICES)

    def __str__(self):
        return f"{self.name}"
