from tokenize import String
 
class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(this, name, age, tracks, score):
        this.name = str(name)
        this.age = int(age)
        this.tracks = tracks
        this.score = float(score)
    
    def change_name(this, new_name):
        if type(new_name) != str:
            return "name must be string"
        this.name = str(new_name)
 
    def change_age(this, new_age):
        if type(new_age != int):
            return "age must be an integer"
        this.age = int(new_age)
    
    def add_track(this, new_track):
        if (type(new_track) != str):
            return "track must be a string"
        this.tracks.append(new_track)
 
    def get_score(this):
        return this.score
 
 
 
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
 
# Expected methods
Bob.change_name("Michael")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()