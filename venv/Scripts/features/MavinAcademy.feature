Feature: Mavin Academy Home Page
      Scenario: Display the Home Page of Mavin Academy
        Given launch Chrome browser
        When open Mavin Web site
        Then verify that the home page displayed
        And close browser