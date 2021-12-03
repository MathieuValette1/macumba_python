from django.contrib import admin

from .models import Temoignage, Personne, Victime, Decoration, Image, Sauveteur, Sauvetage, Dimension, Bateau, \
    BateauSauvetage


# Humain
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ("pk", "temoignage")




class VictimeStaffAdmin(admin.ModelAdmin):
    list_display = ("isEnfant", "isAdo", "isAlive")


class DecorationAdmin(admin.ModelAdmin):
    list_display = ("date", "titre")


class ImageAdmin(admin.ModelAdmin):
    list_display = ("url", "legende")


class SauveteurAdmin(admin.ModelAdmin):
    list_display = ("poste", "biographie")


# Temps

class SauvetageAdmin(admin.ModelAdmin):
    list_display = ("date", "description", "sauvetageIndividuel")


class DimensionAdmin(admin.ModelAdmin):
    list_display = ("largeur", "longueur", "poids", "tirantEau")


# Actus
class BateauAdmin(admin.ModelAdmin):
    list_display = ("nom", "description", "isBateauSauvetage")


class BateauSauvetageAdmin(admin.ModelAdmin):
    list_display = ("affectation", "constructeur", "dateMiseEau", "essais", "finService")


### Register
admin.site.register(Victime, VictimeStaffAdmin)
admin.site.register(Bateau, BateauAdmin)
admin.site.register(BateauSauvetage, BateauSauvetageAdmin)
admin.site.register(Dimension, DimensionAdmin)
admin.site.register(Sauvetage, SauvetageAdmin)
admin.site.register(Temoignage, TemoignageAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Sauveteur, SauveteurAdmin)
admin.site.register(Decoration, DecorationAdmin)
