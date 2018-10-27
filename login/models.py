# from edugen.models import *
# from django_countries.fields import CountryField
# from django_countries import countries
#
#
# class Country(models.Model):
#     country = CountryField(choices=list(countries))
#
#     def __unicode__(self):
#         return self.country
#
#
# class Education(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class PrimaryEducation(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Occupation(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Industry(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
#
# class Profile(models.Model):
#     GENDER = (
#         ('', 'Select Gender'),
#         ('1', 'Male'),
#         ('2', 'Female'),
#         ('3', 'Other'),
#     )
#     MARITAL_STATUS = (
#         ('', 'Select marital status'),
#         ('1', 'Single'),
#         ('2', 'Married'),
#         ('3', 'Other'),
#     )
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     gender = models.CharField(choices=GENDER, max_length=100, null=True)
#     status = models.CharField(choices=MARITAL_STATUS, max_length=100, null=True)
#     education = models.ForeignKey(Education, max_length=100, null=True, on_delete=models.CASCADE)
#     primary_education = models.ForeignKey(PrimaryEducation, max_length=100, null=True, on_delete=models.CASCADE)
#     occupation = models.ForeignKey(Occupation, max_length=100, null=True, on_delete=models.CASCADE)
#     industry = models.ForeignKey(Industry, max_length=100, null=True, on_delete=models.CASCADE)
#     primary_learning_objective = models.CharField(max_length=100, null=True)
#     country = models.CharField(max_length=100, null=True, choices=countries)
#     date_of_birth = models.DateField()
#     picture = models.ImageField(upload_to='profile', null=True)
#     text1 = models.TextField(null=True)
#     text2 = models.TextField(null=True)
#
#     def profile_image_tag(self):
#         return format_html('<img href="{0}" src="{0}" width="100" height="100" />'.format(self.image.url))
#
#     profile_image_tag.allow_tags = True
#     profile_image_tag.short_description = 'Image'
