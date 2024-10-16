from users.models import Profile
def context_profile(request):
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)##teste se o user tem um profile, se não, ele retorna a chave profile vazia
        except Profile.DoesNotExist:
            profile = Profile.objects.filter(user=request.user)#caso não tenha perfil, seta as informações de setor e empres para a string 'sem informações
            profile.empresa='Sem informações'
            profile.setor='Sem informações'    
    else:
        return { 'profile': None }
    return {'profile': profile}