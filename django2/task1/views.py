from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from task1.lang_platform import all_langs as localization
import task1.helper as helper
from django.shortcuts import redirect

from task1.forms import ContactForm

print(localization)

chosen_lang = "Русский"
context = dict(localization[chosen_lang].__dict__)



def platform(request):

    return render(request, 'platform.html', context)


def games(request):
    games = helper.get_games()

    context.update({"games": games})
    return render(request, 'store.html', context)


def cart(request):
    return render(request, 'cart.html', context)


def lang(request):

    global chosen_lang
    global context
    list_lang = list(localization.keys())

    if request.method == 'GET':
        lang = request.GET.get('lang', '')
        if lang in list_lang:
            chosen_lang = lang
            context = dict(localization[chosen_lang].__dict__)

    context.update({"universal_langs": list_lang})

    return render(request, 'lang.html', context)


users = helper.get_users_from_db()



def get_info(object, print=False):
    data = ["username", "password", "password_2", "age"]
    return_list = []

    for i in data:
        try:
            return_list.append(object(i))
        except:
            return_list.append(object[i])

    return return_list


def carry_on(data=None, request=None, form=None):
    global users

    username = False
    password = False
    age = False

    print(users)

    if data[0] not in users:
        username = True

    if data[1] == data[2]:
        password = True

    try:
        age_ = int(data[3])
    except:
        age_ = 0

    if age_ >= 18:
        age = True

    if username == password == age:
        global user__
        helper.add_user_to_db(data[0], data[1], data[3])
        user__ = [username, hash(password), age]
        return redirect('/platform')


    error = []

    if not age:
        error.append('Вы должны быть старше 18')
    if not username:
        error.append('Пользователь уже существует')
    if not password:
        error.append('Пароли не совпадают')

    return render(request, 'registration_page.html', {'form': form, "error": error})


def sign_up_by_html(request):
    if request.method == 'POST':
        info_ = get_info(request.POST.get, print=True)
        print(info_)

        return carry_on(data=info_, request=request)

    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            info_ = get_info(request.POST.get, print=True)
            print(info_)

            return carry_on(data=info_, request=request, form=form)
        else:
            print("nooooo")

    return render(request, 'registration_page.html', {'form': form})
