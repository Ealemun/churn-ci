# churn-ci

Prédiction de résiliation client, construite pas à pas avec un pipeline CI/CD
(GitHub Actions) : tests, lint, entraînement, image Docker, déploiement.

## Lancer les tests en local

```bash
python -m venv .venv
# Windows : .venv\Scripts\activate    Linux/macOS : source .venv/bin/activate
pip install -r requirements.txt
pytest
```
