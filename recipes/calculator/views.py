from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def ingredients(request):
    serv = int(request.GET.get("servings", 1))

    if 'omlet' in request.path:
        dish = 'omlet'
    elif 'pasta' in request.path:
        dish = 'pasta'
    elif 'butter' in request.path:
        dish = 'butter'

    context = {'recipe': {}, 'dish': dish}
    for i, y in DATA.items():
        if i == dish:
            for k, r in y.items():
                context['recipe'][k] = r * serv
    return render(request, 'calculator/index.html', context)




