from users.models import Profile
def context_profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)##teste se o user tem um profile, se não, ele retorna a chave profile vazia
            profile_exists = True
        except Profile.DoesNotExist:
            profile = {
                'pfp': None,
                'empresa': 'Sem informações',
                'setor': 'Sem informações'
            }
            profile_exists = False
    else:
        profile = None
        profile_exists = False

    return {'profile': profile, 'profile_exists': profile_exists}