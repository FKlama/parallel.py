#!/usr/bin/python
# vim:set ts=2 sw=2 et:
import os, re, string
import subprocess
import argparse

from multiprocessing import Pool, cpu_count


def executeCommands(command):
  subprocess.call(command, shell=True)

if __name__ == "__main__":  
  defaultThreads = cpu_count()

  argParser = argparse.ArgumentParser(description="Parallel execution of shell commands")
  argParser.add_argument('--command', '-c', help="Command to execute, by default %%var%% is replaced")
  argParser.add_argument('--threads', '-n', type=int, default=defaultThreads, 
      help="Number of threads to use [%i]"%defaultThreads)
  argParser.add_argument('variables', nargs="+", help="Whatever should go into %%var%%")

  args = vars(argParser.parse_args())

  p = Pool(args['threads'])


  commands = []
  for v in args['variables']:
    command = args['command']
    command = re.sub(args['variable'], v, command)
    commands.append(command)


  p.map(executeCommands, commands)
