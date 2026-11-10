"""Tests unitaires des fonctions de préparation des données."""

import pytest

from churn.features import taux_reclamations, tranche_anciennete


# --- tranche_anciennete -------------------------------------------------

# parametrize lance le même test avec plusieurs couples (entrée, attendu).
# On vérifie surtout les frontières (11/12, 35/36), là où se cachent les bugs.
@pytest.mark.parametrize(
    "mois, attendu",
    [
        (0, "nouveau"),
        (11, "nouveau"),
        (12, "etabli"),
        (35, "etabli"),
        (36, "fidele"),
        (120, "fidele"),
    ],
)
def test_tranche_anciennete(mois, attendu):
    assert tranche_anciennete(mois) == attendu


def test_tranche_anciennete_refuse_le_negatif():
    # pytest.raises vérifie qu'une erreur est bien levée
    with pytest.raises(ValueError):
        tranche_anciennete(-1)


# --- taux_reclamations --------------------------------------------------

def test_taux_reclamations_cas_normal():
    # 6 réclamations en 12 mois = 0,5 par mois
    assert taux_reclamations(6, 12) == 0.5


def test_taux_reclamations_client_du_mois():
    # 0 mois d'ancienneté ne doit pas provoquer de division par zéro
    assert taux_reclamations(2, 0) == 2.0
