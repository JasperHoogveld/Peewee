from peewee import *
import os
import sys

dbase = os.path.join(sys.path[0], 'test_db2.db')
db = SqliteDatabase(dbase)
#db = SqliteDatabase(":memory:")


class BaseModel(Model):
    class Meta:
        database = db


class Jos(BaseModel):
    name = CharField()


class Ingredient(BaseModel):
    ingredient_id = IntegerField(primary_key=True)
    name = CharField()
    is_vegetarian = BooleanField(null=True)
    is_vegan = BooleanField(null=True)
    is_glutenfree = BooleanField(null=True)


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
    ingredients = ManyToManyField(Ingredient, backref='dishes')


class Rating(BaseModel):
    rating_id = IntegerField(primary_key=True)
    restaurant = ForeignKeyField(Restaurant)
    rating = IntegerField()
    comment = CharField(null=True)


# class DishIngredient(BaseModel):
#     dish = ForeignKeyField(Dish)
#     ingredient_id = ForeignKeyField(Ingredient)

DishIngredient = Dish.ingredients.get_through_model()


db.connect()
db.create_tables([Rating, Restaurant, Ingredient, Dish, DishIngredient])

pizza_marios = Restaurant(name = "Marios", closing_time = '22:00', opening_time = '22:00', open_since = 2021)
pizza_marios.save()
pizza_luigi = Restaurant(name = "Luigi", closing_time = '22:00', opening_time = '22:00', open_since = 2021)
pizza_luigi.save()
marios = Rating(restaurant = pizza_marios, rating = 3)
marios.save()    
marios2 = Rating(restaurant = pizza_marios, rating = 5)
marios2.save()    
luigi = Rating(restaurant = pizza_luigi, rating = 5)
luigi.save()

tomato = Ingredient(name = "tomato", is_vegetarian = True)
tomato.save()
rocket = Ingredient(name = "rocket", is_vegetarian = True)
rocket.save()
sosig = Ingredient(name = "sosig", is_vegetarian = False)
sosig.save()    
pizza_veg = Dish(name = "veg_pizza", ingredients = [tomato])
pizza_veg.save()
pizza_sosig = Dish(name = "sosig_pizza", ingredients = [tomato, sosig])
pizza_sosig.save()


# rest1 = Restaurant()
# rest1.name = "Mario's"
# # rest1.open_since = '2020-01-01'
# rest1.opening_time = '22:00'
# rest1.closing_time = '22:00'
# rest1.save()

# rest2 = Restaurant.select().first()
# print(rest2.name)

# rat1 = Rating()
# rat1.restaurant = rest2
# rat1.rating = 4
# rat1.save()

# rat2 = Rating(restaurant=rest1, rating=5)
# rat2.save()

# rest2 = Restaurant.select().first()
# print(rest2.name)

# rat3 = Rating.select().first()
# print(rat3.rating)

# ratings = Rating.select(Rating.restaurant, fn.AVG(Rating.rating))
# for rating in ratings:
#     print(repr(rating))

