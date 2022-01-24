# :dress: Fashion Recommender System

***

Personalized product recommendations are the alternative way of navigating through the online shop. More people find products they need. Even if they didn’t think of them. The project is a Website application for fashion recommendation using machine learning with a built-in a recommendation engine which suggests similar products to the given product.

# BRIEF ON RECOMMENDATION SYSTEMS

***
Recommender systems are one of the most successful and widespread applications of machine learning technologies in business. Recommendation systems help to increase the business revenue and help customers to buy the most suitable product for them.
Now, we’ll look towards different types of filtering used by recommendation engines.

## [Content-based filtering](https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd)
  This filtering is based on the description or some data provided for that product. The system finds the similarity between products based on its context or description. The user’s previous history is taken into account to find similar products the user may like.
 
## [Collaborative filtering](https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd)
  The recommendations are done based on the user’s behavior. History of the user plays an important role. For example, if the user ‘A’ likes ‘Coldplay’, ‘The Linkin Park’ and ‘Britney Spears’ while the user ‘B’ likes ‘Coldplay’, ‘The Linkin Park’ and ‘Taylor Swift’ then they have similar interests. So, there is a huge probability that the user ‘A’ would like ‘Taylor Swift’ and the user ‘B’ would like ‘Britney Spears’. This is the way collaborative filtering is done.
  
Two types of collaborative filtering techniques are used:

   ##### [User-User collaborative filtering](https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd)
   ##### [Item-Item collaborative filtering](https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd)
    
    
 <p align="center">
  <h4><strong> Summary : </strong></h4>
  <img src="https://miro.medium.com/max/700/1*mz9tzP1LjPBhmiWXeHyQkQ.png" />
</p>


Note : In the project we will use the approach of Item-Item Collaborative filtering 

# Problem Statement

***

Given a dataset of 180k apparel images from amazon.com we need to recommend the similar product based on the user choice.

The dataset given contains the following elements :

    1. asin  ( Amazon standard identification number)

    2. brand ( brand to which the product belongs to )

    3. color ( Color information of apparel, it can contain many colors) 

    4. product_type_name (type of the apperal, ex: SHIRT/TSHIRT )

    5. medium_image_url  ( url of the image )

    6. title (title of the product.)

    7. formatted_price (price of the product)

We are going to use a total of `Four approaches` for recommending the apparel as following.

```
1.Bag of words model

2.tf-idf model

3.idf model

4.k nearest neighbors (KNN)

```
# DATASETS

***


### [Dataset link](https://www.kaggle.com/ajaysh/women-apparel-recommendation-engine-amazoncom#tops_fashion.json)

# Setup and Configuration

***

#### Jupyter Notebook

to play a little bit with/and test models, and to observe Data pre-processing follow these steps :

    * Run the jupyter notebook by jupyter notebook Fashion_recommender_notebook.ipynb

    * Start executing the cells by Shift+Enter


To run this app, you will need to follow these 3 steps:

#### 1. Requirements
  - a Laptop (obviously 😄)

  - Text Editor or IDE (eg. vscode, PyCharm)

  - [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your Laptop.


#### 2. Install Python and Pipenv
  - [Python3](https://www.python.org/downloads/)
  

  - [Pipenv](https://pipenv-es.readthedocs.io/es/stable/)

#### 3. Local Setup and Running on Windows, Linux and Mac OS

  ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/BouzCS/Fashion_Recommender_System.git

  # Move into project folder
  $ cd Fashion_Recommender_System/App

  # Install from Pipfile
  $ pipenv install -r requirements.txt 

  # Activate the Pipenv shell
  $ pipenv shell

  # Create database tables
  $ python manage.py migrate
  
  # Create superuser account
  $ python manage.py createsuperuser

  # Start server
  $ python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX
  
  
  # Happy Testing 🤗
  ```
# Screenshots of the website

***

Home Page
:-------------------------:
![HomePage](https://github.com/BouzCS/Fashion_Recommender_System/blob/main/Images/Home%20page.jpeg)


Cart page
:-------------------------:
![Cart](https://github.com/BouzCS/Fashion_Recommender_System/blob/main/Images/Cart.jpeg)


Similar Product
:-------------------------:
![Similar Product](https://github.com/BouzCS/Fashion_Recommender_System/blob/main/Images/Product%201.jpeg)


Similar Product
:-------------------------:
![Similar Product](https://github.com/BouzCS/Fashion_Recommender_System/blob/main/Images/Product%202.jpeg)


Similar Product          
:-------------------------:
![Similar Product](https://github.com/BouzCS/Fashion_Recommender_System/blob/main/Images/Product%203.jpeg)


## Status
Project is: _unfinished_

## Futur Features

* Adding a log in _inteface_
* Implement KNN model on the website
* Update UI/UX

## Technologies
* Python
* Javascript
* Jquery 
* Django
* HTML5
* CSS3 
* Bootstrap 5

# CREDITS

[Brief on recommender systems](https://towardsdatascience.com/brief-on-recommender-systems-b86a1068a4dd)
