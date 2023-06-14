# optimisation-techniques

This is a Web portal to calculate max/min value of any objective function using linear programming methods.

<b>How to run the file</b>:
1. Fork this repository
2. Clone it into your local machine using "git clone "URL"
3. Navigate to the project directory using cmd
3. Run the following command to install required libraries:
```
pip install -r requirements.txt
```
4. Now, run app.py file using the following command:
```
python app.py
```
5. Url of the local server will be displayed, use ctrl+click on the url name to access the web portal.

<b>Inputs</b>:
1. Provide type of problem(maximization or minization) and total number of constraints(inequality + non-negative constraints)
2. Provide number of inequality constraints and click on next
3. Next, Add the coefficients of objective function
4. Add coefficients of all inequality constraints along with constants
5. Choose a method(only simplex is available as of now, but more methods will be added soon)
6. Hola! All the info needed along with all BFS, max/min(objective function) and values of x1, x2, x3, ..... will be calculated.
