# Created by kodycarling at 9/10/20
Feature: Menu Widget
  Menu Widget at https://demoqa.com/accordian

  Scenario: Hovering over Menu items
    When hovering over menu items
    Then color changes from light green to dark green


  Scenario: Hovering on Main Item 2
    When hovering over "Main Item 2"
    Then sub items are present
