from django.shortcuts import render, redirect, HttpResponse

def index(request):
	
	products = [
		{'product_id': 1, 'product': 'Dojo T-Shirts', 'price': 19.99},
		{'product_id': 2, 'product': 'Dojo Sweater', 'price': 29.99},
		{'product_id': 3, 'product': 'Dojo Cup', 'price': 4.99},
		{'product_id': 4, 'product': 'Dojo Alogorithm Book', 'price': 49.99}
	]
	request.session['products'] = products

	return render(request, "amadon/index.html")

def checkout(request):
	if request.method=="POST":
		if request.POST['quantity']=="0":
			errMessage = "Please select the amount for your item"
			return render(request, "amadon/index.html", request.session['products'], errMessage)
		else:	
			product_id =  int(request.POST.get('product_id', ''))
			quantity =  request.POST.get('quantity', '0')
			total = 0
			price = 0
			for item in request.session['products']:
				if item['product_id'] == int(product_id):
					price = item['price']
			total = price * float(quantity)
			some_data = {'product_id':product_id, 'total':total, 'quantity':quantity}
			request.session['purchase_data'] = some_data
			return redirect("confirmation/")
	else:	
		return redirect("/")

def confirmation(request):

	return render(request, "amadon/confirmation.html")