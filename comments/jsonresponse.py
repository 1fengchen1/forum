from django.http import HttpResponse
import json
def json_response(obj):
    txt = json.dumps(obj)
    return HttpResponse(txt)