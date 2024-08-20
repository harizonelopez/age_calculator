from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'aladinh00-010montext'  

@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method=='POST':
        username = request.form['username']
        session['username'] = username
        return redirect(url_for('age_calculator'))
    
    return render_template('index.html')

@app.route('/age_calculator', methods=['GET', 'POST'])
def age_calculator():
    age_years = None
    age_months = None
    age_days = None
    current_year = datetime.now().year
    if request.method=='POST':
        try:
            year = int(request.form['year'])
            month = int(request.form['month'])
            day = int(request.form['day'])
            birthdate = datetime(year, month, day)
            today = datetime.now()
            age_years = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
            birthdate_anniversary = datetime(today.year, month, day)
            if today >= birthdate_anniversary:
                age_months = today.month - birthdate_anniversary.month
                age_days = today.day - birthdate_anniversary.day
            else:
                age_months = (today.month - birthdate_anniversary.month - 1 + 12) % 12
                age_days = (today.day - birthdate_anniversary.day + 30) % 30

        except Exception as e:
            age_years, age_months, age_days = None, None, None
            error_message = f"ERROR!! Invalid data entries. Please enter valid numerical values for year, month and day inputs. {str(e)}"
            
            return render_template('home.html', error_message=error_message, current_year=current_year)
    return render_template('home.html', age_years=age_years, age_months=age_months, age_days=age_days, current_year=current_year)

if __name__ == "__main__":
    app.run(debug=True)
