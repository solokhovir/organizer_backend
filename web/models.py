from django.db import models


class ToDo(models.Model):
    userID = models.IntegerField('ID пользователя tlg')
    name = models.CharField('Название задачи', max_length=255)
    description = models.TextField('Описание задачи', null=True, blank=True)
    date = models.DateTimeField('Дата и время выполнения')
    # attachments = models.FileField('Вложения', upload_to='./files', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Список задач'
        verbose_name = 'Список задач'
        ordering = ['name']

    def __str__(self):
        return self.name
