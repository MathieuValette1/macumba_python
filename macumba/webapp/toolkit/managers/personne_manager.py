from macumba.webapp.models import Personne


def get_Personne_by_id(idPersonne):
    """

    :param idPersonne: id du Personne à rechercher
    :return: le Personne correspondant à l'id
    """
    return Personne.objects.get(pk=idPersonne)


def get_Personne_by_nom(nom):
    """

    :param nom: le nom du Personne à chercher
    :return: le Personne correspondant au nom
    """
    return Personne.objects.get(nom=nom)


