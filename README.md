# CS 163 — Web Apps, Cloud Deployment & ML Fine-Tuning

Course materials covering interactive web applications, cloud deployment, containerization, and model fine-tuning.

## Repository Structure

| Directory | Topic |
|-----------|-------|
| `dashapps/` | Plotly Dash web apps (HTML layout, data tables, graphs, callbacks, multi-page apps) |
| `appengine/` | Deploying a Dash app to Google App Engine with Cloud Storage integration |
| `intro-to-docker/` | Containerizing a FastAPI ML inference service with Docker and deploying to Cloud Run |
| `fine-tuning/` | Transformer fine-tuning techniques: linear probing and LoRA |

## Topics Covered

### Dash Web Apps (`dashapps/`)
Progressive examples building up from basic HTML to interactive dashboards:
- `app1.py` – basic layout
- `app2.py` – HTML and styling
- `app3.py` – data tables and charts
- `app4.py` – callbacks and interactivity
- `app5-multi/` – multi-page app
- `app6.py` – hover/click graph interactions
- `app7.py` / `app8.py` – Bootstrap themes and layout

### Google App Engine (`appengine/`)
- Deploying a Dash app with Gunicorn via `app.yaml`
- Reading data from Google Cloud Storage using `google-cloud-storage`
- Environment variables for bucket configuration

### Docker & Cloud Run (`intro-to-docker/`)
- FastAPI REST API serving a Decision Tree model
- Writing a `Dockerfile` and building images
- Publishing to Google Artifact Registry
- Deploying to Cloud Run

### Fine-Tuning (`fine-tuning/`)
- `01_probing.ipynb` – Linear probing on DistilBERT for IMDb sentiment classification
- `02_lora.ipynb` – Parameter-efficient fine-tuning with LoRA

## Notes
See `note.md` for class notes and references on Dash and Google App Engine topics.
