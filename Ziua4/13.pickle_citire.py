import pickle
from student import Student

with open("student.pkl", "rb") as file_reader:
    obiect:Student = pickle.load(file_reader)


print(obiect)

obiect.invata()

