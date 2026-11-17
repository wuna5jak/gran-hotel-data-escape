import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Obtener la ruta de la carpeta donde se encuentra ESTE notebook (notebooks/)
NOTEBOOK_DIR = Path(".").resolve()

# 2. Calcular la carpeta raíz del proyecto (subir un nivel)
PROJECT_ROOT = NOTEBOOK_DIR.parent if NOTEBOOK_DIR.name == "notebooks" else NOTEBOOK_DIR

# 3. Definir la ruta exacta y absoluta al dataset
DATA_PATH = PROJECT_ROOT / "data" / "reservas_raw.csv"

print(f"📍 Buscando archivo en: {DATA_PATH}")

# 4. Verificación previa con mensaje pedagógico si falta el archivo
if not DATA_PATH.exists():
    print("❌ ¡ERROR! No se encuentra el archivo 'reservas_raw.csv'.")
    print("💡 Pista para el equipo de investigación:")
    print("   Ejecuta en tu terminal el comando: python scripts/make_dataset.py")
else:
    df_raw = pd.read_csv(DATA_PATH)
    print(f"📊 ¡Éxito! Registros brutos cargados: {len(df_raw)} filas")
    #display(df_raw.head())
    print(df_raw.head())


    
# 1. Identificar y contar duplicados exactos
n_duplicados = df_raw.duplicated().sum()
print(f"⚠️ Filas exactamente duplicadas encontradas: {n_duplicados}")

# 2. Eliminar duplicados
df_cleaned = df_raw.drop_duplicates().copy()

# 3. Identificar valores nulos por columna
print("\n❓ Valores nulos por columna (tras deduplicar):")
print(df_cleaned.isnull().sum())

# 4. Limpieza ligera: convertir precio_noche y noches a numérico para evitar errores
df_cleaned['precio_noche'] = pd.to_numeric(df_cleaned['precio_noche'], errors='coerce')
df_cleaned['noches'] = pd.to_numeric(df_cleaned['noches'], errors='coerce')

# Imputación o limpieza básica para el análisis de negocio
df_cleaned['estado'] = df_cleaned['estado'].fillna('Sin Registro')
df_cleaned['precio_noche'] = df_cleaned['precio_noche'].fillna(0)
df_cleaned['noches'] = df_cleaned['noches'].fillna(0)

# Cálculo del Subtotal de cada transacción
df_cleaned['subtotal'] = df_cleaned['precio_noche'] * df_cleaned['noches']

print(f"\n✅ Registros únicos procesados listos para análisis: {len(df_cleaned)} filas")

# Agregación por estado de reserva
resumen_estado = df_cleaned.groupby('estado').agg(
    num_reservas=('id_reserva', 'count'),
    ingresos_totales=('subtotal', 'sum'),
    promedio_noches=('noches', 'mean')
).reset_index()

# Mostrar tabla resumida
#display(resumen_estado)
print(resumen_estado)

# Filtrar únicamente la facturación real (Ventas Completadas efectivas)
ingresos_brutos_totales = df_cleaned['subtotal'].sum()
ingresos_netos_reales = df_cleaned[df_cleaned['estado'] == 'Completada']['subtotal'].sum()
fuga_financiera = ingresos_brutos_totales - ingresos_netos_reales

print(f"💰 Facturación Bruta (Sin Filtrar): {ingresos_brutos_totales:,.2f} €")
print(f"🎯 Facturación Neta Real (Solo Completadas): {ingresos_netos_reales:,.2f} €")
print(f"📉 Fuga / Importes No Efectivos (Canceladas/Devueltas): {fuga_financiera:,.2f} €")



fig, ax = plt.subplots(figsize=(8, 5))

bars = ax.bar(
    resumen_estado['estado'], 
    resumen_estado['ingresos_totales'], 
    color=['#2ecc71' if x == 'Completada' else '#e74c3c' for x in resumen_estado['estado']]
)

ax.set_title('Gran Hotel Olimpo: Distribución de Ingresos por Estado de Reserva', fontsize=12, fontweight='bold')
ax.set_ylabel('Euros (€)', fontsize=10)
ax.set_xlabel('Estado de la Reserva', fontsize=10)

# Etiquetar valores sobre las barras
for bar in bars:
    height = bar.get_height()
    ax.annotate(f'{height:,.0f} €',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.show()

# Preparamos los datos consolidados que servirán de Contexto Factual para la IA
contexto_ia = f"""
INFORMACIÓN VERIFICADA DEL HOTEL:
- Registros brutos iniciales: {len(df_raw)}
- Duplicados eliminados: {n_duplicados}
- Registros únicos finales: {len(df_cleaned)}
- Facturación Neta Real (Completada): {ingresos_netos_reales:,.2f} €
- Fuga por Cancelaciones/Devueltas: {fuga_financiera:,.2f} €
"""

prompt_estructurado = f"""
[ROLE]
Eres un Senior Data Analyst de la industria hotelera especializado en comunicación ejecutiva.

[CONTEXT]
{contexto_ia}

[TASK]
Escribe una síntesis ejecutiva para la Dirección General del Gran Hotel Olimpo explicando la solución a la fuga de datos.

[CONSTRAINTS]
1. Máximo 3 puntos clave (bullet points).
2. Rigor estricto: Utiliza ÚNICAMENTE las cifras del contexto. No inventes métricas adicionales (evita alucinaciones).
3. Mantén un tono profesional, claro y neutro sin sesgos de culpabilidad.
"""

print("📝 PROMPT ESTRUCTURADO LISTO PARA ENVIAR A LA LLM:")
print("="*60)
print(prompt_estructurado)
print("="*60)