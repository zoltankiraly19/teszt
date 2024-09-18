# Válassz egy alap Python képet
FROM python:3.9-slim

# Állítsd be a munkakönyvtárat
WORKDIR /app

# Másold át a projekt összes fájlját a konténerbe
COPY . .

# Telepítsd a Python függőségeket a requirements.txt fájlból
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# Add meg, hogy mit futtasson a konténer indításkor
CMD ["python", "main.py"]
