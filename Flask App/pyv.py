import pyvan

OPTIONS = {
  "main_file_name": "final.py",
  "show_console": True,
  "use_existing_requirements": True,
  "extra_pip_install_args": [],
  "use_pipreqs": False,
  "install_only_these_modules": [],
  "exclude_modules": [],
  "include_modules": [],
  "path_to_get_pip_and_python_embedded_zip": "",
  "build_dir": "dist",
  "pydist_sub_dir": "pydist",
  "source_sub_dir": "",
}

pyvan.build(**OPTIONS)
