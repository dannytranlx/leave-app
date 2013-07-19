import sys
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
		parser_list.add_argument('time_in', action="store", nargs="?", type=str, help='Time you checked in')
		parser_list.add_argument('lunch_time', action="store", default="30", nargs="?", type=str, help='Time you are sprending for lunch')
		parser_list.add_argument('time_work', action="store", default="7", nargs="?", type=str, help='Time you need to do in a day')
		parser_list.set_defaults(func=self.command_when)

		return parser

	def command_when(self, args):
		print args.time_in, args.lunch_time, args.time_work



if __name__ == "__main__":
	LeaveApp().run()