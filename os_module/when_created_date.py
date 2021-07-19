import os
import datetime
timestamp = os.path.getmtime("aspiration.pdf")
datetime.datetime.fromtimestamp(timestamp)