from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  


urlpatterns = [
    path('',views.index,name='index'),
    # path('<int:id>', views.view_product,name='view_product'),
    # path('add/',views.add,name='add')

    path('products/',views.product_list,name='prods'),
    path('factorys/',views.factory_list,name='factorys'),
    path('factorys/<int:id>',views.product_factory_list,name='factorys_product'),
    path('factory/<int:id>',views.edit_factory,name='edit_factory'),
    path('products/<int:id>', views.one_product,name='one_product'),
    path('product/<int:id>', views.edit_product,name='edit_product'),
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)