from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'title': 'Купить квартиру у моря на Котовского',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/index.html", context)


def contact(request):
    context = {
        'title': 'Контактная инфоормация жилого района "Сады Ривьеры"',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/contact.html", context)


def photo(request):
    context = {
        'title': 'Фото жилого района "Сады Ривьеры"',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/photo.html", context)


def video(request):
    context = {
        'title': 'Видео про жилой район "Сады Ривьеры"',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/video.html", context)


def docs(request):
    context = {
        'title': 'Вся документация и лицензии в "Садах Ривьеры"',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/docs.html", context)


def about(request):
    context = {
        'title': 'Информация о новом жиломрайоне "Сады Ривьеры"',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request, "main/about.html", context)

def apartmentsearch(request):
    context = {
        'title':'Тут вы можете подобрать себе квартиру',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request,"main/apartmentsearch.html", context)

def genplan(request):
    context = {
        'title':'Тут вы можете подобрать себе квартиру',
        # 'username':'vall',
        # 'is_promotion':True,
    }
    return render(request,"main/genplan.html", context)

