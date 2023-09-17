from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import pandas as pd
from get_from_api import get_loc

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'technovate'
# Username	Car-Seater	From_lat	From_long	To_lat	To_long	No-of-Passengers	Pickup_Time	Droppoff_Time
mysql = MySQL(app)

@app.route('/signup', methods=['POST'])
def signup():
	data = request.get_json()
	username = data['username']
	seater = data['seater']
	from_lat = data['fromLat']
	from_long = data['fromLong']
	to_lat = data['toLat']
	to_long = data['toLong']
	num_pass = data['numPass']
	print(username,seater)
	cur = mysql.connection.cursor()
	cur.execute("INSERT INTO carOwners (username,seater,fromLat,fromLong,toLat,toLong,numPass) VALUES ( %s,%s, %s,%s, %s,%s, %s)", (username, seater,from_lat,from_long,to_lat,to_long,num_pass))
	mysql.connection.commit()
	cur.close()

	return jsonify({"message": "Signup successful"}), 201

@app.route('/login', methods=['POST'])
def login():
   
    data = request.get_json()
    print(data)
    # username = data['username']

    # cur = mysql.connection.cursor()
    # cur.execute("SELECT * FROM carowners WHERE username = %s ", (username))
    # #print("done")
    # user = cur.fetchone()
    # cur.close()

    # if user:
    #     return jsonify({"message": "Login successful"}), 200
    # else:
    #     return jsonify({"message": "Login failed"}), 401

@app.route('/hell', methods=['POST'])
def get_data_to_csv():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM carOwners")
    x = cur.fetchall()
    df = pd.DataFrame(columns=["username","locs"])
    for i in x:
        points = [list(reversed([round(i[2],4),round(i[3],4)])),list(reversed([round(i[4],4),round(i[5],4)]))]
        
        new_df = {"username" : i[0],"locs" : get_loc(points)}
        try : 
            new_df["locs"] = new_df["locs"]["paths"]["points"]["coordinates"]
            print(new_df["locs"])
            df = pd.concat([df,new_df])
        except:
            #x = new_df["locs"]["message"]
            new_df["locs"] = [[72.866021, 19.260566], [72.865557, 19.260693], [72.865246, 19.259879], [72.864875, 19.259889], [72.863367, 19.259831], [72.862334, 19.259771], [72.862014, 19.259789], [72.861353, 19.259596], [72.86102, 19.25946], [72.859561, 19.258943], [72.859524, 19.258908], [72.859507, 19.258849], [72.859447, 19.258409], [72.859346, 19.25813], [72.859338, 19.257979], [72.859201, 19.257012], [72.859122, 19.256698], [72.859088, 19.256458], [72.859091, 19.256247], [72.858983, 19.25594], [72.859043, 19.255631], [72.859128, 19.255524], [72.85933, 19.255414], [72.859463, 19.255381], [72.859678, 19.255367], [72.859679, 19.255333], [72.859456, 19.255345], [72.859284, 19.255397], [72.859085, 19.255515], [72.859037, 19.255564], [72.858989, 19.255662], [72.858943, 19.255901], [72.858922, 19.255921], [72.858249, 19.256089], [72.858202, 19.25608], [72.858129, 19.256025], [72.858087, 19.255925], [72.857985, 19.254872], [72.858015, 19.254497], [72.858674, 19.25306], [72.859087, 19.249721], [72.859152, 19.24865], [72.859115, 19.246548], [72.858951, 19.243864], [72.858809, 19.242299], [72.858613, 19.241122], [72.858525, 19.240503], [72.85836, 19.239556], [72.857926, 19.237635], [72.857831, 19.236746], [72.857794, 19.23658], [72.857704, 19.236573], [72.857364, 19.236496], [72.856551, 19.23602], [72.856412, 19.235919], [72.856243, 19.23572], [72.855972, 19.235335], [72.855628, 19.235015], [72.855563, 19.234983], [72.855466, 19.234966], [72.855174, 19.234971], [72.854306, 19.235129], [72.853602, 19.23523], [72.853649, 19.233576], [72.853633, 19.233516], [72.853652, 19.233502], [72.853662, 19.233445], [72.853641, 19.233418], [72.853604, 19.232934], [72.853615, 19.23252], [72.853605, 19.231675], [72.853575, 19.231024], [72.853591, 19.231012], [72.853625, 19.230945], [72.853611, 19.230891], [72.853578, 19.230853], [72.853507, 19.230835], [72.853444, 19.23086], [72.853419, 19.23089], [72.852806, 19.230871], [72.852735, 19.228676], [72.852072, 19.228674], [72.852096, 19.228069], [72.852098, 19.227484], [72.852029, 19.22646], [72.851952, 19.22585], [72.851114, 19.225878], [72.850904, 19.225184], [72.850639, 19.224516], [72.850271, 19.223675], [72.850188, 19.223346], [72.850095, 19.223083], [72.849814, 19.222862], [72.849079, 19.222423], [72.848676, 19.222349], [72.847842, 19.222165], [72.847805, 19.220377], [72.847859, 19.220088], [72.84791, 19.219354], [72.844839, 19.21907], [72.844807, 19.218301], [72.844746, 19.21539], [72.844706, 19.215293], [72.844843, 19.214173], [72.844687, 19.212464], [72.844635, 19.212369], [72.84456, 19.212265], [72.844342, 19.211709], [72.844235, 19.21086], [72.844177, 19.210215], [72.843856, 19.209066], [72.843377, 19.208985], [72.843483, 19.208516], [72.843379, 19.208321], [72.843631, 19.208038], [72.843664, 19.207768], [72.843803, 19.20714], [72.843718, 19.207094], [72.843731, 19.206788], [72.843773, 19.206519], [72.843772, 19.206392], [72.843613, 19.205646], [72.843533, 19.205079], [72.843536, 19.204435], [72.842996, 19.203869], [72.842858, 19.203272], [72.842582, 19.202208], [72.842248, 19.201473], [72.84187, 19.200319], [72.841803, 19.200325], [72.841798, 19.199804], [72.841761, 19.199606], [72.841751, 19.198951], [72.842432, 19.198955], [72.842437, 19.198079], [72.842632, 19.195796], [72.842676, 19.195477], [72.842751, 19.194537], [72.842788, 19.194337], [72.842718, 19.194227], [72.842213, 19.193615], [72.841667, 19.193046], [72.841509, 19.192837], [72.84255, 19.192536], [72.842098, 19.191463], [72.841926, 19.190986], [72.841932, 19.190554], [72.84214, 19.189168], [72.842112, 19.188777], [72.842027, 19.188316], [72.841989, 19.187347], [72.842014, 19.187053], [72.841718, 19.185275], [72.842359, 19.185141], [72.842306, 19.18471], [72.842289, 19.184304], [72.842242, 19.183861], [72.842149, 19.183495], [72.842122, 19.183317], [72.842125, 19.182753], [72.842101, 19.18265], [72.842156, 19.182044], [72.842344, 19.180531], [72.84243, 19.180137], [72.842423, 19.179843], [72.842471, 19.17904], [72.84273, 19.17897], [72.843382, 19.17896], [72.844748, 19.178816], [72.845, 19.178772], [72.845377, 19.178516], [72.845635, 19.178372], [72.846309, 19.178123], [72.847073, 19.178041], [72.84855, 19.177801], [72.849106, 19.177219], [72.849284, 19.177008], [72.84924, 19.17695], [72.849295, 19.176618], [72.849246, 19.176501], [72.849312, 19.1753], [72.849401, 19.174326], [72.84939, 19.173566], [72.849452, 19.173188], [72.849564, 19.17202], [72.849658, 19.170415], [72.849576, 19.170166], [72.849626, 19.169229], [72.849581, 19.168421], [72.849594, 19.168266], [72.849669, 19.168114], [72.84984, 19.168043], [72.849834, 19.167809], [72.850344, 19.167805], [72.850844, 19.167648], [72.850365, 19.166909], [72.850686, 19.166775], [72.851394, 19.166218], [72.851641, 19.166147], [72.852638, 19.166222], [72.852699, 19.165002], [72.852811, 19.164767], [72.852607, 19.164546], [72.852677, 19.163593], [72.852784, 19.162894], [72.852816, 19.162103], [72.852798, 19.161376], [72.853265, 19.16128], [72.85377, 19.161227], [72.854253, 19.161202], [72.854368, 19.159803], [72.854768, 19.15906], [72.854439, 19.158713], [72.854311, 19.15849], [72.854159, 19.157967], [72.85397, 19.157542], [72.854654, 19.157203], [72.855566, 19.156899], [72.856465, 19.156863], [72.85642, 19.15617], [72.856516, 19.15577], [72.856704, 19.155183], [72.856639, 19.155007], [72.856545, 19.154444], [72.856437, 19.153587], [72.856363, 19.15261]]
            # Starting position
            
    user = cur.fetchone()
    print(df)
    cur.close()
    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Login failed"}), 401
if __name__ == '__main__':
    app.run(debug=True)