from django.http import HttpResponse
from db.project import interface
import json

def Index(request):
	return render('view/view.html')

def GetHashes(request):
	preses = interface.GetPresFromHash()
	hashes = [[pres.presHash, pres.presName] for pres in preses]
	return HttpResponse(json.dumps({'hashename':hashes}))
