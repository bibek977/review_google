from django.db import models

MinRatings = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

DateFormat = [
    ('my', 'Month-Year'),
    ('ymd', 'Year-Month-Day'),
    ('mdy', 'Month-Day-Year'),
    ('hide', 'Hide'),
]

Align = [
    ('left', 'Left'),
    ('center', 'Center'),
    ('right', 'Right'),
]

Theme = [
    ('light', 'Light'),
    ('dark', 'Dark'),
    ('transparent', 'Transparent'),
    ('custom', 'Custom'),
]

class SettingsPreview(models.Model):
    previewId = models.IntegerField()
    HideReviewsWithoutComments = models.BooleanField()
    HideRatingText = models.BooleanField()
    ShowReviewersPhoto = models.BooleanField()
    ShowReviewersName = models.BooleanField()
    ShowViewAllReviewsLink = models.BooleanField()
    ShowWriteReviewButton = models.BooleanField()
    AutoPlay = models.BooleanField()
    EnableHyperLink = models.BooleanField()
    minratings = models.CharField(choices=MinRatings,max_length=100)
    dateformat = models.CharField(choices=DateFormat,max_length=100)
    align = models.CharField(choices=Align,max_length=100)
    theme = models.CharField(choices=Theme,max_length=100)
    cardbody = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    cardbg = models.CharField(max_length=100)


