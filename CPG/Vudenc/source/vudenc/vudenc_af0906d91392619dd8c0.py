def doSettings(self, afterSubmit):...
htmlSettingsForm = settingsToHtmlForm()
settingsFilename = settings.getSettingsFilename()
self.write(
    """<html>
                            <head>
                                  <link rel="stylesheet" type="text/css" href="webInterface/settings.css">
                                  <script type="text/javascript" src="webInterface/settings.js"></script>
                            </head>
                            <body>
                                  <h1>Liked Saved Downloader Settings</h1>
                                  <a href="/">Back to Homepage</a><br /><br />
                                  {}
                                  <p>Settings being read from {}</p>
                                  <form action="/settings" method="post">
                                       <input type="submit" value="Submit">
                                       {}
                                       <input type="submit" value="Submit">
                                  </form>
                            </body>
                      </html>"""
    .format('<p><b>Settings updated</b></p>' if afterSubmit else '',
    settingsFilename, htmlSettingsForm))
