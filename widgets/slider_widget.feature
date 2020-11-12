# Created by kodycarling at 9/10/20
Feature: Slider Widget
   Slider Widget on https://demoqa.com/slider

  Scenario Outline: Slider position matches the value in the input field
    When I move slider to <position>
    Then the input should be <value>

    Examples:
    | position | value |
    | 25       | 25    |
    | 50       | 50    |

   Scenario: range slide value decreases when slid left
     When range_slider value > 0 if slider is moved left
     Then range_slider value < than original_value

   Scenario: range_slide_value increases when slid right
     When range_slider value > 0 if slider is moved right
     Then range_slider value < than original_value