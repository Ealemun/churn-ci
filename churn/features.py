"""Fonctions de préparation des données pour le modèle de résiliation (churn)."""


def tranche_anciennete(mois: int) -> str:
    """Range un client dans une tranche selon son ancienneté en mois."""
    # Une ancienneté négative n'a pas de sens : on refuse explicitement
    # plutôt que de renvoyer une tranche fausse sans prévenir.
    if mois < 0:
        raise ValueError("L'ancienneté ne peut pas être négative")
    if mois < 12:
        return "nouveau"  # moins d'un an
    if mois < 36:
        return "etabli"  # entre 1 et 3 ans
    return "fidele"  # 3 ans et plus


def taux_reclamations(nb_reclamations: int, mois: int) -> float:
    """Nombre moyen de réclamations par mois d'abonnement."""
    # Un client inscrit ce mois-ci a 0 mois d'ancienneté :
    # on évite la division par zéro en comptant ce mois comme un mois entier.
    if mois == 0:
        return float(nb_reclamations)
    return nb_reclamations / mois
