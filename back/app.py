import  config
from flask import Flask, jsonify,request, render_template
from flask_cors import CORS
from cpuinfo import get_cpu_info
import platform, psutil, math, re, distro

app = Flask(__name__,static_folder='./templates/static')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['JSON_SORT_KEYS'] = False

@app.route('/api/v1/info_system')
def info_system():
    system = platform.system()
    getdist = distro.linux_distribution()
    dist = " ".join(getdist)

    release = platform.release()
    nameMachine = platform.node()
    arch = platform.machine()
    data = [system,nameMachine,release,dist,arch]
    return jsonify(data)

@app.route('/api/v1/info_space_disk/', methods=['POST'])
def info_get_diskAll():
    disklist = []
    regx = re.compile("^/dev/sd.[1-9]")

    for diskn in psutil.disk_partitions(all=False):
        if(re.match(regx,diskn.device)):
            disk = {"device": diskn.device, "mountpoint": diskn.mountpoint, "fstype": diskn.fstype}
            disklist.append(disk)
    return jsonify(disklist)

@app.route('/api/v1/info_space_disk/disk', methods=['POST'])
def info_space_diskHD():
    diskmount = request.get_json()
    disk = psutil.disk_usage(diskmount['path'])
    total = convert(disk[0])
    used  = convert(disk[1])
    free  = convert(disk[2])
    percentage = str(disk[3]) + " %"
    
    data = {'Total': total, 'Used':used, 'Free': free, 'Percentage': percentage}
    return jsonify(data)

def convert(Byte):
    if (Byte == 0):
        return Byte
    n = 1024
    size = ['Bytes', 'KB', 'MB', 'GB', 'TB']
    i = math.floor(math.log(Byte) / math.log(n))
    return str(round(Byte / math.pow(n,i),2)) + ' ' + size[i]

@app.route('/api/v1/cpu_info')
def cpu_info():
    cpuinfo = get_cpu_info()
    cpuphysical = psutil.cpu_count(logical=False)
    data = [ cpuinfo['brand'], cpuinfo['count'], cpuphysical]

    return jsonify(data)

@app.route('/api/v1/cpu_percent', methods=['POST'])
def cpu_percent():
    cpuPercent = [ psutil.cpu_percent(interval=1.5) ]
    return jsonify(cpuPercent)

@app.route('/api/v1/cpu_frequent', methods=['POST'])
def cpu_frequent ():
    cpuFrequent = psutil.cpu_freq()
    return jsonify(cpuFrequent)

@app.route('/', defaults ={ 'path' : ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")
  
if __name__ == '__main__':
    app.run(debug=True) 

