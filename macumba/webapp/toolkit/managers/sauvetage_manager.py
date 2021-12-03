from macumba.webapp.models import Sauvetage


def get_Sauvetage_by_id(idSauvetage):
    """

    :param idSauvetage: id du Sauvetage à rechercher
    :return: le Sauvetage correspondant à l'id
    """
    return Sauvetage.objects.get(pk=idSauvetage)


def get_Sauvetage_by_date(date):
    """

    :param date: le date du Sauvetage à chercher
    :return: le Sauvetage correspondant au date
    """
    return Sauvetage.objects.get(date=date)


