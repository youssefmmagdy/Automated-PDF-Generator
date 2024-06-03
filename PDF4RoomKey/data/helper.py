class DataHelper:
    """
    A helper class for data manipulation and processing.
    """

    @staticmethod
    def build_full_name(first_name: str, last_name: str, format="{last_name}, {first_name}") -> str:
        """
        Builds a full name by combining the first name and last name.

        Args:
            first_name (str): The first name.
            last_name (str): The last name.
            format (str, optional): The format of the full name. Defaults to "{last_name}, {first_name}".

        Returns:
            str: The full name.
        """
        
        tmpl = format

        if not first_name:
            tmpl = "{last_name}"
        
        if not last_name:
            last_name = "ZZZ"

        full_name = tmpl.format(first_name=first_name, last_name=last_name)

        if len(full_name) > 30:
            full_name = tmpl.format(first_name=first_name[0], last_name=last_name)

        if len(full_name) > 28:
            full_name = full_name[0:28] + ".."

        return full_name
    
    @staticmethod
    def resize_full_name(full_name: str) -> float:
        """
        Resize a full name to fit the name field.

        Args:
            full_name (str): The full name.

        Returns:
            float: The size of the resized full name.
        """
        i = len(full_name)
        size = 12.0
        if i > 40:
            size = 8
        elif i > 30:
            size = 8.5
        elif i > 25:
            size = 9    
        elif i > 20:
            size = 10
        elif i > 15:
            size = 11
        
        return size