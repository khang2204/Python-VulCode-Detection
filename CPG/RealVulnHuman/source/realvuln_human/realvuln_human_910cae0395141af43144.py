f = request.files['file']
        rand = random.randint(1, 100)
        fname = secure_filename(f.filename)
        fname = str(rand) + fname  # change file name
        cwd = os.getcwd()
        file_path = cwd + '/Files/' + fname
        f.save(file_path)  # save file locally

        # Access saved file
        document = Document(file_path)
        for para in document.paragraphs:
            print (para.text)  # '\n\n'.join([para.text for paragraph in document.paragraphs])

    # return "file uploaded successfully"
    return render_template('view.html', name=para.text)

@app.route("/yaml")
def yaml_upload():
    return render_template(
        'yaml_test.html')
