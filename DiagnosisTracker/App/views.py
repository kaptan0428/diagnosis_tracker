from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from .models import Post
import pyrebase
from django.contrib import messages

# def index(request):
#     return render(request, 'App/index.html')
config = {

}

def about(request):
    return render(request, 'App/about.html')


def services(request):
    return render(request, 'App/request.html')


# def contact(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         contact = Contact(email=email, message=message, date=datetime.today())
#         contact.save()
#     return render(request, 'App/contact.html')


def index(request):
    return render(request, 'App/index.html')


def signup(request):
    return render(request, 'App/signup.html')


def welcome(request):
    from os import path
    import cv2
    email = request.GET.get('Email', 'default')
    s = str(email)
    index = s.index('@')
    s = s[0:index]
    a = ".jpg"
    f = s+a
    print(f)
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    font = cv2.FONT_HERSHEY_SIMPLEX
    video_capture = cv2.VideoCapture(0)
    name = "jello"
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    location = path.join(PROJECT_ROOT, 'static/App/Training_images')
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(200, 200),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        if faces is not 0:
            cv2.imwrite(path.join(location, f), frame)
        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            cv2.putText(frame, 'Press Q to Capture', (x, y), font, 2, (255, 0, 0), 5)
        # cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)
        # Display the resulting frame
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

    # email = request.GET.get('Email', 'default')
    params = {'email': email ,'f':f , 's':s}
    print(email)

    return render(request, 'App/welcome.html',params)

def main(request):
    from typing import Set
    import cv2
    import numpy as np
    import face_recognition
    import os
    from datetime import datetime
    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(PROJECT_ROOT, 'static/App/Training_images')
    # path2 =os.path.join(PROJECT_ROOT, 'Attendance.csv')
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)

    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    def markAttendance(name):
        with open('Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    name = None
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            matchIndex = np.argmin(faceDis)
            if matches[matchIndex]:
                name = classNames[matchIndex]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
                if markAttendance(name) != None:
                    break

        if name is None :
            message = "Face not Recognised"
            return render(request,'App/index.html',{"messg":message})


        print(name)

        cv2.imshow('Webcam', img)

        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        # cv2.destroyAllWindows()
        # cv2.imshow('Webcam', img)
        # cv2.waitKey(1)
        # cv2.destroyAllWindows()

        # for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        #     matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        #     faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #     matchIndex = np.argmin(faceDis)
        #     if matches[matchIndex]:
        #         name = classNames[matchIndex].upper()
        #     else:
        #         name = "NOTFOUND"

        # if name is None :
        #     message = "Face not Recognised"
        #     return render(request,'App/signin.html',{"messg":message})
        #
        details = Post.objects.all()
        print(details)
        n = len(details)
        b = ".jpg"
        img = name+b
        print(img)
        params = {'name': name,'detail':details,'img':img}
        # params = {'name': name}
        # print(name)


    return render(request, 'App/main.html',params)

def logout(request):
    return render(request,'App/index.html')

def data(request):
    email = request.GET.get('Email', 'default')
    s = str(email)
    # index = s.index('.')
    # s = s[0:index]
    params = {'s':s}
    return render(request, 'App/data.html',params)


def createpost(request):
    if request.method == 'POST':
        # if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('usrname'):
        post = Post()
        post.usrname = request.POST.get('usrname')
        post.fname = request.POST.get('fname')
        post.lname = request.POST.get('lname')
        post.bgrp = request.POST.get('bgrp')
        post.age = request.POST.get('age')
        post.wt = request.POST.get('wt')
        post.ht = request.POST.get('ht')
        post.txta = request.POST.get('txta')
        post.que1 = request.POST.get('que1')
        post.que2 = request.POST.get('que2')
        post.que3 = request.POST.get('que3')
        post.que4 = request.POST.get('que4')
        post.que5 = request.POST.get('que5')
        post.que6 = request.POST.get('que6')
        post.que7 = request.POST.get('que7')
        post.que8 = request.POST.get('que8')
        post.que9 = request.POST.get('que9')
        post.que10 = request.POST.get('que10')
        post.que11 = request.POST.get('que11')
        post.que12 = request.POST.get('que12')
        post.que13 = request.POST.get('que13')
        post.que14 = request.POST.get('que14')
        post.que15 = request.POST.get('que15')
        post.que16 = request.POST.get('que16')
        post.que17 = request.POST.get('que17')
        post.que18 = request.POST.get('que18')
        post.que19 = request.POST.get('que19')
        post.que20 = request.POST.get('que20')
        post.que21 = request.POST.get('que21')
        post.que22 = request.POST.get('que22')
        post.que23 = request.POST.get('que23')
        post.que24 = request.POST.get('que24')
        post.que25 = request.POST.get('que25')
        post.que26 = request.POST.get('que26')
        post.que27 = request.POST.get('que27')
        post.que28 = request.POST.get('que28')
        post.que29 = request.POST.get('que29')
        post.que30 = request.POST.get('que30')
        post.que31 = request.POST.get('que31')
        post.que32 = request.POST.get('que32')
        post.que33 = request.POST.get('que33')
        post.que34 = request.POST.get('que34')
        post.que35 = request.POST.get('que35')
        post.que36 = request.POST.get('que36')
        post.que37 = request.POST.get('que37')
        post.que38 = request.POST.get('que38')
        post.que39 = request.POST.get('que39')
        post.que40 = request.POST.get('que40')
        post.que41 = request.POST.get('que41')
        post.que42 = request.POST.get('que42')
        post.que43 = request.POST.get('que43')
        post.que44 = request.POST.get('que44')
        post.que45 = request.POST.get('que45')
        post.que46 = request.POST.get('que46')

        post.save()

        return render(request, 'App/success.html')

def about(request):
    return render(request, 'App/about.html')
    # else:
    #     return render(request, 'App/index.html')