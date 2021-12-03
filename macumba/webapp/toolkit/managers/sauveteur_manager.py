from macumba.webapp.models import Sauveteur


def get_Sauveteur_by_id(idSauveteur):
    """

    :param idSauveteur: id du Sauveteur à rechercher
    :return: le Sauveteur correspondant à l'id
    """
    return Sauveteur.objects.get(pk=idSauveteur)


def get_Sauveteur_by_nom(nom):
    """

    :param nom: le nom du Sauveteur à chercher
    :return: le Sauveteur correspondant au nom
    """
    return Sauveteur.objects.get(nom=nom)


