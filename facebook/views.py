from django.shortcuts import render, redirect
from facebook.models import article, Comment
from facebook.models import page
from facebook.models import good



from django.shortcuts import render, redirect

# 중간생략

def new_feed(request):
   # 데이터베이스 저장하는 작업하는 함수
   # 사용자가 게시버튼을 눌렀는가?
   if request.method == 'POST':
       #글저장
       new_article = article.objects.create(
           author=request.POST['author'],
           title=request.POST['title'],
           text=request.POST['content']+'-추신 감사합니다.',

           password=request.POST['password'],
       )
       return redirect(f'/feed/{ new_article.pk}')
   return render(request,'new_feed.html')

def remove_feed(request, pk):
   ddd = article.objects.get(pk=pk)

   if request.method == 'POST':
       if request.POST['password']==ddd.password:
           ddd.delete()
           return redirect('/')


   return render(request, 'remove_feed.html', {'feed': ddd})


def edit_feed(request, pk):
   ddd = article.objects.get(pk=pk)

   if request.method == 'POST':
       if request.POST['password']==ddd.password:
           ddd.author = request.POST['author']
           ddd.title = request.POST['title']
           ddd.text = request.POST['content']
           ddd.save()
       return redirect(f'/feed/{pk}')


       #아래와 같은 것들도 동일하게 가능함
   #return redirect('/feed/'+str(pk))
   #return redirect('/feed/{article.pk}')

   return render(request, 'edit_feed.html', {'feed':ddd})


def page(request):
   return render(request, 'page2.html')

def newsfeed(request):
   articles = article.objects.all()
   return render(request, 'newsfeed.html', { 'articles': articles })

def pages(request):
   pages = page.objects.all()
   return render(request, 'page_list.html', {'pages': pages })

def hello(request):
   whatis = good.objects.all()
   return render(request, 'hello.html', {'what': whatis })


def play(request):
  return render(request,'play.html')


count = 0
def play2(request):

  you='최지윤'
  age=29
  if age > 19 :
      상태 = '성인'
  else:
      상태 ='청소년'

  global count
  count = count + 1

  if count==7:
      status = '당첨'
  else :
      status = '꽝...'


  diary = ['10월 3일 -  인천에 갈것이다.', ' 10월 4일 - 강화도를 갈것이다.', '10월 5일']
  return render(request,'play2.html', { 'name': you, '몇':count, '나이': 상태, '방문':status, 'diary':diary,})

count=0
def event(request):
   im='최도근'

   age=24
   if age>19:
       hehe='성인'
   else :
       hehe='청소년'

   global count
   count=count+1
   if count==7:
       status='당첨!'
   else :
       status='꽝...'

   return render(request,'event.html', {'후후':im, '당신은':status, 'cnt':count, '나이':hehe})

def detail_feed(request,pk):
   feed=article.objects.get(pk=pk)
   if request.method =='POST':
       Comment.objects.create(
           article=feed,
           author=request.POST.get('author'),
           text=request.POST.get('text'),
           password=request.POST.get('password'),
       )

   return render (request, 'detail_feed.html', {'feed':feed})


