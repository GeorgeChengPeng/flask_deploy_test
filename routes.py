from config import app
from controller_functions import root,dojo,ninja

app.add_url_rule("/",view_func=root)
app.add_url_rule("/dojo_process",view_func=dojo,methods=["POST"])
app.add_url_rule("/ninja_process",view_func=ninja,methods=["POST"])