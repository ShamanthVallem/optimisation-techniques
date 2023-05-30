from flask import Flask, render_template, request
import numpy as np
from simplex import simplexMethod, optimalValues
from revised_simplex import revisedSimplexMethod
app = Flask(__name__) 

@app.route("/") 
def data():
    return render_template("data.html")


@app.route("/calculate", methods = ['post'])
def calculate():
    global minOrMax
    minOrMax = (request.form["minOrMax"])
    # global function
    # function = (request.form["function"])
    global numOfConstraints
    numOfConstraints = int(request.form['numOfConstraints'])
    global inequalityConstraints
    inequalityConstraints = int(request.form['numOfInequalityConstraints'])

    if(numOfConstraints < inequalityConstraints):
        return render_template("data.html")
    coeff_value_list = [6, 4, 7, 5]
    ineq_value_list = [[1, 2, 1, 2, 20], [6, 5, 3, 2, 100], [3, 4, 9, 12, 75]]
    return render_template("calculate.html", minOrMax = minOrMax, numOfConstraints = numOfConstraints, inequalityConstraints = inequalityConstraints, coeff_value_list=coeff_value_list, ineq_value_list=ineq_value_list)
    # return render_template("calculate.html", minOrMax = minOrMax, numOfConstraints = numOfConstraints, inequalityConstraints = inequalityConstraints)


@app.route("/output", methods = ["post"])
def output():
    
    global functionCoeffecientMatrix
    # functionCoeffecientMatrix = np.zeros((1, int(numOfConstraints - inequalityConstraints)))
    functionCoeffecientMatrix = []
    for i in range(int(numOfConstraints - inequalityConstraints)):
        # functionCoeffecientMatrix[i] = request.form["objcof"+str(i)]
        functionCoeffecientMatrix.append(int(request.form["objcof"+str(i)]))


    global inequalityMatrix
    inequalityMatrix = np.zeros((inequalityConstraints, int(numOfConstraints - inequalityConstraints)))
    for i in range(inequalityConstraints):
        for j in range(int(numOfConstraints - inequalityConstraints)):
            inequalityMatrix[i][j] = request.form["iqrsts"+str(i)+str(j)]

    global constantMatrix
    # constantMatrix = np.zeros((1, inequalityConstraints))
    constantMatrix = []
    for i in range(inequalityConstraints):
        # constantMatrix[i] = request.form["iqrsts"+str(i)+str(int(numOfConstraints - inequalityConstraints))]
        constantMatrix.append(int(request.form["iqrsts"+str(i)+str(int(numOfConstraints - inequalityConstraints))]))

    global method
    method = request.form["methods"]

    global finalResult
    if(method == "simplex"):
        finalResult = simplexMethod(functionCoeffecientMatrix, inequalityMatrix, constantMatrix, minOrMax)
        optimalValues_list = optimalValues(finalResult[-1])
    elif(method == "revisedSimplex"):
        finalResult = revisedSimplexMethod(functionCoeffecientMatrix, inequalityMatrix, constantMatrix, minOrMax)


    return render_template("output.html", minOrMax = minOrMax, numOfConstraints = numOfConstraints, inequalityConstraints = inequalityConstraints, functionCoeffecientMatrix = functionCoeffecientMatrix, inequalityMatrix = inequalityMatrix, constantMatrix = constantMatrix, method = method, finalResult = finalResult,optimalValues_list = optimalValues_list)


@app.route("/docs")
def docs():
    return render_template("docs.html")
# Function to extract coefficients from given equation
def extractVariables(eq):
    eq = eq.split()
    removez = []
    equaltity = False

    for i in range(len(eq)):
        if(i%2 == 1):
            if(eq[i] == "-"):
                eq[i+1] = "-"+eq[i+1]
            if(eq[i] == "<" or eq[i] == ">" or eq[i] == "="):
                eq[i+1] = eq[i+1]+"constant"
                equaltity = True
            removez.append(eq[i])

    for i in eq:
        if(i in removez):
            eq.remove(i)

    coeff = {}
    for i in range(len(eq)):
        if(i == len(eq)-1 and equaltity == True):
            var = "constant"
            num = eq[i][:-8]
        else:
            var = eq[i][-1]
            num = eq[i][:-1]
        if(num == ""):
            num = 1
        elif(num == "-"):
            num = -1
        coeff[var] = num
    return coeff

if __name__ == "__main__":
    app.run(debug = True)
