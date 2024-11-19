
class RUS:
    _id = 1
    # platform
    title = "Главная страница"
    store = "Магазин"
    main_link = "Главная"
    cart = "Корзина"


    #store
    store_title = "Игры"
    store_games = ["Atomic Heart",
               "Cyberpank 2077",
               "Payday 2"
               ]
    store_buy = "Купить"
    store_return_btn = "Вернуться обратно"

    #cart
    cart_empty = "Извините, но ваша корзина пуста"
    cart_lang = "Сменить язык"



class ENG:
    _id = 2
    # platform
    title = "Main page"
    store = "Store"
    main_link = "Main page"
    cart = "Cart"


    #store
    store_title = "Games"
    store_games = ["Atomic Heart",
                   "Cyberpank 2077",
                   "Payday 2"
                   ]
    store_buy = "Buy now"
    store_return_btn = "Go back"

    #cart
    cart_title = "Sorry, your cart is empty"
    cart_lang = "Switch language"

all_langs = {"Русский": RUS,
         "English": ENG}


print(list(all_langs.keys()), "=========")
