# from django import forms


# class StudentRegistration(forms.Form):
#     S_GENDER = (('M', 'MALE'),
#                 ('F', 'FEMALE'),)

#     S_FORMS = (('form1', 'FORM ONE'),
#                ('form2', 'FORM TWO'),
#                ('form3', 'FORM THREE'),)

#     studentid = forms.CharField(label='Student ID', max_length=20)
#     studentname = forms.CharField(label='Student Name', max_length=30)
#     studentgender = forms.CharField(
#         label='Student Gender', choices=S_GENDER, max_length=1)
#     studentform = forms.CharField(
#         label='Student Form', choices=S_FORMS, max_length=5)
#     studentImage = forms.ImageField(label='Student Image', )
#     parentName = forms.CharField(label='Parent Name', max_length=30)
#     parentContact = forms.CharField(label='Parent Contact', max_length=30)
#     parentLocation = forms.CharField(label='Parent Location', max_length=30)
#     registrationDate = forms.DateField(
#         label='Registration Date', auto_now_add=True)
