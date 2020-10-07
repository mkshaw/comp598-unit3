def get_user(request):

    login_value = request.get_argument('login')

    if login_value == 'letmein':
        return 1
    else:
        return None

login_url = '/login'
