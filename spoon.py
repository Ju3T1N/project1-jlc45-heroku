import json

def spoon_output():
    output=[]
    with open('default.json') as f:
        data = json.load(f)
        
#the first index is the name of the item
    output.append(data.get('recipes')[0].get('title'))
#the second index is the url of the recipe
    output.append(data.get('recipes')[0].get('spoonacularSourceUrl'))
#the third index is the url of the image
    output.append(data.get('recipes')[0].get('image'))
#fourth index is time to prepare in minutes
    output.append(data.get('recipes')[0].get('readyInMinutes'))
#fifth index is the amount of servings it makes
    output.append(data.get('recipes')[0].get('servings'))
#the 6th index is a list of all of the ingredients
    ingredients=[]
    for item in data.get('recipes')[0].get('extendedIngredients'):
        ingredients.append(item.get('original'))
    output.append(ingredients)
    
    return output