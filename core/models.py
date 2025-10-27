from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, help_text="e.g., 'Web Developer' or 'Data Scientist'")
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Profile (Only one record needed)"

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    percentage_gpa = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        # Include percentage/GPA in the string representation if it exists
        if self.percentage_gpa is not None:
            return f"{self.degree} at {self.institution} ({self.percentage_gpa})"
        return f"{self.degree} at {self.institution}"

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300) 
    url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='certification_badges/', 
        blank=True, 
        null=True, 
        help_text="Upload the certification badge or logo."
    )

    def __str__(self):
        return self.name