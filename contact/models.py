from django.db import models


class Contact(models.Model):
    """ A model for contact form. """
    
    S5 = 5
    S4 = 4
    S3 = 3
    S2 = 2
    S1 = 1
    S0 = 0

    SUBJECT_CHOICES = (
        (S5, 'Option #5'),
        (S4, 'Option #4'),
        (S3, 'Option #3'),
        (S2, 'Option #2'),
        (S1, 'Option #1'),
        (S0, 'Option #0'),
    )

    MR    = 1
    MRS   = 2

    GENDER_CHOICES = (
        (MR, 'MR'),
        (MRS, 'MRS'),
    )

    subject = models.PositiveSmallIntegerField('subject',
        choices=SUBJECT_CHOICES,
        help_text='Choose your subject.'
    )
    gender = models.PositiveSmallIntegerField('gender',
        choices=GENDER_CHOICES,
        help_text='Gender.'
    )
    first_name = models.CharField('first name', max_length=255,
        help_text='First Name.'
    )
    last_name = models.CharField('last name', max_length=255,
        help_text='Last Name.'
    )
    organization = models.CharField('organization', max_length=255, null=True, blank=True,
        help_text='Company / organization.'
    )
    job_title = models.CharField('job title', max_length=255, null=True, blank=True,
        help_text='Job title : CEO, CTO, Software Engineer, Trainee ..'
    )
    phone = models.CharField('phone', max_length=20,
        help_text='Phone.'
    )
    email = models.EmailField('email', max_length=255, unique=True,
        help_text='This email already exists.'
    )
    message = models.TextField('message',
        help_text='Your message.'
    )
    subscribe = models.BooleanField('subscribe', default=False,
        help_text='Would you like to receive our newsletter?'
    )
    cc_myself = models.BooleanField('cc myself', default=False,
        help_text='Send me a copy of the form.'
    )
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ('-created_at',)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
