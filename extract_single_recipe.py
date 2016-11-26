from bs4 import BeautifulSoup
import requests

def extract_prep_time(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = ''
    for tag in rsoup.find_all(itemprop='prepTime'):
        result = tag.contents[0]
    return result
def extract_cooking_time(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = ''
    for tag in rsoup.find_all(itemprop='cookTime'):
        result = tag.contents[0]
    return result
def extract_author(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = ''
    for tag in rsoup.find_all(itemprop='author'):
        result = tag.contents[0]
    return result

def extract_serves(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = ''
    for tag in rsoup.find_all(itemprop='recipeYield'):
        result = tag.contents[0]
    return result

def extract_ingredients(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = []
    for tag in rsoup.find_all(itemprop='ingredients'):
        if len(tag.contents)>1:
            result.append(tag.contents)
        else:
            result.append([tag.contents[0]])
    result=clean_ingredients(result)
    result=join_ingredients(result)
    return result

def extract_method(recipe_url):
    recipe=requests.get(recipe_url)
    rsoup = BeautifulSoup(recipe.text, "lxml")
    result = []
    for tag in rsoup.find_all(itemprop='recipeInstructions'):
        result.append(tag.contents)
    result=clean_method(result)
    final_output=[]
    for instruction in result:
        temp=clean_ind_instruction(instruction)
        final_output.append(temp)
    return final_output
    
def clean_ingredients(ingredients):
    
    for i in range(len(ingredients)):
        for j in range(len(ingredients[i])):
            if 'class' in str(ingredients[i][j]):
                string=str(ingredients[i][j])
                string=clean_string(string)
                ingredients[i][j]=string
    return ingredients
                
def clean_string(string):
    l=string.split('<')
    string=l[1]
    l=string.split('>')
    string=l[1]
    return string

def join_ingredients(ingredients):
    results=[]
    for ingredient in ingredients:
        string=add_ingredient(ingredient)
        results.append(string)
    return results
def add_ingredient(ingredient):
    string=''
    for element in ingredient:
        string=str.join('',(string,element))
    return string

def clean_method(instructions):
    temp=[]
    for i in range(len(instructions)):
        temp.append(str(instructions[i][1]))
        
    return temp
    
def clean_ind_instruction(string):
    l=string.split('<')
    l=l[1].split('>')
    string=l[1]
    return string
    
def collect_all_information(url):
    author=extract_author(url)
    cook=extract_prep_time(url)
    prep=extract_cooking_time(url)
    serves=extract_serves(url)
    ing=extract_ingredients(url)
    method=extract_method(url)
    print (author)
    print (cook)
    print (prep)
    print (serves)
    print (ing)
    print (method)