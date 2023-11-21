import os

def check_file_existence(file_path):
  if not os.path.isfile(file_path):
    raise Exception('File not found')

def create_dir_if_not_exists(dir_path):
  if not os.path.exists(dir_path):
    os.makedirs(dir_path)


def get_filename(file_path) -> str:
  dirname, basename = os.path.split(file_path)
  name, ext = os.path.splitext(basename)
  return name

def get_output_path_without_ext(input_path, output_dir) -> str:
  filename = get_filename(input_path)
  return os.path.join(output_dir, filename)

def check_file_and_directory(file_path, dir_path) -> str:
  check_file_existence(file_path)
  create_dir_if_not_exists(dir_path)
  output_path_without_ext = get_output_path_without_ext(file_path, dir_path)
  return output_path_without_ext