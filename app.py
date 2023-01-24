'''

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0.

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


__author__ = "@netwookie"
__credits__ = ["Rick Kauffman"]
__license__ = "Apache2"
__version__ = "0.1.1"
__maintainer__ = "Rick Kauffman"
__status__ = "Alpha"

'''
from flask import Flask, request, render_template, abort, redirect, url_for
import pymongo
import os
from jinja2 import Environment, FileSystemLoader
from bson.json_util import dumps
from bson.json_util import loads
from utility.client import get_client
from pycentral.configuration import Groups
#
app = Flask(__name__)

# A dictionary of the mongo database credentials
config = {
    "username": "admin",
    "password": "siesta3",
    "server": "mongo",
}

# Setup database connetor
connector = "mongodb://{}:{}@{}".format(config["username"], config["password"], config["server"])
client = pymongo.MongoClient(connector)

#set mongo database
db = client["demo2"]

'''
#-------------------------------------------------------------------------------
Main Page
#-------------------------------------------------------------------------------
'''

@app.route("/", methods=('GET', 'POST'))
def login():


        message = "Use the group menu"
        return render_template('home.html', message=message)


'''
#-------------------------------------------------------------------------------
Home
#-------------------------------------------------------------------------------
'''

@app.route("/home", methods=('GET', 'POST'))
def home():

    my_central = []
    info = db.central.find({})
    docs = loads(dumps(info))
    for d in docs:
        group_name = d['group_name']
        description = d['description']

        info2 = [number, group_name, description]
        my_central.append(info2)
    message = "Operation completed successfully"
    return render_template('home1.html', message=message, my_central=my_central)



'''
#-------------------------------------------------------------------------------
Group Section
#-------------------------------------------------------------------------------
'''

@app.route("/add_group", methods=('GET', 'POST'))
def add_group():
    if request.method == 'POST':
        central = get_client()
        # Get form values
        group_name = request.form['group_name']
        group_password = request.form['group_password']
        wired_template = False
        wireless_template = False

        groups = Groups()

        response = groups.create_group(conn=central,
                                      group_name=group_name,
                                      group_password=group_password,
                                      wired_template=wired_template,
                                      wireless_template=wireless_template)


        code = response['code']

        if code != 201:
            message = 'Got return code %s operation failed' % (code)

        # TODO check to see record was written to database)
        message = 'Group information written to database %s:' % (code)
        return redirect(url_for('home', message=message))

    return render_template('add_group.html')

@app.route("/get_groups", methods=('GET', 'POST'))
def get_groups():

    central = get_client()

    my_central = []

    all_groups = Groups()

    response = all_groups.get_groups(conn=central,limit=50)

    groups = (response['msg']['data'])


    # Check user credentials
    return render_template('get_groups.html', groups=groups)


@app.route("/delete_group", methods=('GET', 'POST'))
def delete_group():
    central = get_client()

    # If HTTP POST then do this section
    if request.method == 'POST':
        group_name = request.form['group']

        groups = Groups()

        response = groups.delete_group(conn=central,group_name=group_name)

        code = response['code']
        message = 'The Group has been deleted %s ' % (code)
        return redirect(url_for('home', message=message))

    # If it is a HTTP GET do this section first
    my_central = []

    all_groups = Groups()

    response = all_groups.get_groups(conn=central,limit=50)

    groups = (response['msg']['data'])

    return render_template('delete_group.html', groups=groups)
