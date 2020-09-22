from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi=NewsApiClient(api_key="b897c7212bba47a19652a06263f884a9")
    top_headlines=newsapi.get_top_headlines(sources='bbc-news')
    articles=top_headlines['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(articles)):
        myarticles=articles[i]
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
    mylist=zip(news,desc,img)
    return render(request,'index.html',context={'mylist':mylist})
