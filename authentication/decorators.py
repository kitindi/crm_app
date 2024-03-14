# defining user roles
from django.http import HttpResponse
from django.shortcuts import redirect

# decorator for unauthnticated users
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
             return view_func(request,*args, **kwargs)
    
    return wrapper_func
            

# decorator to restric access to the pages based on role/ grouping

def allowed_user(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()
            if group in allowed_roles:
                return view_func(*args, **kwargs)
            else:
                return redirect('customer')
        return wrapper_func
    return decorator



# addmin only url

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0]
        if group == 'admin':
            return view_func(*args, **kwargs)
    return wrapper_func
            