from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('homepage.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/legitimate_claims')
def legitimate_claims():
    return render_template('legit_claim.html')

@app.route('/fraudulent_claims')
def fraudulent_claims():
    return render_template('fraud_claim.html')

@app.route('/graphical_analysis')
def graphical_analysis():
    return render_template('grahic_stats.html')
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/upload_excel', methods=['POST'])
def upload_excel():
    if request.method == 'POST':
        excel_file = request.files['excel_file']
        if excel_file:
            df = pd.read_excel(excel_file)
            # Process the data in the DataFrame (df) as needed
            return "File uploaded successfully"
    return "Error uploading file"