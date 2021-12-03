from macumba.webapp.models import BateauSauvetage


def get_BateauSauvetage_by_id(idBateauSauvetage):
    """

    :param idBateauSauvetage: id du BateauSauvetage à rechercher
    :return: le BateauSauvetage correspondant à l'id
    """
    return BateauSauvetage.objects.get(pk=idBateauSauvetage)


def get_BateauSauvetage_by_nom(nom):
    """

    :param nom: le nom du BateauSauvetage à chercher
    :return: le BateauSauvetage correspondant au nom
    """
    return BateauSauvetage.objects.get(nom=nom)