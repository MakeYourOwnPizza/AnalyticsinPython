def get_recipes(keywords):
    recipe_list = list()
    
    # import inside a function to make it standalone
    import requests
    from bs4 import BeautifulSoup
    
    url = "http://www.epicurious.com/search/" + keywords
    response = requests.get(url)
    
    # check the validity of the url
    if not response.status_code == 200:
        return recipe_list
    try:
        # gives us a BeautifulSoup object
        results_page = BeautifulSoup(response.content,'lxml')
        recipes = results_page.find_all('article', class_="recipe-content-card")
        for recipe in recipes:
            recipe_name = recipe.find('a'). get_text()
            recipe_link = "http://www.epicurious.com" + recipe.find('a').get('href')
            
            # sometimes there is no content for the decription, we don't wnat to stuck there
            try:
                recipe_description = recipe.find('p', class_='dek').get_text()
            except:
                recipe_description = ''
                
            # append can only add one single item, so put them inside a tuple
            recipe_list.append((recipe_name,recipe_link,recipe_description))
    except:
        # return the empty list
        return recipe_list
    return recipe_list

def get_recipe_info(recipe_link):
    recipe_dict = dict()
    
    import requests
    from bs4 import BeautifulSoup
    
    try:
        response = requests.get(recipe_link)
        if not response.status_code == 200:
            return recipe_dict
        results_page = BeautifulSoup(response.content,'lxml')
        
        ingredient_list = list()
        prep_steps_list = list()
        
        # look for the ingredients and prep_steps
        for ingredient in results_page.find_all('li',class_="ingredient"):
            ingredient_list.append(ingredient.get_text())
        for prep_step in results_page.find_all('li',class_="preparation-step"):
            prep_steps_list.append(prep_step.get_text().strip())
        
        # put them into the dictionary
        recipe_dict['ingredients'] = ingredient_list
        recipe_dict['preparation'] = prep_steps_list
        return recipe_dict
    except:
        return recipe_dict

def get_all_recipes(keywords):
    results = list()
    
    # get the lists of name, link and description
    all_recipes = get_recipes(keywords)
    
    for recipe in all_recipes:
        # pass the url
        recipe_dict = get_recipe_info(recipe[1])
        # save the recipe name
        recipe_dict['name'] = recipe[0]
        # save the description
        recipe_dict['description'] = recipe[2]
        results.append(recipe_dict)
    return results
