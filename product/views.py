
from datetime import date

from cart.models import CartModel
from django.http import Http404, HttpRequest, HttpResponse, QueryDict
from django.shortcuts import redirect, render
from django.views import View
from usr.models import UserProfileWishlist

from .models import Category, Product


class CategoryView(View):
    
    def get(self,request,pk=None):
        if pk == None:
            
            categories = Category.objects.all()
        else:
            categories = Category.objects.filter(category_id=pk)
            
        context = {
            "categories":categories,
        }
        
        return render(request,'./category.html',context)

class ProductView(View):
    
    def query(self,request:HttpRequest) -> dict: 
        if request.method == "GET":
            query_dict = QueryDict(request.META['QUERY_STRING'])
            return query_dict.dict()
        else:
            return dict() 
    
    
    def get(self,request:HttpRequest,pk=None):
        query_dict = self.query(request)
        
        args = dict()
        if bool(query_dict):
            for k,v in query_dict.items():
                    args[k] = v
            
        if pk == None:
            
            # this provide args like ?category_id=4
            product = Product.objects.all().filter(**args)
        else :
            product = Product.objects.filter(product_id=pk)
        
        
        
        context = {
            "products":product
        }
        
        return render(request,'product-list.html',context=context)


class ProductDetail(View):
    
    def query(self,request:HttpRequest) -> dict: 
        if request.method == "GET":
            query_dict = QueryDict(request.META['QUERY_STRING'])
            return query_dict.dict()
        else:
            return dict() 
    
    
    def get(self,request):
        query_dict = self.query(request)
        self.user_id = request.user.id
        
        args = dict()
        if bool(query_dict):
            
            for k,v in query_dict.items():
                args[k] = v
        
            
            product = Product.objects.filter(**args)
            if not bool(product):
                
                return HttpResponse("404 Product Not Found")
            
            context_data = {
                "pro" : product
            }
            
        else :
            return redirect("home:home_func")
        
        ### If wishlist added or not check ###
        query = UserProfileWishlist.objects.filter(user_id=self.user_id)
        try:
            q = query[0].product_ids['product_id']
            for t in q:
                if product[0].product_id == t[0]:
                    context_data['is_wishlisted'] = 'true'
                    
            
                
        except IndexError :
            pass
        
        ## Default product quantity
        context_data["quantity"] = '0'
        
        ### Cart Settings ###
        user_model = CartModel.objects.filter(user_id = self.user_id)
        if user_model:
            data = user_model[0].cart_items
            for ls in data["products"]:
                if ls[0] == product[0].product_id:
                    context_data["cart_added"]  = "true"
                    context_data["quantity"] = ls[2]
        
        

        return render(request,"detail_product.html",context_data)


##### Product Wishlist add /remove #####
class ProductWishlist(View):
    model = UserProfileWishlist
    
    def post(self,request):
        self.user_id = request.user.id


class WishlistAdd(ProductWishlist):
    
    def post(self,request,product_id,category_id):
        
        super(WishlistAdd,self).post(request)
        self.if_exist_or_not = self.model.objects.filter(user_id = self.user_id)
        
        self.id_list = list()
        
        """
        structure :
        user_id : int
        product_ids : {"product_id":[ [product_id, category_id],
                        [product_id, category_id],
                    ]}
        """

        # if query dict filter empty then it will go into else condition
        if self.if_exist_or_not : 
            ## capturing previous list
            self.dc = self.if_exist_or_not[0].product_ids
            self.pl = self.dc['product_id'] # capturing list
            self.pl.append(list((product_id , category_id))) # adding out data
            
            
            ## Update 
            obj = self.if_exist_or_not[0]
            obj.product_ids = {'product_id':self.pl}
            obj.save()
        else :
            
            self.dc = {
                "product_id" : [(product_id,category_id)]
            }
            obj = UserProfileWishlist.objects.create(user_id = self.user_id, product_ids = self.dc)
            obj.save()
            
        return redirect(request.META.get("HTTP_REFERER"))
    
    def get(self,request,product_id,category_id):
        return self.post(request,product_id,category_id)


class WishlistRemove(ProductWishlist):
    
    def post(self,request,product_id,category_id):
        super(WishlistRemove,self).post(request)
        self.get_user_model= self.model.objects.filter(user_id = self.user_id)
        
        self.get_data = self.get_user_model[0].product_ids
        
        for i in self.get_data.get('product_id'):
            if product_id == i[0] and category_id == i[1] :
                self.t = self.get_data.get('product_id')
                self.t.remove([product_id,category_id])
                
                # update 
                obj = self.get_user_model[0]
                obj.product_ids = {'product_id':self.t}
                obj.save()
        
        return redirect(request.META.get("HTTP_REFERER"))
    
    def get(self,request,product_id,category_id):
        return self.post(request,product_id,category_id)
