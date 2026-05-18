# L2 Flask App Skeleton（含 README / pytest / Dockerfile）/ L2 Flask App Skeleton (with README / pytest / Dockerfile)

> 對應課程 / Course: [L2_ANTIGRAVITY_COURSE_PLAN.md](../L2_ANTIGRAVITY_COURSE_PLAN.md) §3.4 + §6.2 Builder
> 版本 / Version: 範本 v1.0（學員 / 講師可 clone）/ Template v1.0 (clonable by learner / instructor)
> 授權 / License: Apache 2.0

## 使用方式 / How to use

本檔列出 Flask app 骨架的 **檔案結構 + 各檔案內容**。Builder 課堂上學員用 Antigravity Agent 生成此骨架，再加上自己的業務邏輯。
This file lists the **file structure + per-file content** for a Flask app skeleton. In Builder class, learners use Antigravity Agent to generate this skeleton, then add their own business logic.

---

## 1. 目標檔案結構 / Target file structure

```text
flask-app-skeleton/
├── app.py                 # Flask 主程式 / Flask main
├── requirements.txt       # Python deps
├── Dockerfile             # Docker
├── .dockerignore
├── .gitignore
├── README.md              # 文件 / docs
├── tests/
│   ├── __init__.py
│   ├── test_app.py        # pytest unit tests
│   └── conftest.py        # pytest fixtures
├── routes/
│   ├── __init__.py
│   ├── health.py          # /health endpoint
│   └── api.py             # /api endpoints
├── services/
│   ├── __init__.py
│   └── example_service.py # 範例 business logic / example logic
└── config.py              # 設定 / config
```

---

## 2. 各檔案內容 / Per-file content

### 2.1 `app.py`

```python
"""Flask app entry point."""
from flask import Flask
from routes.health import health_bp
from routes.api import api_bp
from config import Config


def create_app(config_class: type = Config) -> Flask:
    """Application factory."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(health_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    return app


if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8080, debug=False)
```

### 2.2 `requirements.txt`

```text
flask>=3.0,<4.0
gunicorn>=21.0,<22.0
pytest>=8.0,<9.0
pytest-cov>=4.0,<5.0
```

### 2.3 `Dockerfile`

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app:create_app()"]
```

### 2.4 `routes/health.py`

```python
"""Health check endpoint."""
from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/health")
def health():
    return jsonify({"status": "ok"}), 200
```

### 2.5 `routes/api.py`

```python
"""Business API endpoints — fill in your own."""
from flask import Blueprint, jsonify, request
from services.example_service import example_logic

api_bp = Blueprint("api", __name__)


@api_bp.route("/example", methods=["POST"])
def example():
    data = request.get_json() or {}
    result = example_logic(data)
    return jsonify(result), 200
```

### 2.6 `services/example_service.py`

```python
"""Example business logic — replace with your own."""


def example_logic(payload: dict) -> dict:
    """Process payload and return result."""
    return {"echo": payload, "processed": True}
```

### 2.7 `config.py`

```python
"""Application configuration."""
import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-do-not-use-in-prod")
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
```

### 2.8 `tests/conftest.py`

```python
"""pytest fixtures."""
import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c
```

### 2.9 `tests/test_app.py`

```python
"""Unit tests."""


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_example(client):
    r = client.post("/api/example", json={"hello": "world"})
    assert r.status_code == 200
    assert r.get_json()["processed"] is True
```

### 2.10 `.gitignore`

```gitignore
__pycache__/
*.pyc
.pytest_cache/
.coverage
.env
.venv/
```

### 2.11 `.dockerignore`

```text
__pycache__
*.pyc
.pytest_cache
.git
.venv
.env
README.md
tests/
```

### 2.12 `README.md`

```markdown
# Flask App Skeleton

## Setup

\`\`\`bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
\`\`\`

## Run tests

\`\`\`bash
pytest --cov=.
\`\`\`

## Build & run with Docker

\`\`\`bash
docker build -t flask-skeleton .
docker run -p 8080:8080 flask-skeleton
\`\`\`

## Endpoints

- `GET /health` — health check
- `POST /api/example` — example endpoint

## Extending

Add new blueprints in `routes/`, business logic in `services/`, fixtures in `tests/`.
```

---

## 3. 學員任務 / Learner Task

1. 用 Antigravity Agent **生成上述 12 個檔案** / Use Antigravity Agent to **generate all 12 files**
2. `pytest` 跑過 2 個 test / `pytest` passes both tests
3. `docker build && docker run` 成功啟動 / Successful Docker build & run
4. `curl http://localhost:8080/health` 回 `{"status":"ok"}` / curl returns `{"status":"ok"}`
5. 加 **自己業務邏輯** 到 `services/example_service.py` 並補測試 / Add **own business logic** to service + write tests
6. 產出 Walkthrough Artifact（見 L2_WALKTHROUGH_ARTIFACT_EXAMPLE.md）/ Produce Walkthrough Artifact (see L2_WALKTHROUGH_ARTIFACT_EXAMPLE.md)

## 4. 完成標準 / Completion Criteria

- [ ] 12 個檔案結構正確 / 12-file structure correct
- [ ] `pytest` 全綠（含覆蓋率 ≥ 50%）/ `pytest` all green (coverage ≥ 50%)
- [ ] Docker image 成功 build + run / Docker image builds + runs
- [ ] README 含安裝、測試、部署 3 段 / README has setup / test / deploy 3 sections
- [ ] 加了 ≥ 1 個自己的 endpoint / Added ≥ 1 own endpoint
