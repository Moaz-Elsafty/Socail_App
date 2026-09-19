from django.db.models.signals import m2m_changed
from django.db.models import F
from django.dispatch import receiver
from .models import Image

@receiver(m2m_changed, sender=Image.users_like.through)
def users_like_changed(sender, instance: Image, action, reverse, pk_set, **kwargs):
    if reverse:
        return # instance is a User here, not an Image which is a not handled side yet
    if action == 'post_add':
        Image.objects.filter(pk=instance.pk).update(total_likes=F('total_likes') + len(pk_set))
    elif action in ('post_remove', 'post_clear'):
        Image.objects.filter(pk=instance.pk).update(total_likes=F('total_likes') - len(pk_set))