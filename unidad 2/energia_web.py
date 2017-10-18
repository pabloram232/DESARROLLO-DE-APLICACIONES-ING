from flask import Flask, render_template, request, redirect
from energia_module import energia, potencia

app = Flask(__name__)


@app.route('/')
def hello()-> '302':
    return redirect('/entry')

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Unidad 2')

@app.route('/exec_energia', methods=['GET', 'POST'])
def execute() -> 'html':
    L = float(request.form['L'])
    M = float(request.form['M'])
    T = float(request.form['T'])
    title = 'This is the result'
    result = energia(L, M , T)
    return render_template('result.html',
                           the_title=title,
                           the_l=L,
                           the_m=M,
                           the_t=T,
                           the_result=result, )


if __name__ == '__main__':
    app.run()
