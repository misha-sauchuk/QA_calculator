# QA_calculator is program to carry out the first three test for web interface of the calculator

to run this programm you shuold follow next steps:
  - clone this repository
  - install selenium and py.test packages
  - for Chrome Web Browser you should change the path to you Chrome Weddriver in line 10 QA_calculator/fixture/application.py
  - for Fire Fox Web Browser you should uncommit line 9 and commit line 10 QA_calculator/fixture/application.py
  - run files QA_calculator/test:
      - test_initial_interface.py
      - test_display_digit.py
      - test_display_symbol.py
      according to you IDE or with terminal use command: "py.test file_name.py"
