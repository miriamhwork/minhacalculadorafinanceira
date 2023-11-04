from flask import Flask, render_template, request

app = Flask(__name__)

def calcular_tempo_necessario(meta, economia_mensal):
    if economia_mensal <= 0:
        return None  # Para evitar divisão por zero

    meses_necessarios = meta / economia_mensal
    return meses_necessarios

@app.route('/')
def calculadora():
    return render_template('calculadora.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        meta = float(request.form['meta'])
        economia_mensal = float(request.form['economia_mensal'])
        meses_necessarios = calcular_tempo_necessario(meta, economia_mensal)

        if meses_necessarios is not None:
            resultado = f"Para atingir a sua meta de R$ {meta:.2f} , poupando R$ {economia_mensal:.2f} por mês, você levará {meses_necessarios:.0f} meses."
        else:
            resultado = "Para atingir a meta, você deve economizar um valor em reais, ou seja, pelo menos R$0,01 ou mais."

        return render_template('resultado.html', resultado=resultado)

    except ValueError:
        return "Por favor, insira um valor em reais."

# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

