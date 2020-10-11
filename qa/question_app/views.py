from django.shortcuts import render,redirect
from .functions import get_random_obj
from user_app.models import ActiveQuestion,AnsweredQuestion
# Create your views here.
def index(request):
    user = request.user
    try:
        active = ActiveQuestion.objects.get(user=user)
    except:
        
        rand_word = get_random_obj()
        active = ActiveQuestion.objects.create(answer=rand_word, user=user)
        
    
        
        

    top10WrongAnswer=AnsweredQuestion.objects.filter(user=user).order_by('-false_count')[:10]
    if request.method == 'POST':
        
    
        userAnswer = request.POST.get('word').lower()
        obj, created = AnsweredQuestion.objects.get_or_create(answer=active.answer, user=user)
        rand_word = get_random_obj()
        

        if userAnswer == active.answer.translate:
            
            obj.true_count += 1
            
        else:
            obj.false_count += 1
        
        active.answer = rand_word
        active.save()
        obj.save()
        return redirect('main:empty')
    
    context = {
        'word':active,
        'wrongs': top10WrongAnswer
    }
    return render(request, 'index.html',context=context)
