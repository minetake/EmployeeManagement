from .models import User

def get_user_id(request):
    
    user = User.objects.filter(auth_id=request.user.id).values('id')
    
    uid = 0
    for data in user:
        print(data['id'])
        uid = data['id']
        
    return uid    