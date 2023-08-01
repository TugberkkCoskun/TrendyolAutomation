Feature: Trendyol Basic Automation Task

  @main_page
  Scenario: Trendyol Main Page
    Given User shall go to the www.trendyol.com and saw the main page is opened
    Then User shall verify that the opened page is trendyols main page
    When User shall close the pop-up and enters "şort" in the text box
    When User shall clears the text box
    When User enters "gömlek" in the text box
    When User shall presses the enter key on the keyboard
    Then User shall see the gömlek results are displayed

  Scenario: Trendyol Gömlek Page
    Given User shall go to the "https://www.trendyol.com/sr?q=g%C3%B6mlek&qt=g%C3%B6mlek&st=g%C3%B6mlek&os=1"
    When User shall randomly select one of the listed results
    Then User shall see the randomly selected gömlek page is openen
    And User shall add randomly selected gömlek to the basket
    And User shall verify that the price of the item in the basket is the same with the one on the gömlek page

  Scenario: Quantity increase or decrease
    Given User is on the selected gömlek page
    When User increase the quantity
    Then User shall see the quantity is increased,
    And User shall verified that the quantity of the product is 2
    When User press the bin button
    Then User shall verify that the basket is empty