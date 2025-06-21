# ----  Dockerfile  --------------------------------------------------
FROM python:3.12-slim

# 1) set working directory
WORKDIR /app

# 2) copy only the dependency file first (leverages Docker layer cache)
COPY requirements.txt .

# 3) install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4) copy the actual application code
COPY Backend/app ./app

# 5) expose whichever port you’ll map (optional)
ENV PORT=8000

# 6) start FastAPI via uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# --------------------------------------------------------------------
