from django import forms
from django.core.validators import ValidationError, RegexValidator
import re


def proverka_name(value):
    if (value.isalpha() == False) or (value.istitle() == False):
        raise forms.ValidationError('Имя или Фамилия должны состоять из букв и начинаться с заглавной буквы!')


regex = re.compile(
    r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")


def proverka_mail(email):
    if re.fullmatch(regex, email) == None:
        raise forms.ValidationError('Не соблюдены правила названия email')


class Water(forms.Form):
    name = forms.CharField(label='Имя', validators=[proverka_name])
    surname = forms.CharField(label='Фамилия', validators=[proverka_name])
    mail = forms.EmailField(label="Эл.почта", validators=[proverka_mail])
    tel = forms.CharField(label='Моб.телефон',
                          validators=[RegexValidator('[+7][0-9]{10}', message='неправильный телефон')])
    adr = forms.CharField(label='Адрес')
    one_time = (('1 месяц', '1 мес'), ('3 месяца', '3 мес'), ('6 месяцев', '6 мес'), ('12 месяцев', '12 мес'))
    time = forms.TypedChoiceField(label='Срок договора', choices=one_time)
    one_volume = (('5 литров', '5 л'), ('10 литрова', '10 л'), ('15 литров', '15 л'))
    volume = forms.TypedChoiceField(label='Объем поставки', choices=one_volume)
