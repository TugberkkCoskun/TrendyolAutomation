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
  @gomlek_page
  Scenario: Trendyol Gömlek Page
    Given User shall go to the "https://www.trendyol.com/sr?q=g%C3%B6mlek&qt=g%C3%B6mlek&st=g%C3%B6mlek&os=1"
    When User shall randomly select one of the listed results
    Then User shall add randomly selected gömlek to the basket
    Then User shall verify that the price of the item in the basket is the same with the one on the gömlek page
    When User increase the quantity
    Then User shall verified that the quantity of the product is 2
    When User press the bin button
    Then User shall verify that the basket is empty

   @login_page
   Scenario: Trendyol Login Page
     Given User Shall go to the trendyol main page and assert the main page is opened
     When User stay top of the giris yap icon and press giris yap button
     Then User shall assert that the login page is opened
     When User shall insert wrong e-mail and wrong password, correct e-mail and wrong password, wrong e-mail and correct password
     Then User shall assert that "E-posta adresiniz ve/veya şifreniz hatalı " warning appeared
     When User shall insert correct e-mail and correct password
     Then User Shall assert that login is successfull and directed to the main page
