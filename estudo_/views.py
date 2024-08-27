from estudo_ import app, db
from flask import render_template, url_for, request, redirect

from estudo_.models import Contato
from estudo_.forms import ContatoForm

@app.route("/")
def homepage():
    usuario = "rufino"
    idade = 26

    context = {
        'usuario': usuario,
        'idade'  : idade
    }

    return render_template('index.html', context=context)


@app.route('/contato/', methods=['GET', 'POST'])
def contato():
    form = ContatoForm()
    context = {}
    if form.validate_on_submit():
        form.save()
        return redirect(url_for('homepage'))

    return render_template('contato.html', context=context, form=form)


@app.route('/contato/lista')
def contatoLista():

    dados = Contato.query.all()
    print(dados)
    context = {}

    return render_template('contato_lista.html', context=context)





# Formato não recomendado
@app.route('/contato_old/', methods=['GET', 'POST'])
def contato_old():
    context = {}
    if request.method == 'GET':
        pesquisa = request.args.get('pesquisa')
        print('GET:', pesquisa)
        context.update({'pesquisa': pesquisa})

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        assunto = request.form['assunto']
        mensagem = request.form['mensagem']

        contato = Contato(
            name=name,
            email=email,
            assunto=assunto,
            mensagem=mensagem
        )

        db.session.add(contato)
        db.session.commit()

    return render_template('contato_old.html', context=context)
