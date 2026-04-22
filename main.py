'''
SOAP Server
Made by Let's Shop 2024 (now mantained by Ghibbi64)
'''
print("Shopdeck Server - SOAP XML Services\n\nBy Let's Shop Team 2024 & Ghibbi64\n\n\n")
print("----------------------------------")

from flask import Flask
import ecs, ias, cas, cdn, assetcdn, nus

app = Flask(__name__)
app.register_blueprint(ecs.ecs)
app.register_blueprint(ias.ias)
app.register_blueprint(cas.cas)
app.register_blueprint(nus.nus)
app.register_blueprint(cdn.ccs)
app.register_blueprint(assetcdn.cdn)

print("READY!")