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
  parser.add_argument('-e', '--element_name', type=str, default='myElement',
                      help='The name of the element library. camelCase is recommended. Default: myElement')
  parser.add_argument('-c', '--component_name', type=str, default='MyComponent',
                      help='The name of the component in the library. PascalCase is recommended. Default: MyComponent')

  parser.add_argument('-b', '--build_system', type=str, default='cmake',
                      choices=['cmake', 'autotools', 'make'],
                      help='The build system to use. (Default: cmake)')
  parser.add_argument('-d', '--destination', type=str, default=None,
                      help='The directory to put the new element library in. Must not exist.  Defualt: `element_name`')

  args = parser.parse_args()

  # Validate arguments
  if not args.element_name.isidentifier():
    print('Error: `element_name` must be a valid python identifier.')
    sys.exit(1)

  if not args.component_name.isidentifier():
    print('Error: `element_name` must be a valid python identifier.')
    sys.exit(1)

  if not re.search("^[a-z].*", args.element_name):
    print('Warning: It is recomended that element_name be camelCase')

  if not re.search("^[A-Z].*", args.component_name):
    print('Warning: It is recomended that component_name be PascalCase')

  return args

def replace_text(filename: pathlib.Path, element_name: str, component_name: str) -> None:
  with open(filename, 'r') as file:
    filedata = file.read()

  # Replace template strings
  filedata = filedata.replace('{{ELEMENT_NAME}}', element_name)
  filedata = filedata.replace('{{COMPONENT_NAME}}', component_name)
  filedata = filedata.replace('{{ELEMENT_NAME_ALLCAPS}}', element_name.upper())

  # Remove Sandia copyright
  lines = filedata.splitlines()

  end_comment = 0
  stripped_lines = []
  for idx, line in enumerate(lines):
      if not (line.startswith('//') or line.strip() == ''):
        end_comment = idx
        break

  filedata = '\n'.join(lines[end_comment:])

  with open(filename, 'w') as file:
      file.write(filedata)

if __name__ == "__main__":
  args = parse_args()

  build_system = args.build_system
  dest_dir = pathlib.Path(args.destination if args.destination is not None else args.element_name).resolve()

  if dest_dir.exists():
    print(f'Error: {dest_dir} already exists')
    sys.exit(1)

  print(f'Creating new SST element:')
  print(f'  Element library: {args.element_name}')
  print(f'  Component: {args.component_name}')
  print(f'  Destination: {dest_dir}')
  print(f'  Build system: {build_system}')

  shutil.copytree(template_dir/build_system, dest_dir)

  for file in dest_dir.glob('**/*'):
    if not file.is_dir():
      if 'template' in file.name:
        new_name = file.name.replace('template', args.element_name)
        shutil.move(file, file.parent / new_name)

  for file in dest_dir.glob('**/*'):
    if not file.is_dir():
      print(file)
      replace_text(file, args.element_name, args.component_name)


