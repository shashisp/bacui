from permute.models import CoulumA, CoulumB, CoulumC, CoulmD, CoulumE
#from forms import DataImport
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response

def upload(self, commit=False, *args, **kwargs):
        form_input = DataImport()
        #self.place = self.cleaned_data['place']
        file_csv = request.FILES['file_to_import']
        datafile = open(file_csv, 'rb')
        records = csv.reader(datafile)
        for line in records:
            self.dataa = line[1]
            form_input.save()
        datafile.close()



def render(request):
	a = CoulumA.objects.all()
	b = CoulumB.objects.all()
	c = CoulumC.objects.all()
	d = CoulmD.objects.all()
	e = CoulumE.objects.all()
	context = { 'a' : a, 'b' : b, 'c' : c, 'd' : d, 'e' : e}
	return render_to_response('render.html', context, context_instance=RequestContext(request))
    #return render_to_response(request, 'data.html', ctx)



def que(request):
	#from permute.models import CoulumA, CoulumB, CoulumC, CoulmD,CoulumE
    cola = request.GET['cola']
    colb = request.GET['colb']
    colc = request.GET['colc']
    cold = request.GET['cold']
    cole = request.GET['cole']
    mainlist = [cola, colb, colc, cold, cole]
    for i in mainlist:
    	print i

    return HttpResponseRedirect('/test')