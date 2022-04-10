from flask import Flask,render_template,request
import pickle
model=pickle.load(open('./houseprice.pkl','rb'))
app=Flask(__name__)
@app.route('/')
def loadPage():
    return render_template('index.html')
@app.route('/predict',methods=["POST"])
def predict():
    a=float(request.form["lotArea"])
    b=float(request.form["MasVnrArea"])
    c=float(request.form["BsmtUnfSF"])
    d=float(request.form["TotalBsmtSF"])
    e=float(request.form["1stFlrSF"])
    f=float(request.form["2ndFlrSF"])
    g=float(request.form["GrLivArea"])
    h=float(request.form["GarageArea"])
    i=float(request.form["WoodDeckSF"])
    j=float(request.form["OpenPorchSF"])
    

    res=model.predict([[a,b,c,d,e,f,g,h,i,j]])
    return render_template('index.html',z=res[0])
if __name__=="__main__":
    app.run(debug=True)