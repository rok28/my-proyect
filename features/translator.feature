Feature: Google Translator

  @wip
  Scenario Outline: translate
    Given the user is in Google Translator page
    When the user selects origin <origin_language>
    And the user selects destiny <destiny_language>
    And the user writes <message> in origin
    Then the translated message is <translated_message>

    Examples:
      | origin_language | destiny_language | message | translated_message |
      |
