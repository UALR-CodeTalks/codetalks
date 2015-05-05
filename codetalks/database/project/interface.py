from database.project.models import Presentation
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

def GetPresFromName(filterName = ''):
	return Presentation.objects.filter(presName__icontains = filterName)

def AlterMarkdown(presHash, newMarkdown):
	try:
		pres = GetPres(presHash)
		pres.presMarkdown = newMarkdown
		pres.save()
		return True
	except:
		return False

def AlterName(presHash, newName):
	try:
		pres = GetPres(presHash)
		pres.presName = newName
		pres.save()
		return True
	except:
		return False

def DecRank(presHash):
	pres = GetPres(presHash)
	pres.presRank -= 1
	pres.save()

def IncRank(presHash):
	pres = GetPres(presHash)
	pres.presRank += 1
	pres.save()

def GetRank(presHash):
	return GetPres(presHash).presRank
