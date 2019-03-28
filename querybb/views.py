from django.shortcuts import render
import requests

from bitbucket.client import Client

def query(request):
    # response = requests.get()
    # data = response.json()
    # return render(request, 'querybb/index.html', {'data':data})
    client = Client('me.tirtha91@gmail.com','Tirtha@1234')
    # response = client.get_repositories()
    # response = client.get_repository('jirabot')
    response = client.get_issue('jirabot')
    print(response)

    return render(request, 'querybb/index.html', {'data':response})
