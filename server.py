__author__ = 'raviteja_ganireddy'

from bottle import route, run, request, get, post, response
from irs import *


@route('/hello')
def gethello():
    return "hello world"

@route('/search', method='POST')
def get_resuts():
    data1=request.POST['keyword']
    data=request.POST['keyword1']
    l1=search(data1)
    l2=search(data)
    if(l1==False):
        return href(l2)
    if(l2==False):
        return href(l1)
    boolean=request.POST['boolean']
    if boolean == "and":
        l=intersect(l1,l2)
    else:
        l=union(l1,l2)
    return href(l)

run(host='localhost', port=8081, debug=True, reloader=True)
