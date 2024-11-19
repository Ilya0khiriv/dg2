from task1.models import Buyer, Game

def get_users_from_db():

    return Buyer.objects.all()

def add_user_to_db(username, password, age):
    Buyer.objects.create(name=username, balance=0, age=age, hashed_password=hash(password))

def get_games():
    return Game.objects.all()

