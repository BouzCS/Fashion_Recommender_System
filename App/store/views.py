from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import *
from .models import *
from .utils import cookieCart, cartData, guestOrder
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances

from pathlib import Path



from sqlalchemy import create_engine

cnx = create_engine('sqlite:///db.sqlite3').connect()

df_store_product = pd.read_sql_table('store_product', cnx)


tfidf_title_vectorizer = TfidfVectorizer(min_df = 0)
tfidf_title_features = tfidf_title_vectorizer.fit_transform(df_store_product['name'])
tf_idf_euclidean=[]
def tfidf_model(doc_id, num_results):

        L=[]
        pairwise_dist = pairwise_distances(tfidf_title_features,tfidf_title_features[doc_id])

        indices = np.argsort(pairwise_dist.flatten())[0:num_results]
        pdists  = np.sort(pairwise_dist.flatten())[0:num_results]

        df_indices = list(df_store_product.index[indices])
        for i in range(0,len(indices)):
            L.append(df_store_product['asin'].loc[df_indices[i]])
        return L


idf_title_vectorizer = CountVectorizer()
idf_title_features = idf_title_vectorizer.fit_transform(df_store_product['name'])
def n_containing(word):
    # return the number of documents which had the given word
    return sum(1 for blob in df_store_product['name'] if word in blob.split())

def idf(word):
    # idf = log(#number of docs / #number of docs which had the given word)
    return math.log(df_store_product.shape[0] / (n_containing(word)))
idf_euclidean=[]
def idf_model(doc_id, num_results):
    M=[]
    pairwise_dist = pairwise_distances(idf_title_features,idf_title_features[doc_id])

    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]

    df_indices = list(df_store_product.index[indices])

    for i in range(0,len(indices)):

        M.append(df_store_product['asin'].loc[df_indices[i]])

    return M


title_vectorizer = CountVectorizer()
title_features   = title_vectorizer.fit_transform(df_store_product['name'])
title_features.get_shape()
bag_of_words_euclidean=[]
def bag_of_words_model(doc_id, num_results):

    B=[]
    pairwise_dist = pairwise_distances(title_features,title_features[doc_id])

    # np.argsort will return indices of the smallest distances
    indices = np.argsort(pairwise_dist.flatten())[0:num_results]
    #pdists will store the smallest distances
    pdists  = np.sort(pairwise_dist.flatten())[0:num_results]

    #data frame indices of the 9 smallest distace's
    df_indices = list(df_store_product.index[indices])

    for i in range(0,len(indices)):

        B.append(df_store_product['asin'].loc[df_indices[i]])

    return B


def global_model(doc_id,num_results):
    G= bag_of_words_model(doc_id,num_results) + tfidf_model(doc_id,num_results) + idf_model(doc_id,num_results)
    G = list(dict.fromkeys(G))
    return G


def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()[0:100]
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)

def view(request, product_id):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	G= global_model(product_id-1, 10)
	similars = Product.objects.filter(asin__in=G)
# 	L=tfidf_model(product_id-1, 10)
# 	similars = Product.objects.filter(asin__in=L)
# 	M = idf_model(product_id-1, 10)
# 	similars = Product.objects.filter(asin__in=M)
# 	B = bag_of_words_model(product_id-1, 10)
#     G= global_model(product_id-1, 10)
#
# 	similars = Product.objects.filter(asin__in=G)





	products = Product.objects.filter(id=product_id)
	context = {'products':products, 'cartItems':cartItems, 'product_id':product_id, 'similars':similars}
	return render(request, 'store/view.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)