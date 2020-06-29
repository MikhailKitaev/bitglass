Feature: header menu


  Scenario: Request a Demo
        Given I load the website
        When  I click "Request a Demo" link
        Then  I can see "Request a Demo" registration page

  Scenario: What is SASE
        Given I load the website
        When  I click "SASE"
        And   I click "What is SASE" link
        Then  I can see "What is SASE" page

  Scenario: What is CASB
        Given I load the website
        When  I click "SASE"
        And   I click "What is CASB" link
        Then  I can see "What is CASB" page

  Scenario: What is CASB Architecture
        Given I load the website
        When  I click "SASE"
        And   I click "CASB Architecture" link
        Then  I can see "CASB Architecture" page

  Scenario: CASB Magic Quadrant
        Given I load the website
        When  I click "SASE"
        And   I click "CASB Magic Quadrant" link
        Then  I can see "CASB Magic Quadrant" page


  Scenario: All Cloud Apps
        Given I load the website
        When  I click "Products"
        And   I click "All Cloud Apps" link
        Then  I can see "All Cloud Apps" page

  Scenario: Office 365
        Given I load the website
        When  I click "Products"
        And   I click "Office 365" link
        Then  I can see "Office 365" page

  Scenario: G Suite
        Given I load the website
        When  I click "Products"
        And   I click "G Suite" link
        Then  I can see "G Suite" page

  Scenario: Salesforce
        Given I load the website
        When  I click "Products"
        And   I click "Salesforce" link
        Then  I can see "Salesforce" page

  Scenario: Box
        Given I load the website
        When  I click "Products"
        And   I click "Box" link
        Then  I can see "Box" page

  Scenario: Dropbox
        Given I load the website
        When  I click "Products"
        And   I click "Dropbox" link
        Then  I can see "Dropbox" page

  Scenario: Exchange
        Given I load the website
        When  I click "Products"
        And   I click "Exchange" link
        Then  I can see "Exchange" page

  Scenario: Amazon (AWS)
        Given I load the website
        When  I click "Products"
        And   I click "Amazon (AWS)" link
        Then  I can see "Amazon (AWS)" page

  Scenario: Slack
        Given I load the website
        When  I click "Products"
        And   I click "Slack" link
        Then  I can see "Slack" page

  Scenario: JIRA/Confluence
        Given I load the website
        When  I click "Products"
        And   I click "JIRA/Confluence" link
        Then  I can see "JIRA/Confluence" page

  Scenario: Cisco Spark
        Given I load the website
        When  I click "Products"
        And   I click "Cisco Spark" link
        Then  I can see "Cisco Spark" page

  Scenario: Workday
        Given I load the website
        When  I click "Products"
        And   I click "Workday" link
        Then  I can see "Workday" page
