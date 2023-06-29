from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page


class HomePage(Page):
    """A page representing a student hostel."""
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    capacity = models.IntegerField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('address'),
        FieldPanel('capacity'),
        FieldPanel('name'),
        # ImageChooserPanel('image'),
    ]
    # template = "home/hostel_page.html"


class HostelPage(Page):
    """A page representing a student hostel."""
    template = "hostel/hostel_page.html"
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    capacity = models.IntegerField(max_length=5, default=0,blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('address'),
        FieldPanel('capacity'),
        # ImageChooserPanel('image'),
    ]
    # template = "home/hostel_page.html"

class Room(models.Model):
    """A model representing a room in the hostel."""
    hostel = models.ForeignKey(HostelPage, on_delete=models.CASCADE, related_name='rooms')
    room_number = models.CharField(max_length=10, blank=True)
    capacity = models.IntegerField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('room_number'),
        FieldPanel('capacity'),
    ]