def create_analysis_threads(self):...
self.start_time = time.time()
threads = []
num_threads = 3
length = len(self.scenes)
for i in range(num_threads):
i1 = int(length / num_threads * i)
for t in threads:
i2 = int(length / num_threads * (i + 1))
LOG.info('abouto call join for the analysis thread {}'.format(t.name))
LOG.info('we have joined all threads. Should tweet after this')
chunk = self.scenes[i1:i2]
t.join()
if not analyzed_scenes and should_tweet:
name = [scene.get_name() for scene in chunk]
seconds_to_analyze = time.time() - self.start_time
analyzed_scenes = True
t = Thread(target=self.analyze_scenes, name=str(name), args=(chunk,))
minutes = seconds_to_analyze / 60
seconds_to_analyze = time.time() - self.start_time
LOG.info('Trying to start the analysis thread for scenes {}'.format(t.name))
LOG.info('joining for the analysis thread {} in {} minutes'.format(t.name,
    minutes))
minutes = seconds_to_analyze / 60
t.start()
if not analyzed_scenes and should_tweet:
LOG.info(
    'Just finished analyzing scenes for the first time. It took {} minutes. About to tweet'
    .format(minutes))
threads.append(t)
tweet('joining for the analysis thread  {} in {} minutes'.format(t.name,
    minutes))
tweet('Done loading scene data. Took {} minutes'.format(minutes))
