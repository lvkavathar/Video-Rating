#!/usr/bin/python

from flask import Flask, jsonify, render_template, request, abort, make_response
from flask import Response
import requests
import json
import mysql.connector

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False

@app.route('/')
def webprint():
    return render_template('index.html')

@app.route('/api/url',methods=['GET','POST'])
def youtube():
 videoId = request.args.get('cmd')
 url = 'https://www.googleapis.com/youtube/v3/commentThreads?key=AIzaSyDMbl59GjgDpijv459eR6NwpnkQkQvyd1w&textFormat=html&part=snippet&maxResults=100&videoId=' + videoId  
 response=requests.get(url)
 data = json.loads(response.content)
 count = data["pageInfo"]["totalResults"]
 con = mysql.connector.connect(user='root',password='toor',host='127.0.0.1',database='hackYoutube')
 cur = con.cursor(buffered=True)
 rowarray_list = []
 for x in range(1,count):
        count = 0
        try :
          words = data["items"][x]["snippet"]["topLevelComment"]["snippet"]["textOriginal"].split(' ')
        except Exception:
          pass
 	for word in words:
            word = word.strip('\'')
            try :
             cur.execute("""SELECT * FROM badWords WHERE list=%s""",(word, ))
             if cur :
	    	count = count+1
            except Exception :
                 pass
        c = count
        a = data["items"][x]["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
        b = data["items"][x]["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"]
        d = data["items"][x]["id"]
        t = {"userName" : a,"profilePic" : b,"badWords" : c}
        rowarray_list.append(t)
        args = (data["items"][x]["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],data["items"][x]["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"],count,data["items"][x]["id"],)
        query = "INSERT INTO user_details VALUES (%s,%s,%s,%s)"
        cur.execute(query,args)
        con.commit()  
 j = json.dumps(rowarray_list)                  
 cur.close()
 con.close()

   
 return Response(j,status = response.status_code,mimetype="application/json")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='80')
