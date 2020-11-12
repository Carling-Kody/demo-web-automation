# Created by kodycarling at 9/10/20
Feature: Select Menu Widget
  Select Menu Widget on https://demoqa.com/select-menu

  Scenario: placeholders are set to default
    When Page is rendered
    Then Dropdown placeholders are set to default

  Scenario:  Multiselect drop-down can have more than one item selected
    When multiple items are selected
    Then all selected items are present

  Scenario: Multiselect drop-down are removed with clicking the main "x"
    When multiple items are selected, and the main "x" is clicked
    Then all selcted items are no longer present.
