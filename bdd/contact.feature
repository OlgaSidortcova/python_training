Scenario Outline: Add new contact
    Given a contact list
    Given a contact with <firstname> and <lastname> 
    When I add the contact to the list
    Then the new contact list is equal to the old list with the added contact

    Examples:
    | firstname  | lastname  |
    | name1 	 | lastname1 | 
    | name2 	 | lastname2 |
	 

Scenario: Delete a contact
    Given a non-empty contact list
    Given a random contact from the list
    When I delete the contact from the list
    Then the new contact list is equal to the old list without the delete contact

Scenario: Modify a contact
    Given a non-empty contact list
    Given a random contact from the list
    Given a contact with <firstname> and <lastname>
    When I modify the contact from the list
    Then the new contact list is equal to the old list with change the modify contact

    Examples:
    | firstname  | lastname  |
    | newfname 	 | newlname | 