from django.db import models
import datetime


TYPE = (
    ('Company', 'Empresa'),
    ('Agency', 'Agência'),
    ('HR/Recruitment', 'RH/Recrutamento'),
)

STATUS = (
    ('A','Active'),
    ('D','Deactivated'),
    ('N','NeverVisited'),
)
class OpenPosition(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    description = models.CharField(max_length=200, verbose_name='Description')
    tags = models.CharField(max_length=200, blank=True)
    technologies = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=[('Open', 'Open'), ('Closed', 'Closed')])
    url = models.URLField()

    def __str__(self):
        return self.title
class Company(models.Model):

    name = models.CharField(max_length=200, verbose_name='Name')
    description = models.TextField(verbose_name='Description')
    type = models.CharField(max_length=50, choices=TYPE, verbose_name='Type', default='HR/Recruitment')
    url = models.CharField(max_length=100, verbose_name='URL')
    rating = models.IntegerField(max_length=2, verbose_name='Rating')
    status = models.CharField(max_length=2, choices=STATUS, verbose_name='Status', default='N')
    website_screenshot = models.ImageField(upload_to='website_screenshots/', blank=True, null=True)
    date_creation = models.DateField(auto_now_add=True, verbose_name='Date Creation', blank=True)
    last_modified = models.DateField(auto_now_add=True, verbose_name='Last Modified', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
