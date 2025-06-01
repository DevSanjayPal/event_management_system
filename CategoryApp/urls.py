from django.urls import path
from .views import *

urlpatterns = [
    path('category/<int:catId>/',numkeenview ,name='categoryurl'),
    path('shop/<int:subCatId>/',shopview ,name='shopurl'),
    path('SubCategoryView/<int:catId>/',SubCategoryView ,name='SubCategoryView'),
    path('shop_filter/<str:subCatId>/<str:start>/<str:end>/',shopFilterview ,name='shopNewurl'),
    path('numkeen/',numkeenview ,name='numkeenurl'),
    path('productdetail/<int:id>/',userproductdetailview ,name='productdetailurl'),
    path('product_detail/<int:id>/',user_productdetailview ,name='product_detailurl'),
    path('cart/',cartview,name='carturl'),
    path('checkout/',checkoutview,name='checkouturl'),
    path('razorpayView/',razorpayView,name='razorpayView'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('ordersuccess/',ordersuccessview,name='ordersuccessurl'),
    path('order/',myorderview,name='myorderurl'),
    path('invoice/<int:orderId>/',invoiveview,name='invoiceurl'),
    path('removeCart/<int:cartId>/',removeCartView,name='removeCartUrl'),
    path('rating/<int:productId>/',ratingView,name='ratingUrl'),
    path('cart_user_data/',cart_user_data,name='cart_user_data_url'),
    path('direct_buy/',direct_buy,name="direct_buy"),
    # path('pdf/',pdf,name='pdf'),
]