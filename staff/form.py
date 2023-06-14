from django import forms
from . models import Teacher
class TeacherForm(forms.ModelForm):
    RELIGION = [
        ('','Select Your Religion'),
        ('OBC','OBC'),
        ('OEC','OEC'),
        ('General','General')
    ]
    DESOGNATION = [
        ('','Select Your Designation'),
        ('PGT','PGT'),
        ('TGT','TGT'),
        ('PRT','PRT'),
    ]
    GENDER =[
        ('','Select Your Gender'),
        ('Female','Female'),
        ('Male','Male')
    ]
    gender = forms.CharField(
        label='Gender',
        widget = forms.Select(
            choices=GENDER,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    religion = forms.CharField(
        label='Religion',
        widget = forms.Select(
            choices = RELIGION,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    designation = forms.CharField(
        label='designation',
        widget = forms.Select(
            choices = DESOGNATION,
            attrs = {
                'class' : 'form-control'
            }
        )
    )
    class Meta:
        model = Teacher
        fields = "__all__"
        widgets={
            'date_of_birth':forms.DateInput(
                attrs={
                    'style':'font-size:16px;',
                    'type':'date',
                    'onkeydown':'retrun false',
                }
            )
        }
    def __init__(self,*args,**kwargs):
        super(TeacherForm,self).__init__(*args,**kwargs)
        self.fields["name"].required = True
        self.fields["guardian_name"].required = True
        self.fields["email"].required = True
        self.fields["contact_number"].required = True
        self.fields["date_of_birth"].required = True
        self.fields["gender"].required = True
        self.fields["religion"].required = True
        self.fields["photo"].required = True
        self.fields["address"].required = True
        self.fields["state"].required = True
        self.fields["city"].required = True
        self.fields["pincode"].required = True
        self.fields["designation"].required = True
        self.fields["subject"].required = True
        self.fields["languages"].required = True
        self.fields["sslc_certificate_upload"].required = True
        self.fields["sslc_percentage"].required = True
        self.fields["plustwo_certificate_upload"].required = True
        self.fields["plustwo_percentage"].required = True
        self.fields["degree_persentage"].required = True
        self.fields["b_ed_certificate_upload"].required = True
        self.fields["b_ed_persentage"].required = True
        self.fields["m_ed_certificate_upload"].required = True
        self.fields["m_ed_persentage"].required = True
        self.fields["set_certificate_upload"].required = True
        self.fields["net_certificate_upload"].required = True
        self.fields["k_tet_certificate_upload"].required = True
        self.fields["experience"].required = True
        self.fields["cv_upload"].required = True
        self.fields["name"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'name'})
        self.fields["guardian_name"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Guardian name'})
        self.fields["email"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'email'})
        self.fields["contact_number"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Contact Number', 'data-mask': '(00) 00-00'})
        self.fields["date_of_birth"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Date Of Birth'})
        self.fields["gender"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Gender'})
        self.fields["religion"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Religion'})
        self.fields["photo"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'photo'})
        self.fields["address"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Address'})
        self.fields["state"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'State'})
        self.fields["city"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'City'})
        self.fields["pincode"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Pincode'})
        self.fields["designation"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Designation'})
        self.fields["subject"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'Subject'})
        self.fields["languages"].widget.attrs.update({'style': 'font-size:15px', 'placeholder': 'languages'})
        self.fields["sslc_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'SSLC Certificate Upload'})
        self.fields["sslc_percentage"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'SSLC Total Persantage'})
        self.fields["plustwo_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Higher Secondary Certificate Upload'})
        self.fields["plustwo_percentage"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Higher Hecondary Total Percentage'})
        self.fields["degree_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Degree Certificate Upload'})
        self.fields["degree_persentage"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Degree Total Percentage'})
        self.fields["b_ed_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'B ed Certificate upload'})
        self.fields["b_ed_persentage"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'B ed Total Percentage'})
        self.fields["m_ed_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'M ed certificate upload'})
        self.fields["m_ed_persentage"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'M ed Total Percentage'})
        self.fields["set_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Set certificate upload'})
        self.fields["net_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'Net certificate upload'})
        self.fields["k_tet_certificate_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'K tet certificate upload'})
        self.fields["experience"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'experience'})
        self.fields["cv_upload"].widget.attrs.update(
            {'style': 'font-size:15px', 'placeholder': 'CV Upload'})