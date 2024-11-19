from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    age = models.PositiveIntegerField(default=0)
    hashed_password = models.CharField(max_length=100000, default="")

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added max_digits and decimal_places
    size = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Added max_digits and decimal_places
    description = models.TextField(default="No")  # Added parentheses to call the constructor
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)


    def __str__(self):
        return self.title



# game1 = Game.objects.create(title='Mario', cost=100, size=1024, description='lol a game', age_limited=False)
# game2 = Game.objects.create(title='Mario Revenge', cost=120, size=10324, description='lol a game', age_limited=True)
# game3 = Game.objects.create(title='Mario Vengence', cost=140, size=102344, description='lol a game', age_limited=True)
#
# buyer1 = Buyer.objects.create(name="Cole", balance=1000, age=16)
# buyer2 = Buyer.objects.create(name="Sam", balance=1200, age=19)
# buyer3 = Buyer.objects.create(name="Liam", balance=2000, age=23)
#
#
# game1.buyer.set([buyer3, buyer2, buyer1])
# game2.buyer.set([buyer3, buyer2])
# game3.buyer.set([buyer3])

