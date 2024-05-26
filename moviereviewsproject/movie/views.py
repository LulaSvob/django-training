from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Movie, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


def home(request):
    # return HttpResponse('<h1> Welcome to home page</h1>')
    search_term = request.GET.get("search_movie")
    # movies = Movie.objects.all()

    if search_term:
        movies = Movie.objects.filter(title__icontains=search_term)
    else:
        movies = Movie.objects.all()

    return render(request, "home.html", {"search_term": search_term, "movies": movies})


def about(request):
    return HttpResponse("<h1> Welcome to About Page</h1>")


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    reviews = Review.objects.filter(movie=movie)
    return render(request, "detail.html", {"movie": movie, "reviews": reviews})

@login_required
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == "GET":
        return render(
            request, "createreview.html", {"form": ReviewForm(), "movie": movie}
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.movie = movie
            newReview.save()
            return redirect("detail", newReview.movie_id)

        except ValueError:
            return render(
                request,
                "createreview.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )

@login_required
def updatereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    if request.method == "GET":
        form = ReviewForm(instance=review)
        return render(request, "updatereview.html", {"review": review, "form": form})
    else:
        try:
            form = ReviewForm(request.POST, instance=review)
            form.save()
            return redirect("detail", review.movie.id) # type: ignore
        except ValueError:
            return render(
                request,
                "updatereview.html",
                {"review": review, "form": form, "error": "Bad data in form"},
            )

@login_required
def deletereview(request, review_id):
    review = get_object_or_404(Review, pk=review_id, user=request.user)
    review.delete()
    return redirect("detail", review.movie.id) # type: ignore