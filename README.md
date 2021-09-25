# Chess Engine Tester
A program to test your chess engine using the UCI protocol

## Usage
cet.py <path/to/your/chess-engine>

## Prerequisites
Python3 (latest version as of time of writing 3.9.3)

## Missing features
- UCI protocol tests
- Ability to run single test
- Ability to run test suites
- Config file, in addition to command line args
- xboard/WinBoard protocol tests

## Chess engine requirements
The chess engine must make sure to flush its output to stdout after each response
otherwise cet.py will be hanging waiting for a response.

## License
This program is free software published under GPLv2 See LICENSE file
