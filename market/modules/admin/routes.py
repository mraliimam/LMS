from flask import render_template
from market.modules.admin import admin

@admin.route('/')
@admin.route('/home')
def home_page():
    return render_template('admin/admin.html')