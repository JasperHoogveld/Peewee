from lib2to3.pgen2.token import PERCENT
from lib2to3.pygram import python_grammar_no_print_statement
import models
from peewee import *
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want to get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    return (models.Dish.select().order_by(models.Dish.price_in_cents.asc())).first()


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    # query = []
    # for dish in models.Dish.select(models.Dish, models.Ingredient).join(models.Dish.ingredients, 
    #     on=(models.Ingredient.is_vegetarian)):
    #     ingreds = []
    #     for ingred in dish:
    #         ingreds.append(ingred)
    #         if all(ingreds.Ingredient.is_vegetarian):
    #             query.append(dish)

    #for dish in models.Dish.select(models.Dish, models.Ingredient).join()
        
    #return query

 
def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    query = models.Rating.select(models.Rating.restaurant, fn.AVG(models.Rating.rating))
    query = query.group_by(models.Rating.restaurant)
    query = query.order_by(fn.AVG(models.Rating.rating).desc())
    row = query.get()
    print(row.restaurant)
    return query

def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    query = models.Restaurant.select()
    for restaurant in query:
        restaurant.update({models.Restaurant.rating:0})
        restaurant.execute()
        break
    return restaurant.rating


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    vegan_dishes = []
    for dish in models.Dish.select():
        if (models.Dish.select(models.Dish, models.Ingredient)
            .join(models.Ingredient, on=(models.Ingredient.is_vegetarian))
            .where(models.Ingredient.is_vegetarian == True)):
            vegan_dishes.update(dish)
    
    ...


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    ...


print(best_average_rating())