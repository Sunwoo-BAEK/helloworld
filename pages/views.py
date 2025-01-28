import pickle
import pandas as pd
import pdb
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from models import Item, ToDoList

def homePageView(request):
    return render(request,
        'home.html',
        {'mynumbers':[1,2,3,4,5,6,],'firstName':'Sunwoo', 'lastName':'Baek'}
    )

def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

def sunwooPageView(request):
    # return request object and specify page.
    return render(request, 'sunwoo.html')

def homePost(request):
    # Create variable to store choice that is recognized through entire function.
    choice = -999
    gmat = -999  # Initialize gmat variable.

    try:
        # Extract value from request object by control name.
        currentChoice = request.POST['choice']
        gmatStr = request.POST['gmat']
        # print("Just before Sunwoo's Breakpoint")
        # pdb.set_trace()
        # breakpoint()
        # print("Just after breakpoint")

        # Crude debugging effort.
        print("*** Years work experience: " + str(currentChoice))
        choice = int(currentChoice)
        gmat = float(gmatStr)

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The choice was missing please try again',
            'mynumbers': [1, 2, 3, 4, 5, 6, ]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'choice':choice,'gmat':gmat},))

def results(request, choice, gmat):
    print("*** Inside reults()")
    # load saved model

    # For windows, we use full address instead of just "../model_pkl". So unfairrr.
    with open('/Users/sunwo/OneDrive/Desktop/CST Diploma/Term4/Comp4949_BigData/lectures/django/helloworld/model_pkl' , 'rb') as f:
        loadedModel = pickle.load(f)

    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['gmat', 'work_experience'])

    workExperience = float(choice)
    print("*** GMAT Score: " + str(gmat))
    print("*** Years experience: " + str(workExperience))
    singleSampleDf = singleSampleDf._append({'gmat':gmat,
                                            'work_experience':workExperience},
                                        ignore_index=True)

    singlePrediction = loadedModel.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))

    return render(request, 'results.html', {'choice': workExperience, 'gmat':gmat,
                'prediction':singlePrediction})

def todos(request):
    print("*** Inside todos()")
    items = Item.objects
    itemErrandDetail = items.select_related('todolist')
    print(itemErrandDetail[0].todolist.name)
    return render(request, 'ToDoItems.html',
                {'ToDoItemDetail': itemErrandDetail})