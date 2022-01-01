from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class ExamCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ExamTitle(models.Model):
    class Meta:
        verbose_name = _("Exam")
        verbose_name_plural = _("ExamTitle")
        ordering = ["id"]

    title = models.CharField(
        max_length=255, default=_("New Exam"), verbose_name=_("Exam Title")
    )
    category = models.ForeignKey(ExamCategory, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(verbose_name=_("Last Updated"), auto_now=True)

    class Meta:
        abstract = True


class ExamQuestion(Updated):
    class Meta:
        verbose_name = _("ExamQuestion")
        verbose_name_plural = _("ExamQuestions")
        ordering = ["id"]

    TYPE = ((0, _("Multiple Choice")),)
    exam = models.ForeignKey(
        ExamTitle, related_name="examquestion", on_delete=models.DO_NOTHING
    )
    technique = models.IntegerField(
        choices=TYPE, default=0, verbose_name=_("Type of Question")
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    date_created = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Date Create")
    )
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

