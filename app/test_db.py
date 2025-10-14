from app.database import engine

try:
    with engine.connect() as connection:
        result = connection.execute("SELECT NOW();")
        print("✅ Conexión exitosa con Aiven:", result.fetchone())
except Exception as e:
    print("❌ Error al conectar con Aiven:", e)