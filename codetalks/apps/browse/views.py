from django.http import HttpResponse
from django.shortcuts import render
from database.project import interface
import json

def Index(request):

	if 'filterstring' in request.GET:
		projects = interface.GetPresFromName(request.GET['filterstring'])
	else:
		projects = interface.GetPresFromName()
	if 'order' in request.GET:
		if request.GET['order'] == "asc":
			projects = projects.order_by('-presRank')
		elif request.GET['order'] == "desc":
			projects = projects.order_by('presRank')
	htmldata = {
		'projects':projects
	}
	return render(request, 'browse/browserhome.html', htmldata)
