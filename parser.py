class Parser:
    def __init__(self):
        self.in_string = False  
        self.in_number = False 
        self.in_object = False  
        self.in_key = False    

        # parsed: dict containing parsed json
        self.parsed = None  
        self.key = None     
        # character buffer for state management
        self.buff = ""     

    def post_chunk(self):
        if self.in_key:
            if self.buff:
                self.parsed[self.buff] = None
        else:
            if self.buff:
                value = self.buff
                # float / int handling
                if self.in_number:
                    value = float(self.buff)
                    if value.is_integer():
                        value = int(value)
                    self.in_number = False

                self.parsed[self.key] = value
            else:
                self.parsed[self.key] = None

    def parse_object(self, char):
        # inside object context handling
        if char == ':':
            # Colon -> key, start of value
            self.in_key = False
            self.key = self.buff
            self.parsed[self.key] = None
            self.buff = ""
        elif char == ',':
            # Comma -> end of value, start of new key
            self.post_chunk()
            self.buff = ""
            self.in_key = True
        elif char == '}':
            # Closing brace -> end of object
            self.post_chunk()
            self.buff = ""
            self.in_object = False

    def parse_string(self, char):
        # Handle string context
        if char != '"':
            self.buff += char
        else:
            self.in_string = False

    def parse_number(self, char):
        # Handle number context
        if char.isdigit() or char == '.':
            self.buff += char
        else:
            if self.in_object:
                self.parse_object(char)

    def parse(self, stream):
        for chunk in stream:
            # handle leftover key from previous chunk
            if self.in_key and self.buff:
                self.parsed.pop(self.buff)

            for char in chunk:
                if char == ' ' and not self.in_string:
                    continue

                elif self.in_string:
                    self.parse_string(char)

                elif self.in_number:
                    self.parse_number(char)

                elif char.isdigit() or char == '.':
                    # Start of a number
                    self.in_number = True
                    self.buff += char

                elif char == '"':
                    # Start of a string
                    self.in_string = True

                elif self.in_object:
                    self.parse_object(char)

                elif char == '{':
                    # Start of a new object
                    self.in_object = True
                    self.in_key = True
                    self.parsed = {}

                else:
                    print("error")

            if self.in_object:
                self.post_chunk()
            yield self.parsed
