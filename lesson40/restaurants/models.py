from django.db import models

# Create your models here.


class Restaurants(models.Model):
    name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    web_site = models.CharField(max_length=25, blank=True)
    telephone_number = models.CharField(max_length=25)

    @classmethod
    def work_out(cls, request):
        def change_restaurant(cls, post):
            cls.objects.filter(id=post['restaurant_id']).update(
                name=post['name'],
                specialization=post['specialization'],
                address=post['address'],
                web_site=post['web_site'],
                telephone_number=post['telephone_number'],
            )

        def delete(cls, post):
            cls.objects.get(id=post['restaurant_id']).delete()

        def add(cls, post):
            cls.objects.create(
                name=post['name'],
                specialization=post['specialization'],
                address=post['address'],
                web_site=post['web_site'],
                telephone_number=post['telephone_number'],
            )

        commands = {
            'change_restaurant': change_restaurant,
            'delete': delete,
            'add': add,
        }        

        if request.method == 'POST':
            post = request.POST
            commands[post['command']](cls, post)

        elif request.method == 'GET':
            get = request.GET
            if 'command' in get:
                if get['command'] == 'select':
                    specialization = get['specialization']
                    return cls.objects.filter(specialization=specialization).all()
        return cls.objects.all()