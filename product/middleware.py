

class AddProductDimensions:
    def __init__(self,get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        if request.path.startswith("/admin/"):
            
            pass
        response = self.get_response(request)
