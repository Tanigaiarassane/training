
from app import app
from app.models import ActivityItem
from app import db
from flask import render_template,flash, redirect, url_for,request
from app.forms import ToDO


@app.route("/")
def base():
    return render_template("base.html")

@app.route("/sample")
def sample():
    return render_template("sample.html", greetings="Hello sir", title="Sample")

@app.route("/todo/list")
def listing():
    todo = ActivityItem.query.all()
    return render_template("listing.html", todo=todo, title="Item litem")

@app.route("/todo/create", methods = ['GET', 'POST'])
def create():
    form = ToDO()
    if form.validate_on_submit():
        print "welcome"
        print "Submitted values - {} -  {} - {}".format(form.name.data, form.content.data, form.status.data)
        activity = ActivityItem(form.name.data, form.content.data,form.status.data)
        db.session.add(activity)
        db.session.commit()
        message = "Successfully created an activity - {}".format(activity.name)
        flash(message, "success")
        return redirect( url_for('item', item_id=activity.id) )
    print "outside"
    return render_template("create.html",  message="Create item", form=form)

@app.route("/todo/item/<int:item_id>", methods = ["POST","GET"])
def item(item_id):
    print item_id
    todo = ActivityItem.query.get_or_404(item_id)
    return render_template('list.html', todo = todo)

@app.route("/todo/<int:todo_id>/update", methods = ["POST","GET"])
def update(todo_id):
    todo = ActivityItem.query.get_or_404(todo_id)
    form = ToDO()
    print todo
    if form.validate_on_submit():
        todo.name = form.name.data
        todo.content = form.content.data
        todo.status = form.status.data
        db.session.commit()
        message = "Successfully updated activity to- {}".format(todo.name)
        flash(message,"success")

        return redirect(url_for('listing'))
    elif request.method == "GET":
        form.name.data = todo.name
        form.content.data = todo.content
        form.status.data = todo.status
    return render_template("create.html",  message="Update item", form=form)


@app.route("/todo/<int:todo_id>/delete", methods = ["POST","GET"])
def delete(todo_id):
    todo = ActivityItem.query.get_or_404(todo_id)
    message = "Successfully deleted activity - {}".format(todo.name)
    db.session.delete(todo)
    db.session.commit()
    flash(message, "success")
    return redirect(url_for('listing'))


