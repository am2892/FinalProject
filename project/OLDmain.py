from flask import Blueprint, render_template, request
from . import db
from flask_login import login_required, current_user
from .models import functions

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

def returnCorrectHistory(history, itemsToReturn):
    for item in history:
        if item.userName == current_user.name:
            itemsToReturn.append(item)

def deleteCorrectItems(history, itemsToReturn):
    for item in history:
        if item.userName == current_user.name:
            db.session.delete(item)
            db.session.commit()
    itemsToReturn=history

@main.route('/delete_component/<component_id>')
@login_required
def delete_component(component_id):
    component = functions.query.filter_by(id=component_id).first_or_404()
    db.session.delete(component)
    db.session.commit() 
    itemsToReturn = []
    history = functions.query.all()
    for item in history:
        if item.userName == current_user.name:
            itemsToReturn.append(item)
    return render_template('profile.html', logCount=itemsToReturn, name=current_user.name)

@main.route('/return_numbers/<component_id>')
@login_required
def return_numbers(component_id):
    component = functions.query.filter_by(id=component_id).first_or_404()
    numbers = component.numbers
    itemsToReturn = []
    history = functions.query.all()
    for item in history:
        if item.userName == current_user.name:
            itemsToReturn.append(item)
    return render_template('profile.html', logCount=itemsToReturn, name=current_user.name, numbers=numbers)

@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    currentNumbers = 0
    if request.method == 'POST':
        dataset = request.form['dataset'].replace(" ", "")
        operation = request.form['function']

        if operation == 'deleteAll':
            print('delete')
            history = functions.query.all()
            itemsToReturn = []
            deleteCorrectItems(history, itemsToReturn)
            return render_template('profile.html', logCount=itemsToReturn, name=current_user.name)

        if operation == 'mean':
            if len(dataset) > 0 :
                print('dataset: ', dataset)
                new_function = functions(userName=current_user.name,functionName='mean', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import populationMean
                answer = float(populationMean(dataset))
                error=False
            else :
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            print('error: ', error)
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'median':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='median',numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import median
                answer = float(median(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'mode':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='mode', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import mode
                answer = float(mode(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)

        elif operation == 'population-standard-deviation':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='populationStandardDeviation', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import populationStandardDeviation
                answer = float(populationStandardDeviation(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)

        elif operation == 'variance-population-proportion':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='variancePopulationProportion', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import variancePopulationProportion
                answer = float(variancePopulationProportion(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)

        elif operation == 'z-score':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='zScore', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import zScore
                answer = zScore(dataset)
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)

        elif operation == 'standardized-score':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='standardizedScore', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import standardizedScore
                answer = standardizedScore(dataset)
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'pcc':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='PCC', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import populationCorrelationCoefficient
                answer = float(populationCorrelationCoefficient(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name,error=error, numbers=0)
        elif operation == 'confidence-interval':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='confidenceInterval', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import confidenceInterval
                answer = (confidenceInterval(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True

            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'variance':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='variance', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import variance
                answer = float(variance(dataset))
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'p-value':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='pValue', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import pValue
                answer = pValue(dataset)
                error=False
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'proportion':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='proportion', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import proportion
                answer = (proportion(dataset))
                error=False            
            else: 
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'sample-mean':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='sampleMean', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import sampleMean
                answer = float(sampleMean(dataset))
                error=False                
            else:
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'sample-standard-deviation':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='standardDeviation', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import standardDeviation
                answer = float(standardDeviation(dataset))
                error=False
            else: 
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        elif operation == 'variance-sample-proportion':
            if len(dataset) > 0:
                new_function = functions(userName=current_user.name,functionName='varianceSampleProportion', numbers=dataset)
                db.session.add(new_function)
                db.session.commit()
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                from project.StatisticalFunctions import varianceSampleProportion
                answer = float(varianceSampleProportion(dataset))
                error=False
            else: 
                answer = 'input cannot be empty, try again'
                history = functions.query.all()
                itemsToReturn = []
                returnCorrectHistory(history, itemsToReturn)
                error=True
            return render_template('profile.html', answer=answer, logCount=itemsToReturn, name=current_user.name, error=error, numbers=0)
        else:
            return render_template('profile.html', name=current_user.name)
    
    history = functions.query.all()
    itemsToReturn = []
    returnCorrectHistory(history, itemsToReturn)
    return render_template('profile.html', name=current_user.name, logCount=itemsToReturn, numbers=0)
