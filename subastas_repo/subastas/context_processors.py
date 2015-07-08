from subastas.models import Subasta


def current_subasta(request):
    return {'current_subasta': Subasta.objects.get_current()}
