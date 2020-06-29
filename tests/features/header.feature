Feature: header


  Scenario: Free Trial
        Given I load the website
        When  I click "Free Trial" link
        Then  I can see "Free Trial" registration page

  Scenario: Contact
        Given I load the website
        When  I click Contact link
        Then  I can see "Contact" page

  Scenario: Partner Login
        Given I load the website
        When  I click Partner Login link
        Then  I can see "Partner Login" page

  Scenario: Customer Login
        Given I load the website
        When  I click Customer Login link
        Then  I can see "Customer Login" page