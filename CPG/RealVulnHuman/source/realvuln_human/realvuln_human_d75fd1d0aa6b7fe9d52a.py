<p><input type = 'submit' value = 'Submit'/></p>
         </form>
      %s
      </body>
      <a href="dashboard">Go back</a>
   </html>
   """ %(name)
   return render_template_string(template)

if __name__ == "__main__":
    app.debug = True
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=8000)
