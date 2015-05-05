from db.project.models import Presentation
from common.helpers import hashtool
import time

def NewPres(markdown = ''):
	try:
		pres = Presentation()
		timeStamp = time.time()
		timeStamp = str(timeStamp)
		pres.presHash = hashtool.GetHash(timeStamp)
		pres.presMarkdown = markdown
		pres.save()
		return pres
	except:
		return None

def GetPres(presHash):
	try:
		pres = Presentation.objects.get(presHash = presHash)
		return pres
	except:
		return None

def GetPresFromHash(presHash = None):
	if presHash is None:
		return Presentation.objects.all()
	else:
		return Presentation.objects.get(presHash = presHash)

def GetPresFromName(filterName = ''):
	return Presentation.objects.filter(presName__in = filterName)

def AlterMarkdown(presHash, newMarkdown):
	try:
		pres = GetPres(presHash)
		pres.presMarkdown = newMarkdown
		pres.save()
		return True
	except:
		return False
