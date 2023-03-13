from django.db import models
from django.utils.translation import gettext as _

from assessments.models import Assessment



class Question(models.Model):
    
    content = models.CharField(_('Question Content'), max_length=500, blank=False, null=False)
    class Meta:
        abstract =True

class MCQuestion(Question):
    assessment = models.ForeignKey(Assessment, on_delete=models.PROTECT, related_name='mc_questions')


    def check_if_correct(self, guess):
        choice = Choice.objects.get(id=guess)
        if choice.is_correct is True:
            return True
        return False

    def get_choices(self):
        return Choice.objects.filter(question=self)
    
    class Meta:
        verbose_name = _('Multiple Choice Question')
        verbose_name_plural = _('Multiple Choice Questions')
    
    def __str__(self):
        return f'{self.id}-{self.content}'
    

class Choice(models.Model):
    question = models.ForeignKey(MCQuestion, on_delete=models.PROTECT, related_name='choices')

    content = models.CharField(_('Content'), max_length=100, blank=False, null=False)

    is_correct = models.BooleanField(
        default=False, 
        help_text=_("Is this correct answer?"), 
        verbose_name=_("Is Correct")
    )

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("Choice")
        verbose_name_plural = _("Choices")



# =================True False Question==================

class TFQuestion(Question):
    assessment = models.ForeignKey(
        Assessment, 
        on_delete=models.PROTECT, 
        related_name='tf_questions',
        verbose_name=_('Assessment')
    )
    is_true = models.BooleanField(default=False, help_text='Is this true')


    def check_if_true(self, guess):

        if guess == self.is_true:
            return True
        return False
    
    def __str__(self):
        return f'{self.id}-{self.content}'
    

    class Meta:
        verbose_name = _("True False Question")
        verbose_name_plural = _("True False Questions")


# ==================Short Answer Question=================
class SAQuestion(Question):
    assessment = models.ForeignKey(
        Assessment,
        on_delete = models.PROTECT,
        related_name = "sa_questions",
        verbose_name = _("Assessment")
    )
    
    def __str__(self):
        return f'{self.id}-{self.content}'
    
    class Meta:
        verbose_name = "Short Answer Question"
        verbose_name_plural = "Short Answer Questions"


class Answer(models.Model):
    """model definition for Answers"""

    question = models.OneToOneField(
        SAQuestion,
        on_delete = models.CASCADE,
        verbose_name = _("Question")
    )

    content = models.TextField(
        _("Content"),
        max_length = 1000,
        blank = False,
        null = False,
        help_text = _("Write down the answer for the Short Answer Question")
    )

    def __str__(self):
        return f'{self.id}-{self.content}'

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")