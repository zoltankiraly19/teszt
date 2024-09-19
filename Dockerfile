# Használj egy hivatalos Python képfájlt (alapként)
FROM python:3.9-slim

# Állítsd be a munkakönyvtárat a konténerben
WORKDIR /app

# Másold át az aktuális könyvtár tartalmát a konténer /app könyvtárába
COPY . .

# Frissítsd a pip-et
RUN pip install --upgrade pip

# Telepítsd a szükséges csomagokat a requirements.txt alapján
RUN pip install --no-cache-dir -r req.txt

# Töröld az EXPOSE utasítást, mivel nem futtatsz webszervert
# EXPOSE 80  -> EZT ELTÁVOLÍTJUK

# Indítsd el a main.py fájlt a konténer indulásakor
CMD ["python",
