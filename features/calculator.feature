Feature: Test Calculator Functionality
  Scenario: Addition
    Given Calculator app is run
    When I input "2+3" to calculator
    Then I get result "5"

  Scenario: Subtraction
    Given Calculator app is run
    When I input "5-2" to calculator
    Then I get result "3"

  Scenario: Multiplication
    Given Calculator app is run
    When I input "6*3" to calculator
    Then I get result "18"

  Scenario: Multiple Operators
    Given Calculator app is run
    When I input "6+5*3" to calculator
    Then I get result "21"

  Scenario: Negative numbers
    Given Calculator app is run
    When I input "-3+5" to calculator
    Then I get result "2"


