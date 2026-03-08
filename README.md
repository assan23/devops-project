
# API Flask DevOps

Petite API REST Flask avec 2 endpoints.

## Endpoints

| Route     | Description              |
|----------|---------------------------|
| `GET /`  | Message de bienvenue JSON |
| `GET /health` | Statut OK            |

## Lancer en local

```bash
pip install -r requirements.txt
python app.py
```

API : http://localhost:5000

## Lancer avec Docker

```bash
docker build -t devops-flask-api .
docker run -p 5000:5000 devops-flask-api
```

## Fichiers

- `app.py` — Application Flask
- `requirements.txt` — Dépendances Python
- `Dockerfile` — Image Docker
>>>>>>> d585641 (Add Flask API and Dockerfile)
