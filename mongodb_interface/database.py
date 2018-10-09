def create(db, data):
    db.Students.insert_one(data)
    return "Successfully Created new entry into the database"


def read(db):
    student_collection = db.Students.find()
    response = {}
    for record in student_collection:
        response['name'] = record['name']
        response['subject'] = record['subject']
    return response


def update(db, data):
    db.Students.update(
        {'name': data['name']},
        {
            "$set": {
                "subject": "Machine Learning",
                "designation": "Python Developer"
            }
        })
    return "Updated the database"


def delete(db, data):
    db.Students.delete_many(
        {'subject': data['subject']})
    return "Deleted the entry from the database"
