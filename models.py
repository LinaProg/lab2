from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

# # Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
# from .. import settings
# class MyAccountManager(BaseUserManager):
#     def create_user(self, username,email,firstname,lastname, password, penname):
#         if not email:
#             raise ValueError('Необходимо ввести электронную почту')
#         if not username:
#             raise ValueError('Пользователю необходим лгин')
#         if not penname:
#             penname = f"{firstname} {lastname}"
#         user = self.model(
#             email=self.normalize_email(email),
#             user_login=username,
#             lastname = lastname,
#             first_name = firstname,
#             penname = penname
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, username,email,firstname,lastname, password, penname):
#         user = self.create_user(
#             email=email,
#             password=password,
#             username=username,
#             firstname=firstname,
#             lastname=lastname,
#             penname=penname
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class Profile(AbstractUser):
    
    penname= models.CharField(max_length = 21,verbose_name="Псевдоним")
    avatar = models.ImageField(verbose_name='Аватар пользователя',upload_to='static/media/avatars',blank=True)
    # firstname = models.CharField(max_length = 10,verbose_name="Имя")
    # lastname = models.CharField(max_length = 10,verbose_name="Фамилия")
    birthdate = models.DateField(verbose_name="Дата рождения",null=True)
    # user_login = models.CharField(max_length = 30,verbose_name="Логин",unique=True)
    # email = models.EmailField(verbose_name="Электронная почта", max_length = 60, unique=True)
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


    # USERNAME_FIELD = 'user_login'
    # REQUIRED_FIELDS = ['email','firstname','lastname']

    def __str__(self):
        return str(self.penname)

    # objects = MyAccountManager()

    # def has_perm(self, perm, obj=None):
    #     return self.is_admin

    # def has_module_perms(self, app_label):
    #     return True


class Role(models.Model):
    role_name = models.CharField(max_length = 10,verbose_name="Название роли")

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    def __str__(self):
        return self.role_name

class Genre(models.Model):
    role_name = models.CharField(max_length = 20,verbose_name="Название жанра")

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.role_name

# class Lyrics(models.Model):
#     lyrics = models.TextField(max_length=3000,verbose_name='Слова песни', null=True)
#     # project = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)

#     class Meta:
#         verbose_name = 'Текст песни'

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


# class Versions(models.Model):
#     project_id = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)
#     change_date = models.DateTimeField(verbose_name = 'Время внесения изменения',auto_now=True)

#     class Meta:
#         verbose_name = 'Версия'
#         verbose_name_plural = 'Версии'

# class ProjectNote(models.Model):
#     author = models.ForeignKey(Profile, verbose_name = 'Пользователь', on_delete=models.CASCADE)
#     project_id = models.ForeignKey(Project, verbose_name = 'Проект', on_delete=models.CASCADE)
#     note_text = models.TextField(max_length=500,verbose_name='Текст заметки')
#     version_id = models.ForeignKey(Versions,on_delete=models.CASCADE,verbose_name = 'Версия проекта')

#     class Meta:
#         verbose_name = 'Заметка по проекту'
#         verbose_name_plural = 'Заметки по проекту'



# class LyricsVersion(models.Model):
#     version = models.ForeignKey(Versions,on_delete=models.CASCADE,verbose_name = 'Версия проекта')
#     lyrics = models.ForeignKey(Lyrics,on_delete=models.CASCADE,verbose_name = 'Слова')

#     class Meta:
#         verbose_name = 'Версия текста'
#         verbose_name_plural = 'Версии текста'

class Instrument(models.Model):
    name = models.CharField(max_length = 20,verbose_name="Инструмент")

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

# class SoundtrackVersion(models.Model):
#     version = models.ForeignKey(Versions,on_delete=models.CASCADE,verbose_name = 'Версия проекта')
#     lyrics = models.ForeignKey(Soundtrack,on_delete=models.CASCADE,verbose_name = 'Слова')

#     class Meta:
#         verbose_name = 'Версии звуковых дорожек'