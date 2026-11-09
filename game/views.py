from django.shortcuts import render

# Create your views here.
import random
from django.shortcuts import render

def guessing_game(request):
    # create secret number first time
    if 'secret' not in request.session:
        request.session['secret'] = random.randint(1, 20)
        request.session['attempts'] = 0

    message = ""
    if request.method == "POST":
        guess = int(request.POST.get('guess'))
        request.session['attempts'] += 1
        secret = request.session['secret']

        if guess > secret:
            message = "Too High"
        elif guess < secret:
            message = "Too Low"
        else:
            message = f"Correct! The number was {secret}"
            del request.session['secret'] # reset game

        if request.session['attempts'] >= 5 and message != f"Correct! The number was {secret}":
            message = f"Game over. Number was {secret}"
            del request.session['secret']

    return render(request, 'game/index.html', {'message': message})
