from .models import MainMenu


def send_data(request):
    data = {
        'MenuData': MainMenu.objects.prefetch_related('submenu_set').all()
    }
    return data
