from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from django.http import StreamingHttpResponse
from camera import VideoCamera
from .models  import  Camera
from .form   import CameraForm
from django.http import Http404

# Create your views here.
#def index(request):
    #return HttpResponse("<h1>Welcome to Django Rithisak</h1>")

def insertCamera(request):
	#locations = Location.objects.all()
	context = {}
	if request.method == "POST":
		ip = request.POST['ip']
		name = request.POST['name']

		auth_uname = request.POST['auth_uname']
		auth_pwd   = request.POST['auth_pwd']
		camObj = Camera.objects.create(
									ip=ip,
									name=name,
									auth_uname = auth_uname,
									auth_pwd = auth_pwd,
								)
		camObj.save()


		return redirect('/preview')

	else:
		print("not post")
		#CameraLists = Camera.objects.filter(location__pk = request.POST.get('location'))
		#context.update({'CameraLists' : CameraLists,'Camname':Camname,'locations' : locations})
		#return render (request,"Index/cameralocation.html",context)
	#locations = Location.objects.all()
	#context.update({'locations' : locations})
	return render (request,"addCamera/insertCamera.html",context)

def index(request):
	return render (request,"addCamera/index.html")

def previewCamera(request):

	camObjs = Camera.objects.all()
	context = {
	  'camObjs' : camObjs
	}
	return render (request, "addCamera/previewCamera.html", context)

def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
					b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_streamer(request ,camPK):
	camObj = Camera.objects.get(pk=camPK)
	camIP = "rtsp://%s:%s@%s/" %(camObj.auth_uname, camObj.auth_pwd, camObj.ip)
	repsone = gen(VideoCamera(camIP))
	return  StreamingHttpResponse(repsone,content_type='multipart/x-mixed-replace; boundary=frame')
