from deepface import DeepFace
import cv2
def takepic(): 
    cap = cv2.VideoCapture(0)
    #width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    #height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    _, frame = cap.read()
    return frame
def mood_detect():
    img=takepic()
    #img=cv2.imread(r"C:\Users\praveenraj\Downloads\livetest4.jpg")
    cv2.imwrite(r"recommendationapp\static\recommendationapp\personpic.jpg",img)
    try:
      predictions=DeepFace.analyze(img,actions=['emotion'])
      predictions=predictions['emotion']
      del predictions['neutral']
      del predictions['disgust']
      print(predictions)
      temp1=0
      for i in predictions:
        if predictions[i]>temp1:
            mod1=i
            temp1=predictions[i]
      

      #print(mod1)
    except Exception:
        mod1=None
    #print(mod1,w,h)
    return mod1
