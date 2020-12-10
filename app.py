from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from functions import *


app = Flask(__name__)
app.config['SECRET_KEY'] = "SecretForexConverter"
app.debug = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.route('/')
def show_homepage():
    """Display homepage with currency conversion form"""

    return render_template('index.html')

@app.route('/conversion')
def show_conversion():
    """Harvest form-data to make currency conversion.
    Handle Error messages
    Display page with successful conversion information"""

    converting_from = request.args['from'].upper()
    converting_to = request.args['to'].upper()
    amount = float(request.args['amt'])

    message = handle_error_msg(converting_from, converting_to, amount)
    
    if message:
        flash(message)
        
        return redirect('/')

    else:
        conv_decimal = handle_conversion(converting_from, converting_to, amount)
        
        curr_symbol_from =  get_curr_symbol(converting_from)
        curr_symbol_to = get_curr_symbol(converting_to)

        message = f"{curr_symbol_from} {amount} converts to {curr_symbol_to} {conv_decimal}"

        return render_template('conversion.html', message=message)
    
