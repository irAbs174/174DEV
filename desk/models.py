from django.db import models

class Newsletter_Subscribe(models.Model):
    lang = models.CharField(max_length=3, verbose_name='زبان کاربر',null=False, blank=False )
    email = models.CharField(max_length=40, verbose_name='رایانامه',null=False, blank=False )
    join_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت', blank=True, null=True)

    objects = models.Manager()

    class Meta:
        verbose_name = 'عضو خبرنامه'
        verbose_name_plural = 'اعضای خبرنامه'

    def __str__(self):
        return self.email