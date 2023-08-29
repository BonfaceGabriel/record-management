from django.urls import path
from .views import RecordsViewSets


urlpatterns = [
    path('all-records/', RecordsViewSets.as_view({'get': 'records_list'}), name='all-records'),
    # path('best-selling-categories/', RecordsViewSets.as_view({'post': 'get_best_selling_categories'}), name='best-sales-categories'),
    # path('best_categories_by_revenue/', RecordsViewSets.as_view({'post': 'get_best_categories_by_revenue'}), name='best-revenue-categories'),
    # path('sales_by_hour/', RecordsViewSets.as_view({'get': 'get_order_hours'}), name='order-by-hour-of-day'),
    # path('sales_by_weekday/', RecordsViewSets.as_view({'get': 'get_orders_by_dayofweek'}), name='order-by-dayofweek'),
    # path('percentage_sales/', RecordsViewSets.as_view({'post': 'get_percentage_change_in_sales'}), name='percentage-sales')

]