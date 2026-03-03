from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post

from google import genai
from django.http import JsonResponse
import json
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

def feed(request):
    if request.method == "POST" and request.user.is_authenticated:
        Post.objects.create(user=request.user, text=request.POST.get('text'))
        return redirect('feed')



    posts = Post.objects.all()

    # ai posts to summarize
    latest_posts = posts[:5]
    blob = " ".join([p.text for p in latest_posts])

    return render(request, 'feed.html', {'posts': posts, 'all_content_blob': blob })

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log them in after sign up
            return redirect('feed')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('signup')

    # Filter posts to only show those belonging to the current user
    user_posts = Post.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'posts': user_posts})

# Setup the client once
client = genai.Client(api_key=settings.GEMINI_API_KEY)

@csrf_exempt # Simple for prototyping
def summarize_view(request):
    if request.method == "POST" and request.user.is_authenticated:
        data = json.loads(request.body)
        user_text = data.get("content", "")

        # Call the Gemini helper
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=f"Summarize these latest posts into an oracle-like short paragraph: {user_text}"
        )

        return JsonResponse({"summary": response.text})

    return JsonResponse({"error": "Send a POST request."}, status=400)
