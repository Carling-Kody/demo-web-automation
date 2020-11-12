# Created by kodycarling at 9/10/20
Feature: Progress Bar Widget
  Progress Bar Widget on https://demoqa.com/progress-bar

  Scenario: Progress bar progresses
    When clicking the start button waiting 3 seconds and clicking stop
    Then the progress bar will show 3 seconds of progress

  Scenario: Progress Bar is not saved
    When clicking the start button waiting 3 seconds and clicking stop then refresh the page
    Then The progress bar is reset to default
