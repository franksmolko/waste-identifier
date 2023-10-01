#Organic: 0
#Recyclable: 1

import tensorflow as tf 
import numpy as np 
import cv2
import tkinter as tk
from tkinter import filedialog

model = tf.keras.models.load_model('wasteFinal.h5')


class Predict():
    def __init__(self, root):
        self.text = tk.StringVar()
        self.label = tk.Label(root, textvariable = self.text)
        self.label.configure(bg=root.cget('bg'))
        self.label.pack()



def classify_image():
    image = filedialog.askopenfilename()
    if image:
        image_read = cv2.imread(image)
        image_rgb = cv2.cvtColor(image_read, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(image_rgb, (256, 256))
        yhat = model.predict(np.expand_dims(resized/255, 0))
        estimate = np.round(yhat[0])
        print(yhat[0])
        

        if estimate ==0:
            decision = "This Waste is Organic"
        else:
            decision = "This Waste is Recyclable"
        
        predict.text.set(decision)

root = tk.Tk()

root.geometry("200x400")

root.configure(bg='forestgreen')

root.title("Wastify")

classify = tk.Button(root, text="Classify Image", command=classify_image, bg='forestgreen')

classify.place(relx=0.5, rely=0.5, anchor='center')

predict = Predict(root)

root.mainloop()

