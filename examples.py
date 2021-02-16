from pyrecipepuppy import RecipePuppy
import pprint

if __name__ == '__main__':
    rp = RecipePuppy()
    recipes = rp.get_recipes(ingredients='salmon,onions,cheese', search_query='omelet')
    print(f'Some fancy omelets')
    pprint.pprint(recipes)
    print(f'Easy dinners with tuna, lettuce and avocado')
    recipes = rp.get_recipes(ingredients='tuna,lettuce,avocado')
    pprint.pprint(recipes)