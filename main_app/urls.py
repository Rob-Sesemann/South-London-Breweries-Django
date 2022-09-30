from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name='about'),
    path('breweries/', views.breweries_index, name='index'),
    path('breweries/<int:brewery_id>', views.breweries_detail, name='detail'),

    path('breweries/create/', views.BreweryCreate.as_view(), name='breweries_create'),
    path('breweries/<int:pk>/update/', views.BreweryUpdate.as_view(), name='breweries_update'),
    path('breweries/<int:pk>/delete/', views.BreweryDelete.as_view(), name='breweries_delete'),

    path('breweries/<int:brewery_id>/add_specialbrew/', views.add_specialbrew, name='add_specialbrew'),

    # Paths for CRUD operations in Torebrews
    path('corebrews/', views.CorebrewList.as_view(), name='corebrews_index'),
    path('corebrews/<int:pk>/', views.CorebrewDetail.as_view(), name='corebrews_detail'),

    path('corebrews/create/', views.CorebrewCreate.as_view(), name='corebrews_create'),
    path('corebrews/<int:pk>/update/', views.CorebrewUpdate.as_view(), name='corebrews_update'),
    path('corebrews/<int:pk>/delete/', views.CorebrewDelete.as_view(), name='corebrews_delete')
]