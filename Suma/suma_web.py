"""JUAN PABLO RAMIREZ IBARRA
GITI9072-E

SUMA DE DOS NUMEROS"""
from flask import Flask, render_template, request, redirect, escape
from functions import comp_tot, vent_net
import psycopg2

app = Flask(__name__)

#
def insertar_registro(num1: float, num2: float) -> None:
    configuracionDB = {'host': 'localhost',
                              'user':'postgres',
                              'password':'2414',
                              'database':'UNIDAD_III',}
    conexion = psycopg2.connect(**configuracionDB)
    tot = comp_tot(num1, num2)
    _SQL = ("INSERT INTO Resultado(numero1, numero2, total) VALUES(%s, %s, %s)")
    cursor = conexion.cursor()
    cursor.execute(_SQL, (num1, num2, tot))
    conexion.commit()
    cursor.close()
    conexion.close()

@app.route('/')
def inicio() -> '302':
    return redirect('/entry')


@app.route ('/exec_equation', methods=['POST'])
def execute()->'html':
    num1=float((request.form['num1']))
    num2=float((request.form['num2']))
    tot = float(comp_tot(num1, num2))
    title='Resultado:'
    insertar_registro(num1, num2)
    return render_template('results.html',
                           the_title=title,
                           the_num1=num1,
                           the_num2=num2,
                           the_result=tot,)

@app.route ('/entry')
def entry_page()->'html':
    return render_template('entry.html',
                           the_title='SUMA')


@app.route('/data')
def view_data() -> 'html':
    params = {'host': 'localhost',
              'user':'postgres',
              'password':'2414',
              'database':'UNIDAD_III',}
    connection = psycopg2.connect(**params)
    cursor = connection.cursor()
    _SQL = ("SELECT * FROM Resultado")
    cursor.execute(_SQL)
    rows = cursor.fetchall()
    contents = []
    for row in rows:
            contents.append(row)
    cursor.close()
    connection.close()
    titles = ('id','numero1', 'numero2', 'Resultado')
    return render_template('data.html',
                           the_title='Resultados',
                           the_row_titles=titles,
                           the_data=contents, )

if __name__ == '__main__':
    app.run(debug=True)
