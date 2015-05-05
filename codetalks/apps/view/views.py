from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from database.project import interface

def Index(request):
	# try:
	return render(request, 'view/index.html')
	# except:
	# 	return HttpResponseRedirect(reverse("apps.home.home.Index"))
#
# def GetNewProject(request):
# 	projectHash = interface.GenerateNewProject()
# 	if projectHash is not None:
# 		url = reverse('editor:index')
# 		url += "?projecthash="
# 		url += projectHash
# 		return HttpResponseRedirect(url)
# 	else:
# 		return HttpResponseRedirect(reverse('apps.home.home.Index'))
#
# def Fork(request):
# 	result = interface.Fork(request.POST['projecthash'])
# 	returnString = "The code was forked." if result else "An error occured."
# 	return HttpResponse(returnString)
#
# def SaveCode(request):
# 	result = interface.SaveCode(request.POST['projecthash'], request.POST['code'])
# 	returnString = "The code was saved." if result else "An error occured."
# 	return HttpResponse(returnString)
#
# def AlterPublicPrivate(request):
# 	result = interface.AlterPublicPrivate(request.POST['projecthash'])
# 	returnString = "Make Private" if result else "Make Public"
# 	return HttpResponse(returnString)
#
# def AlterName(request):
# 	result = interface.ChangeName(request.POST['projecthash'], request.POST['name'])
# 	returnString = "The name was changed." if result is True else "An error occured."
# 	return HttpResponse(returnString)
