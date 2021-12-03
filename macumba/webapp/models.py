from django.db import models


class Temoignage(models.Model):
    temoignage = models.CharField(max_length=2000)


class Personne(models.Model):
    HOMME = "Homme"
    FEMME = "Femme"

    SEXE_CHOICES = [
        (HOMME, "Homme"),
        (FEMME, "Homme")
    ]

    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    sexe = models.CharField(max_length=50, choices=SEXE_CHOICES)
    dateNaissance = models.DateField()
    dateDeces = models.DateField()
    lieuNaissance = models.CharField(max_length=50)
    lieuDeces = models.CharField(max_length=50)

    temoignage = models.ForeignKey(Temoignage, on_delete=models.CASCADE)

class Victime(Personne):
    isEnfant = models.BooleanField()
    isAdo = models.BooleanField()
    isAlive = models.BooleanField()


class Decoration(models.Model):
    date = models.DateField()
    titre = models.CharField(max_length=50)


class Image(models.Model):
    url = models.CharField(max_length=200)
    legende = models.CharField(max_length=200)


class Sauveteur(Personne):
    poste = models.CharField(max_length=50)
    biographie = models.CharField(max_length=2000)
    decoration = models.ForeignKey(Decoration, on_delete=models.CASCADE)

    images = models.ManyToManyField(Image)


class Sauvetage(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=1000)
    sauvetageIndividuel = models.BooleanField()

    temoignages = models.ManyToManyField(Temoignage)
    personnes = models.ManyToManyField(Personne)


class Dimension(models.Model):
    largeur = models.FloatField()
    longueur = models.FloatField()
    poids = models.FloatField()
    tirantEau = models.FloatField()


class Bateau(models.Model):
    VOILE = "Voile"
    RAME = "Rame"
    MOTEUR = "Moteur"

    TYPE_CHOICES = [
        (VOILE, "Voile"),
        (RAME, 'Rame'),
        (MOTEUR, 'Moteur')
    ]

    CANOT = "Canot"
    CORVETTE_DE_PILOTAGE = "Corvette de pilotage"
    REMORQUEUR = "Remorqueur"
    BATEAU_FEU = "Bateau-feu"
    GOELETTE = "Goelette"
    PNEUMATIQUE = "Pneumatique"

    MODELE_CHOICES = [
        (CANOT, "Canot"),
        (CORVETTE_DE_PILOTAGE, "Corvette de pilotage"),
        (REMORQUEUR, "Remorqueur"),
        (BATEAU_FEU, "Bateau-feu"),
        (GOELETTE, "Goelette"),
        (PNEUMATIQUE, "Pneumatique")
    ]

    nom = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    isBateauSauvetage = models.BooleanField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    modele = models.CharField(max_length=50, choices=MODELE_CHOICES)

    images = models.ManyToManyField(Image)
    sauvetages = models.ManyToManyField(Sauvetage)
    personnes = models.ManyToManyField(Personne)
    dimension = models.OneToOneField(Dimension, on_delete=models.CASCADE)





class BateauSauvetage(Bateau):
    affectation = models.CharField(max_length=100)
    constructeur = models.CharField(max_length=100)
    dateMiseEau = models.DateField()
    essais = models.CharField(max_length=50)
    finService = models.DateField()


