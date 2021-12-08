"""Web Application Program"""
from flask import Flask, render_template, request, flash
from calc.calculator import Calculator

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def homepage():
    """Display homepage"""
    return render_template('index.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    """Display the form"""
    if request.method == 'POST':
        # name of the tag
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']

        if value1 == "" or value2 == "":
            flash("Input Empty Error!", "error")
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation, result="")

        getattr(Calculator, operation)(value1, (value2,))
        result = ""

        if Calculator.get_last_calculation() is None:
            flash("Division by Zero Error!", "error")
            result = "None"
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation, result=result)
        else:
            result = str(Calculator.get_last_calculation())
            flash("Success!", "success")
            return render_template('result.html', value1=value1,
                                   value2=value2, operation=operation, result=result)
    else:
        return render_template('form.html')


@app.route('/result')
def result_message():
    """Display the result"""
    value1 = request.args.get('value1')
    value2 = request.args.get('value2')
    operation = request.args.get('operation')
    result = request.args.get('result')
    message = operation + " of " + value1 + " " + value2 + " is " + result
    flash('You were successfully logged in')
    return message
