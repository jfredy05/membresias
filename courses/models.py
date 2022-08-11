from django.db import models
from django.utils import timezone

class Author(models.Model):
    first_name = models.CharField(("First Name"), max_length=50)
    last_name = models.CharField(("Last Name"), max_length=50)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    
    def __str__(self):
        return self.first_name


def user_directory_path(instance, filename):
    return "courses/{0}/{1}".format(instance.title, filename)

def chapter_directory_path(instance, filename):
    return 'courses/{0}/{1}/{2}'.format(instance.course, instance.title, filename)

def lesson_directory_path(instance, filename):
    return 'courses/{0}/{1}/Lesson #{2}: {3}/{4}'.format(instance.course, instance.chapter, instance.lesson_number, instance.title, filename)


class Course(models.Model):
    authors = models.ManyToManyField(Author, verbose_name=("author"))
    title = models.CharField(("Title"), max_length=100)
    sub_title = models.CharField(("SubTitle"), max_length=100)
    thumbnail = models.ImageField(
        ("Thumbnail"), upload_to=user_directory_path, blank=True, null=True
    )
    video = models.FileField(
        ("Video"), upload_to=user_directory_path, blank=True, null=True
    )
    vimeo_video = models.CharField(
        ("Video Vimeo"), help_text="Vimeo Video ID (optional)",
        blank=True, null=True, max_length=100
    )
    slug = models.SlugField(
        max_length=250, unique_for_date="published", null=False, unique=True
    )
    published = models.DateTimeField(("Published"), default=timezone.now)
    is_active = models.BooleanField(("Is Active"), default=True)

    class Meta:
        ordering = ("-published",)
        verbose_name = ("Course")
        verbose_name_plural = ("Courses")

    def __str__(self):
        return self.title


class Chapter(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    chapter_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=chapter_directory_path)
    video = models.FileField(upload_to=chapter_directory_path)
    vimeo_video = models.CharField(help_text="Vimeo Video ID (Optional)",max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:chapter-detail", kwargs={
            'course_slug': self.course.slug,
            'chapter_number': self.chapter_number,
        })


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,blank=True, null=True)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE,blank=True, null=True)
    lesson_number = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to=lesson_directory_path, default='courses/default.jpg')
    video = models.FileField(upload_to=lesson_directory_path)
    vimeo_video = models.CharField(verbose_name="Vimeo Video ID (Optional)", max_length=100, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title