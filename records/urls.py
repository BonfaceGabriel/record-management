from django.urls import path
from records import views
from .views import RecordsViewSets


urlpatterns = [
    # path('', views.home, name='home'),
    # # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('record/<str:pk>', views.record, name='record'),
    # path('delete-record/<str:pk>', views.delete_record, name='delete'),
    # path('add-record/', views.add_record, name='add'),
    path('all-records/', RecordsViewSets.as_view({'get': 'records_list'}), name='all-records'),
    path('create-record/', RecordsViewSets.as_view({'post': 'create_record'}), name='create-record'),
    path('publicwifi-count/', RecordsViewSets.as_view({'get': 'get_publicwifi_count'}), name='publicwifi-count'),
    path('publicwifi/', RecordsViewSets.as_view({'get': 'get_publicwifi'}), name='publicwifi'),
    path('lastmile/', RecordsViewSets.as_view({'get': 'get_lastmile'}), name='lastmile'),
    path('lastmile-count/', RecordsViewSets.as_view({'get': 'get_lastmile_count'}), name='lastmile-count'),
    path('update-record/<str:pk>/', RecordsViewSets.as_view({'patch': 'update_record'}), name='update-record'),

    # path('login/', RecordsViewSets.as_view({'post': 'login_user'}), name='login'),
    # path('logout/', RecordsViewSets.as_view({'post': 'logout_user'}), name='logout'),
   
    # path('best-selling-categories/', RecordsViewSets.as_view({'post': 'get_best_selling_categories'}), name='best-sales-categories'),
    # path('best_categories_by_revenue/', RecordsViewSets.as_view({'post': 'get_best_categories_by_revenue'}), name='best-revenue-categories'),
    # path('sales_by_hour/', RecordsViewSets.as_view({'get': 'get_order_hours'}), name='order-by-hour-of-day'),
    # path('sales_by_weekday/', RecordsViewSets.as_view({'get': 'get_orders_by_dayofweek'}), name='order-by-dayofweek'),
    # path('percentage_sales/', RecordsViewSets.as_view({'post': 'get_percentage_change_in_sales'}), name='percentage-sales')

]