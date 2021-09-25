#!/usr/bin/env python3

import argparse

def main():
  parser = argparse.ArgumentParser(description="Chess Engine Tester", prog="cet.py")
  parser.add_argument("Engine", action = "store", help="Path to chess engine program")
  args = parser.parse_args()
  engine_exe = args.Engine
  print(engine_exe)

if __name__ == "__main__":
  main()

# License:
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>
# or write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
