# Használj egy hivatalos Python képfájlt (alapként)
FROM python:3.9-slim

# Állítsd be a munkakönyvtárat a konténerben
WORKDIR /app

# Másold át az aktuális könyvtár tartalmát a konténer /app könyvtárába
COPY . .

# Frissítsd a pip-et
RUN pip install --upgrade pip

# Telepítsd a szükséges csomagokat, amiket a requirements.txt-ben jelöltél meg
RUN pip install --no-cache-dir -r req.txt

# Tedd elérhetővé a 80-as portot (ha szükséges)
EXPOSE 80

# Indítsd el a main.py fájlt a konténer indulásakor
CMD ["python3", "main.py"]
