from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# # Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class SuperAdmin(models.Model):
    name = models.CharField(max_length = 10,verbose_name="Имя")
    surname = models.CharField(max_length = 10,verbose_name="Фамилия")
    position = models.CharField(max_length = 10,verbose_name="Должность")


class Profile(AbstractUser):
    
    penname= models.CharField(max_length = 21,verbose_name="Псевдоним")
    avatar = models.ImageField(verbose_name='Аватар пользователя',upload_to='static/media/avatars',blank=True)

    birthdate = models.DateField(verbose_name="Дата рождения",null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    def __str__(self):
        return str(self.penname)




class Genre(models.Model):
    role_name = models.CharField(max_length = 20,verbose_name="Название жанра")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.role_name

class Project(models.Model):
    project_name  = models.CharField(max_length = 20,verbose_name="Название проекта",unique=True)
    creation = models.DateTimeField(verbose_name='Время создания',auto_now=True)
    release = models.BooleanField(verbose_name='Релиз', default=False)
    is_public = models.BooleanField(verbose_name='Публичный', default=True) 
    genre = models.ForeignKey(Genre, verbose_name = 'Жанр', on_delete=models.SET_NULL, null=True)        
    description = models.TextField(max_length=200,verbose_name='Описание')
    slug = models.SlugField(null = True)
    lyrics = models.TextField(max_length=3000,verbose_name='Слова песни', null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name,True)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Participants(models.Model):                                                          
    project_id = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, verbose_name = 'Пользователь', on_delete=models.CASCADE)
    role_id = models.ForeignKey(Role, verbose_name = 'Роль', on_delete=models.CASCADE)     

    class Meta:
        verbose_name = 'Участник проекта'
        verbose_name_plural = 'Участники проекта'

class Comment(models.Model):
    author = models.ForeignKey(Profile, verbose_name = 'Пользователь', on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=500,verbose_name='Текст комментария')
    work_note = models.BooleanField(default=False,verbose_name="Рабочая заметка")


    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Instrument(models.Model):
    name = models.CharField(max_length = 20,verbose_name="Инструмент")
    tyoe = models.ForeignKey(InstrumentType, verbose_name = 'Вид', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.name


class Soundtrack(models.Model):
    name = models.CharField(max_length = 21,verbose_name="Название дорожки")
    instrument = models.ForeignKey(Instrument,on_delete=models.SET_NULL,verbose_name = 'Инструмент',null=True)
    author = models.ForeignKey(Profile, verbose_name = 'Пользователь', on_delete=models.CASCADE)
    soundtrack = models.FileField(upload_to='static/media/soundtracks')
    project = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Звуковая дорожка'
        verbose_name_plural = 'Звуковые дорожки'

    def __str__(self):
        return self.name

