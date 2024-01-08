from django.urls import path
from .import views

urlpatterns = [
    path('userregistration/',views.UserRegisteration.as_view(),name="UserRegistration"),
    path('userlogin/',views.UserSignIn.as_view(),name="userLogin"),
    path('userInformation/',views.userInformationSection.as_view(),name="UserInformationSectionForRoute"),
    path('userContent/',views.ContextCreation.as_view(),name="UserContext"),
    
    
]
