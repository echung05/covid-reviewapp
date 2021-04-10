from django.urls import path
from . import views, auth

app_name = 'changed'
urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('signup/register/',auth.registerUser,name='register'),
    path('signup/',views.signup,name='signup'),
    path('authenticate/',auth.auth,name='authenticate'),
    path('logout/',auth.logout,name='logout'),
    #displays directory of businesses with links to reviews
    path('review_processing/',views.writeReview,name='processreview'),
    #shows comments/reviews for one particular business
    path('reviews',views.show_reviews,name='specificreview'),
    path('profile/<str:username>',views.profile,name='profile'),
    path('reply/<int:business_info_id>',views.reply,name='reply'),
    path('processreply/',views.processReply,name='processReply'),
]