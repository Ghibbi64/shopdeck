from flask import Blueprint, request, render_template, make_response
import xmltodict, time, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopdeck.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from shopdeckdb.models import *
from django.core.exceptions import ObjectDoesNotExist

print("NUS Starting Up")

nus = Blueprint("nus", "nus")
@nus.route("/nus/services/NetUpdateSOAP", methods=['POST'])
def soap():
    if request.get_data() == b"IwI":
        return "TwT"
    try:
        parsed = xmltodict.parse(request.get_data())
    except:
        return "Error"
    if "nus:GetSystemTitleHash" in parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']:
        try:
            ds = parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']['nus:GetSystemTitleHash']['nus:DeviceId']
        except ObjectDoesNotExist:
            return "Error"
        title_hash="C0CA780FC2BC26D3B4E791A3E6F1EBC9"
        r = make_response(render_template("nus/GetSystemTitleHash.xml", id=ds, message=parsed['SOAP-ENV:Envelope']['SOAP-ENV:Body']['nus:GetSystemTitleHash']['nus:MessageId'], time=int(round(time.time()*1000)), titlehash=title_hash, nusname="GetSystemTitleHashResponse"))
        r.headers.set("Content-Type", "text/xml; charset=utf-8")
        return r