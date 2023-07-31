from market import db, models, forms


def getCourses(user):
    
    # items = db.engine.execute(f'''select c.Name, c.Grade, tc.Strength from teacher_course tc
    #                      join course c on tc.Teacher = '{user.username}' and tc.Active = 1;''')
    items = db.engine.execute(f'''select c.Course_ID, c.Name, c.Grade, tc.Strength from teacher__course tc
                         join course c on tc.Teacher = 'tr10001' and tc.Active = 1
                         and c.Course_ID = tc.Course;''')

    cols = list(items.keys())
    items = list(items)

    return items,cols