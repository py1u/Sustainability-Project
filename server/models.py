from app import db

class Course(db.Model):
    
    # relation named course
    __tablename__ = 'course'
    
    
    # 6 primary columns from 2021-2024 course catalogue
    cid = db.Column(db.String, nullable=False , primary_key=True)
    level = db.Column(db.String, nullable=False)
    college = db.Column(db.Text, nullable=False)
    
    dept = db.Column(db.Text, nullable=False)
    course_title = db.Column(db.String, nullable=False)
    course_desc = db.Column(db.Text, nullable=False, index=True)
    
    #unique 
    sgd = db.Column(db.String)
    
    
    # get a list for the sdgs
    
    def sgd_list(self):
        if self.sgd:
            return list(map(int, self.sgd.split(',')))
        return []
    
    
    def __repr__(self):
        return f'course id: {self.cid}'