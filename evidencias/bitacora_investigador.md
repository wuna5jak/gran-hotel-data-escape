# 📝 Bitácora de Investigación - Gran Hotel Olimpo
**Equipo Auditor:** [Diana D] & [Maria del Mar]  
**Fecha:** [16/11/2026]

---

## 1. 🔑 Hallazgo Inicial (Puerta 1 - Git Bash)
* **Comando utilizado para encontrar la credencial oculta:** `ls -la`
* **Código de la Llave Maestra:** `GH-OLIMPO-DATA-2026-KEY`
* **Primera anomalía detectada en el servidor:*10 filas duplicadas + celdas vacias (NaN)* 

---

## 2. 🛡️ Registro de Control de Versiones (Puerta 2 - Git & GitHub)
* **Comando para preparar archivos (Staging):** `git add`
* **Mensaje del primer commit local:** `"feat: inicio de investigacion tras ataque al Gran Hotel Olimpo"`
* **URL del repositorio público en GitHub:** `git@github.com:wuna5jak/gran-hotel-data-escape.git`

---

## 3. 🗺️ Arquitectura y Entorno (Puerta 4 - VS Code & Dependencies)
* **Versión de Python detectada:** `3.15.2`
* **Comando utilizado para instalar `requirements.txt`:** `python -m pip install -r requirements.txt'
* **Diferencia entre Ruta Absoluta y Ruta Relativa (explicación breve):** 
Absoluta = dirección completa.
Relativa = dirección desde la ubicación actual.
---

## 4. ⚙️ Conciliación Financiera (Puerta 5 - Python CLI)
* **Facturación Bruta (Sin filtrar):** `56,090.00 €`
* **Facturación Neta Real (Solo Completadas):** `29,055.00 €`
* **Fuga Financiera (Canceladas + Devueltas):** ` 27,035.00 €`
* **Conclusión de Negocio:** ¿Por qué no debemos tomar decisiones con la facturación bruta?
Porque puede variar mucho de la situacion real.

---

## 5. 🔮 Auditoría Final e IA Generativa (Puerta 6 - Jupyter & Prompting)
* **Número de duplicados exactos eliminados:** `10`
* **Respuesta de la LLM tras enviar el Prompt Estructurado:**
  > 📝 PROMPT ESTRUCTURADO LISTO PARA ENVIAR A LA LLM:
============================================================

[ROLE]
Eres un Senior Data Analyst de la industria hotelera especializado en comunicación ejecutiva.

[CONTEXT]

INFORMACIÓN VERIFICADA DEL HOTEL:
- Registros brutos iniciales: 100
- Duplicados eliminados: 10
- Registros únicos finales: 90
- Facturación Neta Real (Completada): 29,055.00 €
- Fuga por Cancelaciones/Devueltas: 27,035.00 €


[TASK]
Escribe una síntesis ejecutiva para la Dirección General del Gran Hotel Olimpo explicando la solución a la fuga de datos.

[CONSTRAINTS]
1. Máximo 3 puntos clave (bullet points).
2. Rigor estricto: Utiliza ÚNICAMENTE las cifras del contexto. No inventes métricas adicionales (evita alucinaciones).
3. Mantén un tono profesional, claro y neutro sin sesgos de culpabilidad.

============================================================
* **Verificación de Factualidad y Sesgos (Guardrails):**
  - ¿La IA inventó algún dato que no estuviera en el contexto? (Sí/No y detalle):
  No? 
  - ¿El lenguaje utilizado es neutro y libre de sesgos de culpabilidad?
  Si

---

## 🏁 Semáforo de Autoevaluación Individual
* **Piloto:**  🟡 Amarillo  — *aunque yo tengo el conocimiento previo, me costo mucho entender los ejercicios*