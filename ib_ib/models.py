from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class HeroSection(models.Model):
    tagline = models.CharField(max_length=300, help_text="Short tagline shown under your name")
    bio_paragraph1 = models.TextField(help_text="First paragraph in the About section")
    bio_paragraph2 = models.TextField(blank=True, help_text="Second paragraph (optional)")
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    cta_text = models.CharField(max_length=50, default="View My Work", help_text="Button text")
    cta_link = models.CharField(max_length=100, default="/projects/")

    class Meta:
        verbose_name = "Hero / About Section"
        verbose_name_plural = "Hero / About Section"

    def __str__(self):
        return "Hero & About Content"


class Goal(models.Model):
    text = models.CharField(max_length=200, help_text="One goal/drive bullet point")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "About Goal"
        verbose_name_plural = "About Goals"

    def __str__(self):
        return self.text

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Skill Categories"

    def __str__(self):
        return self.name

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100)
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    level = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    proficiency = models.CharField(
        max_length=20,
        choices=PROFICIENCY_CHOICES,
        default='beginner'
    )
    years_of_experience = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        null=True,
        blank=True
    )
    icon = models.CharField(max_length=50, blank=True)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.get_proficiency_display()}"


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.CharField(max_length=300, help_text="Comma-separated tags e.g. Django, Python, CSS")
    link = models.URLField(blank=True, help_text="Live demo or GitHub URL (optional)")
    link_label = models.CharField(max_length=50, default="View project")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def tag_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]


class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="e.g. Bachelor of Science in Information Technology")
    school = models.CharField(max_length=200, help_text="School or institution name")
    year_start = models.CharField(max_length=10, help_text="e.g. 2023")
    year_end = models.CharField(max_length=10, blank=True, help_text="e.g. 2027 or leave blank for 'Present'")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} — {self.school}"

    def year_display(self):
        end = self.year_end if self.year_end else "Present"
        return f"{self.year_start} — {end}"


class ContactInfo(models.Model):
    intro_text = models.TextField(
        default="Whether you have a project in mind, want to collaborate, or just want to say hello — I'd love to hear from you.",
        help_text="Intro paragraph on the left side"
    )
    email = models.EmailField(blank=True)
    linkedin_url = models.URLField(blank=True, help_text="Full LinkedIn profile URL")
    github_url = models.URLField(blank=True, help_text="Full GitHub profile URL")
    instagram_url = models.URLField(blank=True, help_text="Full Instagram profile URL")

    class Meta:
        verbose_name = "Contact Info"
        verbose_name_plural = "Contact Info"

    def __str__(self):
        return "Contact Information"
