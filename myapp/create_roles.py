#here we create roles and assign permissions to the roles

from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_roles(sender, **kwargs):
    if sender.name != 'myapp':
        return 
    
    roles = ['Manager', 'Staff', 'Customer']

    for role in roles:
        Group.objects.get_or_create(name=role)

    #assign permission
    manager = Group.objects.get(name='Manager')
    staff = Group.objects.get(name='Staff')
    customer = Group.objects.get(name='Customer')

    manager_perms = Permission.objects.filter(
        codename__in=['add_product','change_product','view_product']
    )

    staff_perms = Permission.objects.filter(
        codename__in=['view_product']
    )

    manager.permissions.set(manager_perms)
    staff.permissions.set(staff_perms)
    customer.permissions.clear()