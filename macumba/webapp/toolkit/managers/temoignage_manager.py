from macumba.webapp.models import Temoignage


def get_Temoignage_by_id(idTemoignage):
    """

    :param idTemoignage: id du Temoignage à rechercher
    :return: le Temoignage correspondant à l'id
    """
    return Temoignage.objects.get(pk=idTemoignage)


def get_Temoignage_by_nom(nom):
    """

    :param nom: le nom du Temoignage à chercher
    :return: le Temoignage correspondant au nom
    """
    return Temoignage.objects.get(nom=nom)


