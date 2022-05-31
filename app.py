from Flask import Flask,render_template,request,jsonify
import numpy as np
import pickle


app=Flask(__name__)
model1=pickle.load(open("Loan_prediction.pkl","rb"))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final_features=[np.array(int_features)]
    prediction=model1.predict(final_features)

    output=prediction[0]
    if int(output)== 0:
            output ='Sorry!! Loan wil not be given to customer'
    else:
            output ='Congratulations Loan wil  be given to customer'

    return render_template('index.html',prediction_text='Loan = {}'.format(output))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)