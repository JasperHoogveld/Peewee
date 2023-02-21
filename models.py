from peewee import *
import os
import sys

#dbase = os.path.join(sys.path[0], 'test_db.db')
#db = SqliteDatabase(dbase) 
db = SqliteDatabase(":memory:") 

class BaseModel(Model):
    class Meta:
        database = db

class Ingredient(BaseModel):
    ingredient_id = IntegerField(primary_key=True)
    name = CharField()
    is_vegetarian = BooleanField()
    is_vegan = BooleanField()
    is_glutenfree = BooleanField()


class Restaurant(BaseModel):
    restaurant_id = IntegerField(primary_key=True)
    name = CharField()
    open_since = DateField(null=True)
    opening_time = TimeField(null=True)
    closing_time = TimeField(null=True)


class Dish(BaseModel):
    dish_id = IntegerField(primary_key=True)
    name = CharField(unique=True)
    served_at = ForeignKeyField(Restaurant)
    price_in_cents = IntegerField()
    ingredients = ManyToManyField(Ingredient)


class Rating(BaseModel):
    rating_id = IntegerField(primary_key=True)
    restaurant = ForeignKeyField(Restaurant)
    rating = IntegerField()
    comment = CharField(null=True)


class DishIngredient(BaseModel):
    dish = ForeignKeyField(Dish)
    ingredient_id = ForeignKeyField(Ingredient)


DishIngredient = Dish.ingredients.get_through_model()


db.connect()
db.create_tables([Restaurant, Rating])
pizza_marios = Restaurant(name = "Marios", closing_time = '22:00', opening_time = '22:00', open_since = 2021)
pizza_marios.save()
marios = Rating(restaurant = pizza_marios, rating = 3)
marios2 = Rating(restaurant = pizza_marios, rating = 5)
marios.save()
marios2.save()
# db.create_tables(Dish)
# pizza = Dish(name="Pizza", served_at = "Marios", price_in_cents=895)
# pizza.save()
# pizza_large = Dish(name="Large Pizza", served_at = "Marios", price_in_cents=1295)
# pizza_large.save()
db.close()
#print(marios.rating)

