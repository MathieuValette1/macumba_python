from .managers import bateau_manager, bateausauvetage_manager, personne_manager, sauveteur_manager, victime_manager, temoignage_manager, sauvetage_manager


def search_filters(filters:list, mot_cle):
    for filter in filters:
        if filter == "bateau":
            return bateau_manager.get_bateau_by_nom(mot_cle)
        elif filter == "bateau_sauvetage":
            return bateausauvetage_manager.get_BateauSauvetage_by_nom(mot_cle)
        elif filter == "personne":
            return personne_manager.get_Personne_by_nom(mot_cle)
        elif filter == "sauvetage":
            return sauvetage_manager.get_Sauvetage_by_date(mot_cle)
        elif filter == "victime":
            return victime_manager.get_Victime_by_nom(mot_cle)
        elif filter == "sauveteur":
            return sauveteur_manager.get_Sauveteur_by_nom(mot_cle)
        elif filter == "temoignage":
            return temoignage_manager.get_Temoignage_by_nom(mot_cle)
        else:
            pass

