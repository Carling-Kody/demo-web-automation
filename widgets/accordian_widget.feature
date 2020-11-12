# Created by kodycarling at 9/10/20
Feature: Accordian Widget
  Accordian Widget at https://demoqa.com/accordian

  Scenario: Landing on the page
    When  I render the landing page
    Then The first section heading, What is Lorem Ipsum?, Should have information(div) showing

  Scenario: Only one section heading should be showing at once
    When I click on any given accordian section heading
    Then Only one card-body should be showing