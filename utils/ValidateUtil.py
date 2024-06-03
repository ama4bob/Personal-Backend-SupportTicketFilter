class ValidateUtil():
    # Validates the ticket to see if the ticket is missing the time or the phone number, and it must be populated
    # Input: A ticket
    # Output: A boolean where False indicates the ticket is fine, and true otherwise
    def validateTicket(self, input: dict) -> bool:
        if bool(input) == False:
            return True

        if input.get("createdAt") != None and input.get("createdAt") != "" and input.get("tel") != None and input.get("tel") != "":
            return False
        return True

