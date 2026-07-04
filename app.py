import sqlite3
from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

def init_db():
    if not os.path.exists('database.db'):
        conn = sqlite3.connect('database.db')
        with open('init.sql', 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

init_db()

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Portal de Empleados - Logística</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #eef2f5; padding: 40px; color: #333; }
        .container { max-width: 650px; margin: auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        h2 { color: #2c3e50; margin-top: 0; }
        input[type="text"] { width: calc(100% - 110px); padding: 12px; margin-bottom: 20px; border: 1px solid #ccd1d9; border-radius: 4px; }
        button { width: 100px; padding: 12px; background: #3498db; color: white; border: none; border-radius: 4px; cursor: pointer; font-weight: bold; }
        button:hover { background: #2980b9; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { padding: 12px; border: 1px solid #e1e8ed; text-align: left; }
        th { background: #34495e; color: white; }
        .error { color: #e74c3c; font-weight: bold; background: #fadbd8; padding: 10px; border-radius: 4px; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Directorio Corporativo de Empleados</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Buscar por usuario (ej. j.perez)" autocomplete="off">
            <button type="submit">Buscar</button>
        </form>
        
        {% if error %}
            <div class="error">{{ error }}</div>
        {% endif %}
        
        {% if results %}
            <table>
                <tr>
                    <th>Usuario</th>
                    <th>Rol</th>
                    <th>Email</th>
                </tr>
                {% for row in results %}
                <tr>
                    <td>{{ row[1] }}</td>
                    <td>{{ row[2] }}</td>
                    <td>{{ row[3] }}</td>
                </tr>
                {% endfor %}
            </table>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    error = None
    
    if request.method == 'POST':
        username = request.form.get('username', '')
        try:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            query = f"SELECT * FROM datos_publicos WHERE usuario = '{username}'"
            cursor.execute(query)
            results = cursor.fetchall()
            conn.close()
        except sqlite3.Error as e:
            error = "Error interno de la base de datos."
        except Exception as e:
            error = "Error inesperado."

    return render_template_string(HTML_TEMPLATE, results=results, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)