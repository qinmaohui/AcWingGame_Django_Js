from django.http import HttpResponse

def index(request):
    line1='<h1 style="text-align:center">术士之战</h1>'
    return HttpResponse(line1)
def play(request):
    line1='<h1 style="text-align:center">游戏界面</h1>'
    return HttpResponse(line1)
