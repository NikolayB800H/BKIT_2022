@gen_random
Feature: gen_random
    Generator function to generate random integer.

Scenario: Giving count, begin and end
    Given 5 numbers to generate from 2 to 2
    When using gen_random generator
    Then I should get these numbers

    Given 5 numbers to generate from 1 to 3
    When using gen_random generator
    Then I should get these numbers

    Given 5 numbers to generate from -3 to -1
    When using gen_random generator
    Then I should get these numbers
