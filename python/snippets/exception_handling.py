#!/usr/bin/env python
import os

"""
This file contains the sample code for XXX.  Search for the string CONTENT to
skip directly to it.

Executing this file will begin an enhanced interactive Python session.  You
can step through each slide of sample code and explore the results.  If your
explorations hose the environment, just quit, restart and jump directly to the
slide where you left off.

The block of code below sets up the interactive session.  Skip over it to view
the sample code.
"""

##############################################################################
#
# sliderepl - 0.12
#   Copyright (c) Jason Kirtland <jek@discorporate.us>
#   sliderepl lives at http://discorporate.us/projects/sliderepl
#   sliderepl is licensed under the MIT License:
#   http://www.opensource.org/licenses/mit-license.php
#
# sliderepl may be textually included in a file that also contains its input
# data.  The input data may be under a different license. sliderepl's MIT
# License covers only this block of sliderepl code, extensions and other
# derivative works.
#
# Looking for the sample code?
#                        _ _       _
#     ___  ___ _ __ ___ | | |   __| | _____      ___ __
#    / __|/ __| '__/ _ \| | |  / _` |/ _ \ \ /\ / / '_ \
#    \__ \ (__| | | (_) | | | | (_| | (_) \ V  V /| | | |
#    |___/\___|_|  \___/|_|_|  \__,_|\___/ \_/\_/ |_| |_|
#
# This bootstrapping code loads the sample code below into an interactive
# Python session.

environ = globals().copy()
import code, inspect, itertools, logging, re, sys, traceback
try:
    import rlcompleter, readline
except ImportError:
    readline = None


class Deck(object):
    expose = ('commands', 'next', 'goto', 'show', 'info', 'quick')

    def __init__(self, path=None):
        self.path = path or '<no file>'
        self.slides = []
        self.current = 0
        self.enter_advances = False

    def start(self):
        pass

    def next(self):
        """Advance to the next slide."""
        os.system('clear')
        if self.current >= len(self.slides):
            print "% The slideshow is over."
            return
        slide = self.slides[self.current]
        self.current += 1
        print "%%\n%% Running slide %s\n%%" % (self.current)
        if (slide.name and
            not (slide.name.isdigit() and int(slide.name) == self.current)):
            print "%% %s" % slide.name
        slide.run()

    def slide_actor(fn):
        def decorated(self, slide_number):
            if isinstance(slide_number, str) and not slide_number.isdigit():
                print "%% Usage: %s slide_number" % fn.__name__
                return
            num = int(slide_number)
            if num < 1 or num > len(self.slides):
                print "%% Slide #%s is out of range (1 - %s)." % (
                    num, len(self.slides))
            else:
                return fn(self, num)
        decorated.__doc__ = fn.__doc__
        return decorated

    def show(self, slide_number):
        """show NUM, display a slide without executing it."""
        print str(self.slides[slide_number - 1]).strip()
    show = slide_actor(show)

    def goto(self, slide_number):
        """goto NUM, skip forward to another slide."""
        if slide_number <= self.current:
            print "% Cowardly refusing to re-run slides."
        else:
            for _ in range(slide_number - self.current):
                self.next()
    goto = slide_actor(goto)

    def info(self):
        """Display information about this slide deck."""
        print "%% Now at slide %s of %s from deck %s" % (
            self.current, len(self.slides), self.path)

    def commands(self):
        """Display this help message."""
        for cmd in self.expose:
            print "% " + cmd
            print "%\t" + getattr(self, cmd).__doc__


    def quick(self, toggle):
        """quick on|off, type enter to advance to the next slide."""
        if toggle not in ('on', 'off'):
            print 'usage: quick on|off'
        else:
            self.enter_advances = (toggle == 'on')
            print "%% Quick mode %s (enter will advance to the next slide)" % (
                toggle)
    del slide_actor

    class Slide(object):
        def __init__(self, name=None):
            self.name = name
            self.codeblocks = []
            self.lines = []
            self._stack = []
            self._level = None
        def run(self):
            for display, co in self.codeblocks:
                if not getattr(self, 'no_echo', False):
                    shown = [getattr(sys, 'ps1', '>>> ') + display[0]]
                    shown.extend([getattr(sys, 'ps2', '... ') + l
                                          for l in display[1:]])
                    Deck._add_history(''.join(display).rstrip())
                    print ''.join(shown).rstrip()
                try:
                    exec co in environ
                except:
                    traceback.print_exc()
        def __str__(self):
            return ''.join(self.lines)
        def _append(self, line):
            self.lines.append(line)
            if not self._stack and line.isspace():
                return
            indent = len(line) - len(line.lstrip())
            if not self._stack:
                self._level = indent
            elif indent <= self._level:
                try:
                    co = self._compile()
                    if co:
                        self.codeblocks.append((self._pop(), co))
                except SyntaxError:
                    pass
            self._stack.append(line)
        def _close(self):
            if self._stack:
                co = self._compile()
                assert co
                self.codeblocks.append((self._pop(), co))
        def _compile(self):
            style = getattr(self, 'no_return', False) and 'exec' or 'single'
            return code.compile_command(''.join(self._stack), '<input>', style)
        def _pop(self):
            self._stack.reverse()
            lines = list(itertools.dropwhile(str.isspace, self._stack))
            lines.reverse()
            self._stack = []
            return lines

    def run(cls, path=None):
        """Run an interactive session for this Deck and exit when complete.

        If '
         is first on the command line, all slides are executed
        immediately and the script will exit.  Useful for sanity testing.
        """
        if path is None:
            path = sys.argv[0]
        deck = cls.from_path(path)
        if not deck:
            sys.stderr.write("Aborting: no slides!\n")
            sys.exit(-1)

        deck.start()

        if sys.argv[1:] and sys.argv[1] == '--run-all':
            deck.goto(len(deck.slides))
            sys.exit(0)

        console = code.InteractiveConsole()
        global environ
        environ = console.locals
        console.raw_input = deck.readfunc
        if readline:
            readline.parse_and_bind('tab: complete')
            readline.set_completer(rlcompleter.Completer(environ).complete)
        console.interact(deck.banner)
        sys.exit(0)
    run = classmethod(run)

    def from_path(cls, path):
        """Create a Deck from slides embedded in a file at path."""
        sl_re = re.compile(r'### +slide::\s*')
        a_re = re.compile(r',\s*')

        fh, deck, slide = open(path), cls(path), None
        for line in fh:
            if not sl_re.match(line):
                if slide:
                    slide._append(line)
                continue
            if slide:
                slide._close()
                deck.slides.append(slide)
            metadata = sl_re.split(line, 2)[1].split('-*-', 2)
            name = metadata[0].strip()
            if name == 'end':
                break
            slide = cls.Slide(name=name or None)
            if len(metadata) >= 2:
                for option in (metadata[1] and a_re.split(metadata[1]) or []):
                    setattr(slide, option.strip(), True)
        fh.close()
        return deck.slides and deck or None
    from_path = classmethod(from_path)

    def banner(self):
        return """\
%% This is an interactive Python prompt.
%% Extra commands: %s
%% Type "next" to start the presentation.""" % ', '.join(self.expose)
    banner = property(banner)

    def readfunc(self, prompt=''):
        line = raw_input(prompt)
        if prompt == getattr(sys, 'ps1', '>>> '):
            tokens = line.split()
            if line == '' and self.enter_advances:
                tokens = ('next',)
            if tokens and tokens[0] in self.expose:
                fn = getattr(self, tokens[0])
                if len(tokens) != len(inspect.getargspec(fn)[0]):
                    print "usage: %s %s" % (
                        tokens[0], ' '.join(inspect.getargspec(fn)[0][1:]))
                else:
                    self._add_history(line)
                    fn(*tokens[1:])
                return ''
        return line

    def _add_history(cls, line):
        if readline and line:
            readline.add_history(line)
    _add_history = classmethod(_add_history)

#  end of sliderepl
#
##############################################################################

Deck.run()

#        ____ ___  _   _ _____ _____ _   _ _____ _
#       / ___/ _ \| \ | |_   _| ____| \ | |_   _| |
#      | |  | | | |  \| | | | |  _| |  \| | | | | |
#      | |__| |_| | |\  | | | | |___| |\  | | | |_|
#       \____\___/|_| \_| |_| |_____|_| \_| |_| (_)
#
# Slide CONTENT starts here.

### slide:: 1 -*- no_echo -*-

print """\
###########Exception Handling #############################

   1. Purpose of Exception Handling
   2. Construct - Try, Except handlers, else, finally
   3. User defined exception

#############################################################
"""

### slide:: 2 -*- no_echo -*-

print """\
#############################################################

What is an exception?
Exceptions are error conditions that occur during run time.The program will be syntactically correct. But while executing the program we might encounter these errors. When these errors occur, the program aborts abruptly

################################################################
"""

### slide::3
# -- Slie 2/10 ---
0/1
1/0

### slide:: -*- no_echo -*-

print """\
The purpose of exception handling is to handle these errors gracefully
and let the program to take appropriate action based on the error conditions
"""

### slide:: -*- no_echo -*-
print """\
Syntax of exception hanling in Python

 try:
    Block statement
 except <exception>:
    Action when an exception occur
 else:
    Action when there is no Exception
"""

### slide::
try:
   1/0
except ZeroDivisionError:
   print "Encountered Division by zero"

### slide::
try:
    f = open("sample.txt")
    print f.read()
    f.close()
except IOError:
    print "File does not exist"

### slide:: -*- no_echo -*-
print """\
Handling multiple exceptions

A single try block can have multiple exception handlers. The syntax is

try:
  Try block
except <typeA>:
  handler typeA
except <typeB>:
  handler tryeB
.....
else:
  This block will be executed if there is no exception
"""

### slide::-*- no_echo -*-

print """\
try:
    input_val = raw_input("Provide a number")
    input_val2 = raw_input("Provide a divisor")
    result = int(input_val)/int(input_val2)
except ValueError:
    print "Only numbers are allowed"
except ZeroDivisionError:
    print "Division by zero not allowed"
else:
    print "Result is {}".format(result)
"""

### slide:: end
