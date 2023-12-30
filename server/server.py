from microdot import Microdot
import mm_wlan

def read(path):
    try:
        with open(path) as fd:
            return fd.read()
    except Exception as e:
        print(e,path)
        
mime = {
    'html':'text/html',
    'js':'text/javascript',
    'css':'text/css',
    'json':'application/json',
    'jpg':'image/jpeg',
    'png':'image/png',
    'svg':'image/svg+xml',
    'ico':'image/vnd.microsoft.icon'
}
    
app = Microdot()  
mm_wlan.connect_to_network(ssid, password)

@app.get('/')
def index(request):
    return static_file(request, 'index.html')

@app.get('<path>')
def static_file(request, path):
    data = read('./public/'+path)
    type = path.split('.')[1]
    return data, {'Content-Type':mime[type]}

app.run(port=5000)