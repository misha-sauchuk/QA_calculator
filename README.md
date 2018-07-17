# QA_calculator is program to carry out the first three tests for web interface of the calculator

to run this program you should follow next steps:
  - clone this repository
  - install selenium and py.test packages
  - for Chrome Web Browser you should change the path to you Chrome Weddriver in line 10 QA_calculator/fixture/application.py
  - for Fire Fox Web Browser you should uncomment line 9 and comment line 10 QA_calculator/fixture/application.py
  - run files according to you IDE or with terminal use command: "py.test file_name.py" for files:
      - QA_calculator/test/test_initial_interface.py
      - QA_calculator/test/test_display_digit.py
      - QA_calculator/test/test_display_symbol.py
     
