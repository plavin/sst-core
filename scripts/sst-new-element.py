#!/usr/bin/env python3

import argparse
import sys
import pathlib
import re
import os
import shutil

template_dir = pathlib.Path(os.path.dirname(os.path.realpath(__file__))) / 'templates'
if not template_dir.exists():
  print('Error: Unable to find templates/ directory')
  sys.exit(1)

def parse_args() -> argparse.Namespace:
  parser = argparse.ArgumentParser(
    description='Generate the boilerplate code for a new external element library')
  parser.add_argument('element_name', metavar='elementName', type=str, help='The name of the element library. camelCase is recommended.')
  parser.add_argument('-b', '--build_system', type=str, default='cmake',
                      choices=['cmake', 'autotools', 'make'],
                      help='The build system to use. (Default: cmake)')
  parser.add_argument('-d', '--destination', type=str, default=None,
                      help='The directory to put the new element library in. If the directory exists it must be empty. Defualt: `element_name`')
  args = parser.parse_args()

  # Validate arguments
  if not args.element_name.isidentifier():
    print('Error: `element_name` must be a valid python identifier.')
    sys.exit(1)

  if not re.search("^[a-z].*", args.element_name):
    print('Warning: It is recomended that ElementName be camelCase')

  print(type(args))
  return args


def copy_files(files: dict[pathlib.Path, pathlib.Path]) -> None:
  for src, dst in files.items():
    shutil.copyfile(src, dst)
    #print(f'move {src} to {dst}')

def replace_text_in_files(files: dict[pathlib.Path, pathlib.Path]) -> None:
  for file in files.values():
    pass
    #print(f' replace {file}')

if __name__ == "__main__":
  args = parse_args()

  build_system = args.build_system
  element_name = args.element_name
  dest_dir = pathlib.Path(args.destination if args.destination is not None else args.element_name).resolve()

  if dest_dir.exists():
    if not dest_dir.is_dir():
      print(f'Error: {dest_dir} exists and is not an empty dest_dir')
      sys.exit(1)
    if len([*dest_dir.iterdir()]) > 0:
      print(f'Error: {dest_dir} is not empty')
      sys.exit(1)

  print(f'Creating new SST element:')
  print(f'  Name: {element_name}')
  print(f'  Destination: {dest_dir}')
  print(f'  Build system: {build_system}')

  if not dest_dir.exists():
    dest_dir.mkdir()

  src_dir = template_dir / build_system

  if build_system == 'cmake':
    pass

  elif build_system == 'autotools':
    pass

  elif build_system == 'make':

    files = {
      src_dir / 'LICENSE'     : dest_dir / 'LICENSE',
      src_dir / 'template.h'  : dest_dir / f'{element_name}.h',
      src_dir / 'template.cc' : dest_dir / f'{element_name}.cc',
    }

  else:
    print('Error: Unknown build system')
    sys.exit(1)

  for f1, f2 in files.items():
    print(type(f1))
  copy_files(files)
  replace_text_in_files(files)


