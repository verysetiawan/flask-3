from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config ["SECRET_KEY"] = "IniSecretKeyKu2020"

#membuat route untuk halaman /index dengan nama fungsi (def) indexku
@app.route("/index")
def indexku():
    #menambahkan nilai/variabel 
    nilaiku = 100
    #menambahkan looping
    hari = ("senin","selasa","rabu","kamis","jumat","sabtu","minggu")
    #conditioning if else
    statushari = "minggu" #jika hari adalah minggu maka libur, selainya kerja
    return render_template ("index.html", var1=nilaiku, var2=hari, var3=statushari)

#membuat route untuk halaman /about dengan nama fungsi (def) about
@app.route("/about")
def about():
    return render_template ("about.html")

#membuat route untuk halaman /contact dengan nama fungsi (def) contact
@app.route("/contact")
def contact():
    return render_template ("contact.html")

#membuat route untuk halaman /main dengan nama fungsi (def) mainlay
@app.route("/main")
def mainlay():
    return render_template ("main_layout.html")

#MATERI PARSING DI FLASK
#parsing nilai integer
@app.route("/parsingint/<int:nilaiku2>")
def parsint(nilaiku2):
    return f"nilainya integer adalah : {nilaiku2}"

#parsing nilai string
@app.route("/parsingstr/<string:nilaiku>")
def parsstr(nilaiku):
    return f"isinya string adalah : {nilaiku}"

#argument parser
@app.route("/parsarg")
def parsarg():
    data = request.args.get("nilai")
    return f"isi dari argument parser adalah {data}" 

#memparsing nilai untu diset di sesion url
@app.route ("/halaman/<int:nilaiku>")
def session_1 (nilaiku):
    session["nilai"] = nilaiku
    return "Data yang dinputkan berhasil"

#menampilkan parsing ke halaman view
@app.route ("/halaman/view")
def view_session_1 ():
    data = session["nilai"]
    return f"nilai sesion adalah {data}"

#logout / destroy session
@app.route ("/halaman/logout")
def logout_session_1 ():
    session.pop ("nilai")
    return "Berhasil Logout"


    
if __name__ == "__main__":
    app.run (debug=True)