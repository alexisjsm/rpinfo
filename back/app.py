from flask import Flask, jsonify
from flask_cors import CORS
import platform, os, shutil, getpass, math

app = Flask(__name__)
cors = CORS(app, resource = {r"/api/*":{"origins": "*"}})

@app.route('/api/v1/info_system')
def info_system():
    data = platform.uname()
    return jsonify(data)

@app.route('/api/v1/info_space_disk/')
def info_get_diskAll():
    username = getpass.getuser()
    for ls in os.listdir("/media/"):
        if(ls == username):
            dirlist = os.listdir("/media/"+username)
        else:
            dirlist = os.listdir("/media/")   
    return jsonify(dirlist)

@app.route('/api/v1/info_space_disk/<nameDisk>')
def info_space_diskHD(nameDisk):
    username = getpass.getuser()
    disk = shutil.disk_usage("/media/"+username+"/"+nameDisk)

    total = convert(disk[0])
    used  = convert(disk[1])
    free  = convert(disk[2])
    
    data = {"total": total, "used":used, "free": free}

    return jsonify(data)

def convert(Byte):
    if (Byte == 0):
        return Byte
    n = 1024
    size = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    i = math.floor(math.log(Byte) / math.log(n))
    
    return str(round(Byte / math.pow(n,i),2)) + ' ' + size[i]
    

if __name__ == '__main__':
    app.run(debug= True)

