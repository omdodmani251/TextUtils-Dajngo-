# Contains Business Logic
# Controller in MVC architecture
from django.http import HttpResponse
from django.shortcuts import render  # this function return the html or any other file as an HttpResponse


def index(request):
    # writing the tags in the HttpResponse in form of string is tire some lets create the templates to make this
    # more easier

    # return HttpResponse('''<h1> Om Dodmani <h1><h2> Python Django Developer <h2><h3> Currently Looking For Jobs <h3>
    #                     <br>
    #                     <span> Contact </span>
    #                     <a href="http://127.0.0.1:8000/contact/"> click </a><br>
    #                     <span> TOP5 Useful Urls </span><a href="http://127.0.0.1:8000/top5/"> click </a>
    #                     ''')

    params = {'name': 'XYZ', 'desc': 'Django Python Developer', 'need': 'Looking For Jobs'}
    return render(request, 'index.html', params)


def contact(request):
    # return HttpResponse('''<b> Email <b>  <p> omdodmani251@gmal.com <p> <br> <b> Phone <b> <p> 9175195711<p><br> <br>
    # <a href="http://127.0.0.1:8000/"> back </a>''')

    params = {'email': 'xyz@gmail.com', 'phone': '8129740917489'}
    return render(request, 'contact.html', params)


def top5urls(request):
    # return HttpResponse('''<span> Facebook :   <a href="https://www.facebook.com/"> click </a> <br>
    # <span> Google : <a href="https://www.google.co.in/"> click </a> <br>
    # <span> Instagram : <a href="https://www.instagram.com/"> click </a> <br>
    # <span> Whatsapp : <a href="https://www.whatsapp.com/"> click </a> <br>
    # <span> Twitter : <a href="https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flang%3Den-in"> click </a>
    # <br> <br>
    # <a href="http://127.0.0.1:8000/"> back </a>
    # ''')

    params = {'Google': 'https://www.google.co.in/',
              'Twitter': 'https://twitter.com/i/flow/login?redirect_after_login=%2F%3Flang%3Den-in',
              'Instagram': 'https://www.instagram.com/',
              'Facebook': 'https://www.facebook.com/'}
    return render(request, 'top5.html', params)


def home(request):
    return render(request, 'Home.html')


def analyze(request):
    input_text = request.POST.get('text', 'default')  # arg1 => name of the html element arg2 => if blank return
    # default value
    remove_punc = request.POST.get('remove_punc', 'off')
    remove_newline = request.POST.get('remove_newline', 'off')
    all_uppercase = request.POST.get('all_uppercase', 'off')
    character_count = request.POST.get('character_count', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    cc_count = None

    analyzed_text = input_text
    purpose = ''

    if remove_punc != 'off':
        purpose = ' Removing Punctuations'
        analyzed_text = ""
        punc = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for i in input_text:
            if i not in punc:
                analyzed_text += i
        input_text = analyzed_text
    else:
        purpose = 'Analyzing Text'
        analyzed_text = input_text

    if remove_newline != 'off':
        purpose += ' Removing New Line'
        analyzed_text = ""
        for char in input_text:
            if char != '\n' and char != '\r':
                analyzed_text += char
        input_text = analyzed_text

    if all_uppercase != 'off':
        purpose += ' All Characters UPPERCASE'
        analyzed_text = ""
        for char in input_text:
            analyzed_text += char.upper()
        input_text = analyzed_text

    if capitalize != 'off':
        analyzed_text = ""
        purpose += ' Capitalize First Letter'
        for words in input_text.split():
            analyzed_text += words.capitalize() + " "
        input_text = analyzed_text

    if character_count != 'off':
        analyzed_text = ""
        cc_count = len(input_text)

    params = {'purpose': purpose, 'analyzed_text': input_text, 'character_count': cc_count}
    return render(request, 'Analyzed.html', params)
