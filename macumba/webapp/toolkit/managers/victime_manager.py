from macumba.webapp.models import Victime


def get_Victime_by_id(idVictime):
    """

    :param idVictime: id du Victime à rechercher
    :return: le Victime correspondant à l'id
    """
    return Victime.objects.get(pk=idVictime)


def get_Victime_by_nom(nom):
    """

    :param nom: le nom du Victime à chercher
    :return: le Victime correspondant au nom
    """
    return Victime.objects.get(nom=nom)


