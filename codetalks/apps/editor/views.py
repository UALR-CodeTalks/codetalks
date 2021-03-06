from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from database.project import interface

def Index(request):
	try:
		project = interface.GetPres(request.GET['projecthash'])
		htmldata = {
			'pres': project
		}
		return render(request, 'editor/editorhome.html', htmldata)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))

def GetNewProject(request):
	project = interface.NewPres()
	if project is not None:
		url = reverse('editor:index')
		url += "?projecthash="
		url += project.presHash
		return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect(reverse('apps.home.home.Index'))

def SaveCode(request):
	result = interface.AlterMarkdown(request.POST['projecthash'], request.POST['code'].replace("<//script>", "</script>"))
	returnString = "The code was saved." if result else "An error occured."
	return HttpResponse(returnString)

def AlterName(request):
	result = interface.AlterName(request.POST['projecthash'], request.POST['name'])
	returnString = "The name was changed." if result is True else "An error occured."
	return HttpResponse(returnString)

def Vote(request):
	change = request.POST['vote']
	if change == '0':
		interface.DecRank(request.POST['projecthash'])
	elif change == '1':
		interface.IncRank(request.POST['projecthash'])
	return HttpResponse(interface.GetRank(request.POST['projecthash']))
