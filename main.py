from lib2to3.pgen2.token import PERCENT
from lib2to3.pygram import python_grammar_no_print_statement
from models import *
from peewee import *
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> Dish:
    """You want to get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    return (Dish.select().order_by(Dish.price_in_cents.asc())).first()


def vegetarian_dishes() -> List[Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    query = Dish.select(Dish, Ingredient).join(Dish.ingredients, 
        on=(Ingredient.is_vegetarian)).group_by(Dish.dish_id)
    veg_list = []
    for row in query:
        if row.is_vegeterian and row.name not in veg_list:
            veg_list.append(row.name)
        elif not row.is_vegeterian and row.name not in veg_list:
            veg_list.remove(row.name) 

    return veg_list

 
def best_average_rating() -> Restaurant:
    """You want to know what restaurant is best

    Query the database to retrieve the restaurant that has the highest
    rating on average
    """
    #return (Rating.select().order_by(Rating.restaurant.asc()))
    #return (Rating.select(Rating.restaurant, Rating.rating, fn.AVG(Rating.rating).over(partition_by=[Rating.restaurant]).alias('cavg')))
    query = Rating.select(Rating.restaurant, fn.AVG(Rating.rating).alias("avg_rating"))
    query = query.group_by(Rating.restaurant)
    query = query.order_by(fn.AVG(Rating.rating).desc())
    row = query.get()

    return row.restaurant.name

def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    # query = Rating.select(Rating.restaurant, Rating.rating)
    # firstRestaurant = query.get()
    # firstRestaurant.update(rating = 1)
    # firstRestaurant = firstRestaurant.order_by(fn.AVG(Rating.rating).alias("avg_rating"))
    # firstRestaurant.save()

    # return firstRestaurant.rating
    

def dinner_date_possible() -> List[Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    vegan_dishes = []
    for dish in Dish.select():
        if (Dish.select(Dish, Ingredient)
            .join(Ingredient, on=(Ingredient.is_vegetarian))
            .where(Ingredient.is_vegetarian == True)):
            vegan_dishes.update(dish)
    
    ...


def add_dish_to_menu() -> Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    ...


print(best_average_rating())