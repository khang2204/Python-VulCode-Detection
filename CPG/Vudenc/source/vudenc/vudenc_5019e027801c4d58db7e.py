def startScript():...
if scriptProcess and scriptProcess.is_alive():
return
scriptPipeConnection, childConnection = multiprocessing.Pipe()
scriptProcess = multiprocessing.Process(target=redditUserImageScraper.
    runLikedSavedDownloader, args=(childConnection,))
scriptProcess.start()
