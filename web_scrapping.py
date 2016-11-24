from bs4 import BeautifulSoup
import requests

def initial_data(url):
    food_links=[]
    r  = requests.get("http://" +url)
    data = r.text 
    soup = BeautifulSoup(data,'lxml')
    for link in soup.find_all('a'):
        if(link.get('href').startswith('/food/')):
            food_links.append(link.get('href'))
    return food_links

def extract_recipes_links(home_link,urls):
    food_links=[]
    for link in urls:
        url=home_link+link
        r  = requests.get("http://" +url)
        data = r.text 
        soup = BeautifulSoup(data,'lxml')
        for link in soup.find_all('a'):
            if(link.get('href').startswith('/food/recipes')):
                food_links.append(link.get('href'))
    food_links=set(food_links)
    food_links=list(food_links)
    return food_links

def extract_other_links(url):
    food_links=[]
    r  = requests.get("http://" +url)
    data = r.text 
    soup = BeautifulSoup(data,'lxml')
    for link in soup.find_all('a'):
        if(link.get('href').startswith('/food/')):
            food_links.append(link.get('href'))
    return food_links
  
def add_list(L1,L2):
    for element in L2:
        L1.append(element)
    return L1


def extract_ingredient_urls():
    initial_link='www.bbc.co.uk/food/ingredients'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "/food/ingredients/by/letter/" in link:
            ingredient_url=home_link+link
            array=extract_other_links(ingredient_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link

def save_all_links_ingredients():
    home_link='www.bbc.co.uk'
    urls=extract_ingredient_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()
        
def extract_chef_urls():
    initial_link='www.bbc.co.uk/food/chefs/'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "/food/chefs/by/letters/" in link:
            chef_url=home_link+link
            array=extract_other_links(chef_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link

def extract_season_urls():
    months=['january','february','march','april',
           'may','june','july','august','september',
           'october','november','december']
    initial_link='www.bbc.co.uk/food/seasons/'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        for month in months:
            if month in link:
                month_url=home_link+link
                array=extract_other_links(month_url)
                every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link

def extract_occassion_urls():
    initial_link='www.bbc.co.uk/food/occasions'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "occasions" in link:
            occasion_url=home_link+link
            array=extract_other_links(occasion_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link
    
def save_all_links_occasions():
    home_link='www.bbc.co.uk'
    urls=extract_occassion_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links3.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()
    
def save_all_links_months():
    home_link='www.bbc.co.uk'
    urls=extract_season_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links2.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()
    
def save_all_links_chefs():
    home_link='www.bbc.co.uk'
    urls=extract_chef_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links2.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()

def extract_cuisines_urls():
    initial_link='www.bbc.co.uk/food/cuisines/'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "cuisines" in link:
            occasion_url=home_link+link
            array=extract_other_links(occasion_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link
      
def save_all_links_cuisines():
    home_link='www.bbc.co.uk'
    urls=extract_cuisines_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links4.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()
    
def extract_dishes_urls():
    initial_link='www.bbc.co.uk/food/dishes'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "/food/dishes/by/letter/" in link:
            ingredient_url=home_link+link
            array=extract_other_links(ingredient_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link

def save_all_links_dishes():
    home_link='www.bbc.co.uk'
    urls=extract_dishes_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links5.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()

def extract_programmes_urls():
    initial_link='www.bbc.co.uk/food/programmes'
    home_link='www.bbc.co.uk'
    links=initial_data(initial_link)
    every_link=[]
    for link in links:
        if "programmes" in link:
            ingredient_url=home_link+link
            array=extract_other_links(ingredient_url)
            every_link=add_list(every_link,array)
        
    every_link=set(every_link)
    every_link=list(every_link)
    return every_link

def save_all_links_programs():
    home_link='www.bbc.co.uk'
    urls=extract_programmes_urls()
    l=extract_recipes_links(home_link,urls)
    file_name='links6.txt'
    target=open(file_name,'w')
    for link in l:
        target.write(link)
        target.write('\n')
    target.close()
    
def run():
    home_link='www.bbc.co.uk'
    save_all_links_ingredients()
    print (" Done with Recipes related to Ingredients")
    time.sleep(60)
    save_all_links_occasions()
    print (" Done with Recipes related to Occassion")
    time.sleep(60)
    save_all_links_months()
    print (" Done with Recipes related to Seasons")
    time.sleep(60)
    save_all_links_chefs()
    print (" Done with Recipes related to Chefs")
    time.sleep(60)
    save_all_links_cuisines()
    print (" Done with Recipes related to Cuisines")
    time.sleep(60)
    save_all_links_dishes()
    print (" Done with Recipes related to Dishes")
    time.sleep(60)
    total_recipe_links=[]
    file1='links.txt'
    file2='links1.txt'
    file3='links2.txt'
    file4='links3.txt'
    file5='links4.txt'
    file6='links5.txt'
    target1=open(file1,'r')
    target2=open(file2,'r')
    target3=open(file3,'r')
    target4=open(file4,'r')
    target5=open(file5,'r')
    target6=open(file6,'r')
    for line in target1:
        total_recipe_links.append(home_link+line)
    for line in target2:
        total_recipe_links.append(home_link+line)
    for line in target3:
        total_recipe_links.append(home_link+line)
    for line in target4:
        total_recipe_links.append(home_link+line)
    for line in target5:
        total_recipe_links.append(home_link+line)
    for line in target6:
        total_recipe_links.append(home_link+line)
    target1.close()
    target2.close()
    target3.close()
    target4.close()
    target5.close()
    target6.close()
    total_recipe_links=set(total_recipe_links)
    total_recipe_links=list(total_recipe_links)
    total_recipe_links=make_clean_links(total_recipe_links)
    name='links_all_recipes.txt'
    f=open(name,'w')
    for link in total_recipe_links:
        f.write(link)
        
    f.close()
    print (len(total_recipe_links))

def make_clean_links(links):
    for link in links:
        if "search" in link or "share" in link or "shopping-list" in link:
            links.remove(link)
    return links
    
