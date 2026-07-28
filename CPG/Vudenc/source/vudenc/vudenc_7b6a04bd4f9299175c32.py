from flask import Flask, render_template, request, current_app, g
from indic_transliteration import sanscript
from indic_transliteration.sanscript import SchemeMap, SCHEMES, transliterate
import random
import sqlite3 as sql
import re
app = Flask(__name__, static_url_path='', static_folder='static')
@app.route('/')...
all_vargas = ['स्वर्गवर्गः', 'व्योमवर्गः', 'दिग्वर्गः', 'कालवर्गः',
    'धीवर्गः', 'शब्दादिवर्गः', 'नाट्यवर्गः', 'पातालभोगिवर्गः', 'नरकवर्गः',
    'वारिवर्गः', 'भूमिवर्गः', 'पुरवर्गः', 'शैलवर्गः', 'वनौषधिवर्गः',
    'सिंहादिवर्गः', 'मनुष्यवर्गः', 'ब्रह्मवर्गः', 'क्षत्रियवर्गः',
    'वैश्यवर्गः', 'शूद्रवर्गः', 'विशेष्यनिघ्नवर्गः', 'सङ्कीर्णवर्गः',
    'विशेष्यनिघ्नवर्गः', 'सङ्कीर्णवर्गः', 'नानार्थवर्गः', 'अव्ययवर्गः']
return render_template('index.html', all_vargas=all_vargas)
