from django import forms


class UploadFileForm(forms.Form):
    tool_change = forms.CharField(max_length=50, initial="M6", label='Tool change code')
    tool_measure = forms.CharField(max_length=50, initial="G119", label='Tool measure code')
    file = forms.FileField()


class TolerancesForm(forms.Form):
    diameter = forms.IntegerField(max_value=50,)

    FEATURE_TYPE_CHOICES = [
        ('shaft', 'shaft'),
        ('hole', 'hole'),
    ]
    feature_type = forms.ChoiceField(
        choices=FEATURE_TYPE_CHOICES,
    )

    TOLERANCE_CLASS_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
        ('13', '13'),
        ('14', '14'),
        ('15', '15'),
        ('16', '16'),
        ('17', '17'),
        ('18', '18'),
    ]
    tolerance_class = forms.ChoiceField(
        choices=TOLERANCE_CLASS_CHOICES,
        initial='7',
    )

    TOLERANCE_LETTER_CHOICES = [
        ('a', 'a'),
        ('c', 'c'),
        ('d', 'd'),
        ('e', 'e'),
        ('f', 'f'),
        ('g', 'g'),
        ('h', 'h'),
        ('j', 'j'),
        ('k', 'k'),
        ('m', 'm'),
        ('n', 'n'),
        ('p', 'p'),
        ('r', 'r'),
        ('s', 's'),
        ]
    tolerance_letter = forms.ChoiceField(
        choices=TOLERANCE_LETTER_CHOICES,
        initial='h',
    )