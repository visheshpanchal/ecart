from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from usr.models import UserProfileAddress


@login_required(login_url="accounts:account_login")
def user_address(request:HttpRequest,delete=0):
    user_id = request.user.id
    query_dict = UserProfileAddress.objects.filter(user_id=user_id)
        
    return render(request,"profile_user/address.html",context={'addresses':query_dict})



@login_required(login_url="accounts:account_login")
def user_add_address(request):
    user_id = request.user.id
    
    if request.method == "POST":
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phoneNumber']
        city = request.POST['city']
        state = request.POST['state']
        zip_no = request.POST['zip']
        address_1 = request.POST['address1']
        address_2 = request.POST['address2']
        
        usr_data = UserProfileAddress.objects.create(
                            user_id=user_id,
                            first_name = first_name,
                            last_name = last_name,
                            email = email,
                            phone_number = phone,
                            city = city,
                            state = state,
                            address_1 = address_1,
                            address_2 = address_2,
                            zip_number = zip_no
            )
        
        usr_data.save()
        
        messages.success(request,"New address successfully added.")
        return redirect('profile:address')
    
    return render(request,"profile_user/add-address.html")

def user_address_delete(request):
    if request.method == 'POST':
        delete_add_id = request.POST.get('deleteId')

        delete_add = UserProfileAddress.objects.get(id=delete_add_id)
        delete_add.delete()
        
        
    
    return redirect("profile:address")
