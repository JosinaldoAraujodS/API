from flask import Flask
import datetime as dt

# data_atual = dt.date.today()
# print("Data atual:", data_atual)

feriados_brasil = {
    dt.date(2023, 1, 1): "Ano Novo",
    dt.date(2023, 4, 21): "Tiradentes",
    dt.date(2023, 5, 1): "Dia do Trabalhador",
    dt.date(2023, 9, 7): "Dia da Independência",
    dt.date(2023, 10, 12): "Nossa Senhora Aparecida",
    dt.date(2023, 11, 2): "Finados",
    dt.date(2023, 11, 15): "Proclamação da República",
    dt.date(2023, 12, 25): "Natal"
}

validade = {
    "August": dt.date(2023, 6, 30)
}

hj = dt.date.today()

app = Flask(__name__)

# HOME API


@app.route("/")
def home():
    return "The API is live!"


# VERIFICAR VALIDADE DE ACESSO
@app.route('/vldd', defaults={"hj": hj})
def ident(hj):

    hj = dt.date.today()
    valido = hj < validade["August"]

    data_br = hj.strftime("%d/%m/%Y")

    if valido:
        return f"Hoje {data_br} a ferramenta está válida!"
    else:
        return f"Hoje {data_br} a ferramenta não está mais válida!"


# FERIADOS NO BRASIL
@app.route('/feriado', defaults={"hj": hj})
def feriado(hj):
    hj = dt.date.today()

    data_br = hj.strftime("%d/%m/%Y")

    if hj in feriados_brasil:
        return f"Hoje {data_br} é um feriado no Brasil!"
    else:
        return f"Hoje {data_br} não é um feriado no Brasil."


if __name__ == "__main__":
    app.run(debug=True)
