<<<<<<< HEAD
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("/data_resolver/index_20200514")

def register(request):
=======
#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.http import HttpResponseRedirect

def index(request):
	return HttpResponseRedirect("/data_resolver/index_20200514")

def register(request):
>>>>>>> edb34653d679429b0461f4c57d1574c628cb1793
	return HttpResponseRedirect("/data_resolver/register")