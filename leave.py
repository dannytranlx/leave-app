import time
import argparse

class LeaveApp():
	def __init__(self):
		self.argparse = self.build_argparser()

	def run(self):
		args = self.argparse.parse_args()
		args.func(args)

	def build_argparser(self):
		parser = argparse.ArgumentParser(description = "LeaveApp application")
		subparsers = parser.add_subparsers(help = "Help")

		# when command
		parser_list = subparsers.add_parser('when', help='Gives the time when you can leave')
		parser_list.add_argument('time_in', action="store", type=str, help='Time you checked in')
		parser_list.add_argument('lunch_time', action="store", default="0.50", nargs="?", type=str, help='Time you are sprending for lunch')
		parser_list.add_argument('time_work', action="store", default="8", nargs="?", type=str, help='Time you need to do in a day')
		parser_list.set_defaults(func=self.command_when)

		# leave command
		parser_list = subparsers.add_parser('leave', help='Gives the time when you need to come in to leave at the desired time')
		parser_list.add_argument('time_out', action="store", type=str, help='Time you want to leave')
		parser_list.add_argument('lunch_time', action="store", default="0.50", nargs="?", type=str, help='Time you are sprending for lunch')
		parser_list.add_argument('time_work', action="store", default="8", nargs="?", type=str, help='Time you need to do in a day')
		parser_list.set_defaults(func=self.command_leave)

		return parser

	def command_when(self, args):
		self.when_can_i_leave(args.time_in, args.lunch_time, args.time_work)

	def command_leave(self, args):
		self.i_want_to_leave_at(args.time_out, args.lunch_time, args.time_work)

	def when_can_i_leave(self, time_in, lunch_time, time_work):
		time_in = TimeParser().parse_time(time_in)
		lunch_time = TimeParser().time_to_sec(lunch_time)
		time_work = TimeParser().time_to_sec(time_work)

		time_in = time_in + lunch_time + time_work

		print 'You may leave at ' + time.strftime("%H:%M",time.localtime(time_in)) + '!'

	def i_want_to_leave_at(self, time_out, lunch_time, time_work):
		time_out = TimeParser().parse_time(time_out)
		lunch_time = TimeParser().time_to_sec(lunch_time)
		time_work = TimeParser().time_to_sec(time_work)

		time_in = time_out - lunch_time - time_work
		time_in = time.strftime("%H:%M",time.localtime(time_in))

		print 'You must check in at ' + time_in + '!'

class TimeParser():
	def parse_time(self, p_time):
		p_time = time.strptime('2013' + p_time, '%Y%H%M') # Added the year since there's some fuckup with the epoch date
		return time.mktime(p_time)

	def time_to_sec(self, p_time):
		return float(p_time) * 60 * 60

if __name__ == "__main__":
	LeaveApp().run()
