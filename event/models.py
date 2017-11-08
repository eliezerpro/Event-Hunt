from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

from datetime import datetime
# Create your models here.

city_choices = [('DURHAM', 'Durham'), ('RALEIGH', 'Raleigh')]

# now = datetime.strptime(str(timezone.now), "%H:%M")

class EventManager(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=140, unique=True, blank=True, null=True)
    description = models.TextField()
    # Images =
    # music_category = models.CharField(max_length=500)
    # music_sample =
    # dj_name = models.CharField(max_length=500)
    event_start_time = models.TimeField(default=timezone.now)
    event_end_time = models.TimeField(default=timezone.now)
    event_date = models.DateField(default=timezone.now)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("events_app:details", kwargs={'event_slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while EventManager.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()


class EventLocation(models.Model):
    title = models.ForeignKey(EventManager, on_delete=models.CASCADE)
    address = models.CharField(max_length=300)
    zip_code = models.CharField(max_length=10)
    states = models.CharField(default="North Carolina", max_length=20, editable=False)
    city = models.CharField(choices=city_choices, max_length=10, default='Select')

    def __str__(self):
        return self.address


        # import psycopg2
        #
        # try:
        #     conn = psycopg2.connect("dbname='event_hunt' user='postgres' host='localhost' password='stunner'")
        #     cur = conn.cursor()
        #     cur.execute("select * from states")
        #     rows = cur.fetchall()
        #     states_choices = [(j,j) for i in rows for j in i]
        #
        # except:
        #     print ("I am unable to connect to the database")
