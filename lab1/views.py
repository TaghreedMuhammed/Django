from django.shortcuts import render
from django.http import HttpResponse

# Your product_list data
product_list = [
    {'id': 1, 'Name': 'Women Shoes', 'Image': 'convwomen.jpg', 'category':'Women'},
    {'id': 2, 'Name': 'Women Shoes', 'Image': 'convwomen2.jpg','category':'Women'},
    {'id': 3, 'Name': 'Men Shoes', 'Image': 'nikemen1.jpg','category':'Men'},
    {'id': 4, 'Name': 'Men Shoes', 'Image': 'nikemen2.jpg','category':'Men'},
]

def products(request):
    context = {'product_list': product_list}
    return render(request, 'index.html', context)

def category(request):
    context = {'product_list': product_list}
    return render(request, 'category.html', context)
    
    # if product:
    #     return render(request, 'product_details.html', context)
    # else:
    #     return HttpResponse('<h3>Product Is Not Found</h3>')

def aboutUs(request):
    return render(request, 'about.html')


    
  
    
