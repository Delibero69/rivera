from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
            'title':'Купить квартиру у моря на Котовского',
            # 'username':'vall',
            # 'is_promotion':True,
        }
    return render(request, "main/index.html",context)


# def index(request):
#     # context = {
#     #     'title':'Store',
#     #     # 'username':'vall',
#     #     # 'is_promotion':True,
#     # }
#     return render(request,"main/index.html")

# def products(request):
#     # context = {
#     #     'title':'Store - Каталог',
#     #     'products': Product.objects.all(),
#     #     'categories':ProductCategory.objects.all(),
#     # }
#     return render(request,'main/products.html')