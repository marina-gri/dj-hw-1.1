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
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def get_dishes(request, dish):
    for k, v in DATA.items():
        if k == dish:
            ingredients = {}
            servings = request.GET.get("servings")
            if servings is None:
                ingredients = DATA[dish]
            else:
                for key, value in DATA[dish].items():
                    ingredients[key] = value * int(servings)

    context = {
        'dish_name': dish,
        'ingridients': ingredients,
        }

    return render(request, 'calculator/index.html', context)
