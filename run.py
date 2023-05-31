from market import app
from market.modules.admin.routes import admin
from market.modules.student.routes import student
from market.modules.teacher.routes import teacher


app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(teacher)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host = "0.0.0.0", debug=True)
