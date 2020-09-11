# Created by kodycarling at 9/10/20
Feature: # Add two numbers and return the sum


  Scenario: Adding two even numbers returns an even number
    Given x=2 and y=2
    When I add them together
    Then the sum should be 4
    And be even


  Scenario: Adding two negative numbers returns a negative number
    Given x=-2 and y=-2
    When I add them together
    Then the sum should be -4


  Scenario: Adding 0 to any number returns the same number (without any increase)
    Given x=-3 and y=0
    When I add them together
    Then the sum should be -3

  Scenario: Adding higher value positive number with a negative number should return a positive number
    Given x=10 and y=-7
    When I add them together
    Then the sum will be 3 and positive

  Scenario:  Adding higher value negative number with a positive number should return a negative number
    Given x=-10 and y=7
    When I add them together
    Then the sum will be -3 and negative