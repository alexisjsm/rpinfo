import  config
from flask import Flask, jsonify,request, render_template
from flask_cors import CORS
from cpuinfo import get_cpu_info
import platform, psutil, math, re, distro,subprocess

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
    data = []
    for d in disk:
        if(type(d)==float):
            data.append(str(d) + "%")
        else:
            data.append(convert(d))

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
    cpuPercent = [ psutil.cpu_percent(interval=1) ]
    return jsonify(cpuPercent)

@app.route('/api/v1/cpu_frequent', methods=['POST'])
def cpu_frequent ():
    cpuFrequent = psutil.cpu_freq()
    return jsonify(cpuFrequent)

@app.route('/api/v1/cpu_temp')
def cpu_temp():
     arg = ['vcgencmd','measure_temp']
     temp = subprocess.Popen(arg,stdout=subprocess.PIPE,stdin=subprocess.PIPE,encoding="utf8")
     out, _ = temp.communicate()
     regx = r"^temp=|.['C]\n$"
     data =  re.split(regx,out,re.MULTILINE)
     number = float(data[1])
     return jsonify(number)

     
     

@app.route('/api/v1/memory_info')
def memory_info ():
    data = psutil.virtual_memory()
    ram  = []
    print(len(data))
    for r in range(0,5):
        if(type(data[r]) == float):
            ram.append(str(data[r]) + "%")
        else:
            ram.append(convert(data[r]))
    return jsonify(ram)

@app.route('/', defaults ={ 'path' : ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")
  
if __name__ == '__main__':
    app.run(host=config.url['HOST'], port=config.url['PORT']) 

