from django.http import HttpResponse

from msclassapp.models import Scripture, Question, Trait
import datetime
from django.utils import simplejson

def scriptureAPI(request):
	dateStr=request.GET['date']
	scriptures = Scripture.objects.all()
	scripture = Scripture.objects.get(pk=1)
	mydate = datetime.datetime.strptime(dateStr, "%d%m%Y").date()

	for s in scriptures:
		print s.view_date.date()
		print mydate
		if s.view_date.date() == mydate:
			scripture = s
			break

	qlist = []

	for question in scripture.question_set.all():
		qlist.append(question.serializeForJson())
	to_json = {
        "scripture": scripture.serializeForJson(),
        "questions": qlist
    }

	return HttpResponse(simplejson.dumps(to_json), mimetype="application/json")
