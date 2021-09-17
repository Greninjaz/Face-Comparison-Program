import face_recognition
from PIL import Image, ImageDraw

#importing all known faces. Magic code happens with the library
Jisoo = face_recognition.load_image_file('./known/Jisoo BlackPink.jpeg')
RM = face_recognition.load_image_file('./known/Rap Monster.jpeg')
Keanu = face_recognition.load_image_file('./known/Keanu Reeves.jpeg')
Mina = face_recognition.load_image_file('./known/Mina Twice.jpeg')
Tyuzu = face_recognition.load_image_file('./known/Tyuzu Twice.jpeg')
Jungkook = face_recognition.load_image_file('./known/Jungkook.jpeg')
Momo = face_recognition.load_image_file('./known/Momo Twice.jpeg')
PDP = face_recognition.load_image_file('./known/PewDiePie.jpeg')


#getting fancy numbers that help with fancy math that i dont quite understand, 
#but it works so i dont conmplain
encodedJisoo = face_recognition.face_encodings(Jisoo)[0]
encodedRM = face_recognition.face_encodings(RM)[0]
encodedKeanu = face_recognition.face_encodings(Keanu)[0]
encodedMina = face_recognition.face_encodings(Mina)[0]
encodedTyuzu = face_recognition.face_encodings(Tyuzu)[0]
encodedJK = face_recognition.face_encodings(Jungkook)[0]
encodedMomo = face_recognition.face_encodings(Momo)[0]
encodedPDP = face_recognition.face_encodings(PDP)[0]


#That one face you want to compare to the others
unknownFace = face_recognition.load_image_file('./unknown/logan_corey.jpeg')
encodedUF = face_recognition.face_encodings(unknownFace)[0]

#An array to hold all the known pictures' encodings, cause its easier this way
knownEncodings = [encodedJisoo, encodedRM,encodedKeanu,encodedMina,encodedTyuzu,
                    encodedJK,encodedMomo,encodedPDP,encodedLisa,encodedTOP]

 #An array to match names of the ppl in the known pictures. 
 #Names must match order of knownEncodiings array               
namesToFace = ["Jisoo from BlackPink",
                  "Rap Monster from BTS",
                  "Keanu Reeves",
                  "Mina from Twice",
                  "Tyuzu from Twice",
                  "Jungkook from BTS",
                  "Momo from Twice",
                  "PewDiePie"]

#An array that holds all the known file variables in order. Used for output purposes     
filesToFace = [Jisoo,RM,Keanu,Mina,Tyuzu,Jungkook,Momo,PDP]

#Used to get a number of simularity to the faces. 
faceDistances = face_recognition.face_distance(knownEncodings, encodedUF)
faceDistanceArray = []

# Find all the faces and face encodings in the unknown image
faceLocations = face_recognition.face_locations(unknownFace)
faceEncodings = face_recognition.face_encodings(unknownFace, faceLocations)

#putting all the similarity numbers and putting it into an array
for i, faceDistance in enumerate(faceDistances):
    newChallenger = "{:.4}".format(faceDistance)
    #print("The test image has a distance of {:.2} from known image {}".format(face_distance, i))
    #print("Do you look like {}: {}".format(names_to_face[i],face_distance < 0.4))
    faceDistanceArray.append(float(newChallenger))

#converting the above array
for i in range(len(faceDistanceArray)):
    newFaceValue = faceDistanceArray[i]
    #print(newFaceValue)
    newFaceValue = newFaceValue *100
    newFaceValue = int(newFaceValue)
    faceDistanceArray[i] = newFaceValue
    #print(newFaceValue)

#printing said array 
print(faceDistanceArray)

#Variables used for final comparision 
finalFace = faceDistanceArray[0]
counter = 0

#making final comparison and generating output
#Everyone starts with jisoo's number
#loops through and compares them all to find smallest value
#Smallest Value = most similar
#output the two pictures and an supportive message
for i in range(len(faceDistanceArray)):
    if finalFace > faceDistanceArray[i]:
        finalFace = faceDistanceArray[i]
        counter = i
    if i == (len(faceDistanceArray) - 1):
        print("You look like {}".format(namesToFace[counter]))
        print("")
        # Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
        notKnownFace = Image.fromarray(unknownFace)
        knownFace = Image.fromarray(filesToFace[counter])

        # Create a Pillow ImageDraw Draw instance to draw with
        draw = ImageDraw.Draw(notKnownFace)
        draw2 = ImageDraw.Draw(knownFace)

        # Remove the drawing library from memory as per the Pillow docs
        del draw
        del draw2

        # Display the resulting image
        notKnownFace.show()
        knownFace.show()




