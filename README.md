# bouba
***No-name*** project for Bouba

![ScreenShot](https://github.com/A-Arari/bouba/blob/master/preview.PNG)

I don't have enough information about the project, but I created it based on some information you gived to me, Bouba.

## To run this project :
  #### Method 1:
  
  I deployed the project on a free host named ***Heroku***
  You can visit this Website at this address : ***[bouba-no-name.com](https://bouba-no-name.herokuapp.com/)***
  
  #### Method 2:
  
  Download [Python 3.7](https://www.python.org/downloads/)
  ```diff
  - make sure to add python to System **PATH** (see [Add Python to the Windows Path](https://geek-university.com/python/add-python-to-the-windows-path/)) 
  ```
  clone this repository using Git or just download it and extract it
  
  open **CMD** and Type:
  
  ```diff
    pip install Django
    cd "{ project path, where there is the manage.py file e.g : cd no-name}"
    python manage.py runserver
  ```
then visit [localhost:8000](https://127.0.0.1:8000)

## About this project :
  Simple ***CRUD***(stands for Create, Retrieve, Update, Delete) project with authentication system (see [django auth](https://docs.djangoproject.com/en/3.0/topics/auth/default/))and search filter.
  Simply, a user should register then login. he will views tutorials posted by other users at the home page.
  A user can :
    - Create new Tutorial
    - Update a Tutorial
    - Delete a Tutorial
    - View a Tutorial
    
```diff    
-notes :
- username and password are case-sensitive
! tutorial url must be a Youtube video and typed like this ('https://www.youtube.com/watch?v=5xInN-fZNnE' OR only the ID 'v=5xInN-fZNnE)
! you can't reset password(because i'm tired now and it takes about 15 minutes with django to get is done)
```

## Oh god, It tooks me 13 hours(in two days) to get this DONE. Fuuuuuuuuck

Thanks at the end!
