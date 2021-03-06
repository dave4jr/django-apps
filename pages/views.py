#*====================== #
#*  Author:		 Dave Luke Jr
#*  Company:	 CenterStack.io
#*  Description:	 pages/views.py
#*====================== #
import os
from django.shortcuts import render

APP_DIR = os.path.dirname(os.path.abspath(__file__))
APP_NAME = os.path.basename(APP_DIR)

def navigation(request, template):
	url = os.path.join(APP_NAME, template)
	return render(request, url)