from django.http import HttpResponse
from db.project import interface
import json

def GetHashes(request):
	preses = GetPresFromHash()
	hashes = [[pres.presHash, pres.presName] for pres in preses]
	return HttpResponse(json.dumps({'hashes':hashes}))
