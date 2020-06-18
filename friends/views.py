from django.shortcuts import render
from items.models import Friend
from django.contrib.auth.models import User

# Create your views here.
def page(request):
    users = User.objects.all()

    # Find the current users friends
    try:
        friend = Friend.objects.get(current_user=request.user)
        friends = friend.users.all()
    except:
        friends = None

    context = {
        'users': users,
        'friends': friends,
    }

    return render(request, 'friends.html', context)