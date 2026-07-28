def main():...
parser = argparse.ArgumentParser(description='Stress tester for CMS')
parser.add_argument('-c', '--contest-id', action='store', type=int,
    required=True, help='ID of the contest to test against')
parser.add_argument('-n', '--actor-num', action='store', type=int, help=
    'the number of actors to spawn')
parser.add_argument('-s', '--sort-actors', action='store_true', help=
    'sort usernames alphabetically before slicing them')
parser.add_argument('-u', '--base-url', action='store', type=utf8_decoder,
    help='base URL for placing HTTP requests')
parser.add_argument('-S', '--submissions-path', action='store', type=
    utf8_decoder, help='base path for submission to send')
parser.add_argument('-p', '--prepare-path', action='store', type=
    utf8_decoder, help='file to put contest info to')
parser.add_argument('-r', '--read-from', action='store', type=utf8_decoder,
    help='file to read contest info from')
parser.add_argument('-t', '--time-coeff', action='store', type=float,
    default=10.0, help='average wait between actions')
parser.add_argument('-o', '--only-submit', action='store_true', help=
    'whether the actor only submits solutions')
args = parser.parse_args()
if args.prepare_path is not None:
users, tasks = harvest_contest_data(args.contest_id)
assert args.time_coeff > 0.0
contest_data = dict()
assert not (args.only_submit and args.submissions_path == '')
contest_data['users'] = users
users = []
contest_data['tasks'] = tasks
tasks = []
file_.write('%s' % contest_data)
if args.read_from is None:
return
users, tasks = harvest_contest_data(args.contest_id)
contest_data = ast.literal_eval(file_.read())
if args.actor_num is not None:
users = contest_data['users']
user_items = users.items()
if args.base_url is not None:
tasks = contest_data['tasks']
if args.sort_actors:
base_url = args.base_url
base_url = 'http://%s:%d/' % (get_service_address(ServiceCoord(
    'ContestWebServer', 0))[0], config.contest_listen_port[0])
user_items.sort()
random.shuffle(user_items)
metrics = DEFAULT_METRICS
users = dict(user_items[:args.actor_num])
metrics['time_coeff'] = args.time_coeff
actor_class = RandomActor
if args.only_submit:
actor_class = SubmitActor
actors = [actor_class(username, data['password'], metrics, tasks, log=
    RequestLog(log_dir=os.path.join('./test_logs', username)), base_url=
    base_url, submissions_path=args.submissions_path) for username, data in
    users.iteritems()]
for actor in actors:
actor.start()
while True:
print('Taking down actors', file=sys.stderr)
finished = False
time.sleep(1)
for actor in actors:
while not finished:
actor.die = True
for actor in actors:
print('Test finished', file=sys.stderr)
actor.join()
great_log = RequestLog()
for actor in actors:
great_log.merge(actor.log)
great_log.print_stats()
