from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from database.project import interface

def Index(request):
	try:
		pres = interface.GetPres(request.GET['projecthash'])
		markdown = pres.presMarkdown.split("<break>")
		htmldata = {
			'markdownlist':markdown
		}
		return render(request, 'view/index.html', htmldata)
	except:
		return HttpResponseRedirect(reverse("apps.home.home.Index"))
