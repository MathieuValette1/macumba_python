from macumba.webapp.models import Bateau


def get_bateau_by_id(idBateau):
    """

    :param idBateau: id du bateau à rechercher
    :return: le bateau correspondant à l'id
    """
    return Bateau.objects.get(pk=idBateau)


def get_bateau_by_nom(nom):
    """

    :param nom: le nom du bateau à chercher
    :return: le bateau correspondant au nom
    """
    return Bateau.objects.get(nom=nom)


