from collections import namedtuple
from datetime import datetime
from PDF4RoomKey import DataHelper


class PDFTemplate:
    def __init__(self, template):
        """
        Initializes a Template object.

        Args:
            template (dict): A dictionary containing the template configuration.

        Attributes:
            fields (dict): A dictionary containing the fields configuration.
            date_format (str): The date format used in the template.
            orientation (str): The orientation of the template (L for landscape, P for portrait).
            unit (str): The unit of measurement used in the template.
            pdf_format (list): The format of the PDF (width and height).
            font (str): The font used in the template.
            font_size (int): The font size used in the template.
            full_name (str): The format of the full name field.
        """
        self.fields = template.get("fields", None)
        if not self.fields:
            self.fields = {
                "id":            {"x": -1, "y":  0, "type": "text"},
                "full_name":     {"x": 90, "y": 37, "type": "name", "key": False},
                "arrival":       {"x": 90, "y": 63, "type": "date"},
                "departure":     {"x": 90, "y": 76, "type": "date"},
                "breakfast":     {"x": 112, "y":  90, "type": "checkbox"},
                "room":          {"x": 90, "y": 50, "type": "text"}
            }
        self.date_format = template.get("date_format",  "%d.%m.%Y")
        self.orientation = template.get("orientation", "L")
        self.unit = template.get("unit", "mm")
        self.pdf_format = template.get("format", [105,148.5]) # A6
        self.font = template.get("font", "Arial")
        self.font_size = template.get("font_size", 10)
        self.full_name = template.get("full_name", "{last_name}, {first_name}")

    def format_arrivals(self, arrivals):
        """
        Formats a list of arrival data.

        Args:
            arrivals (list): A list of arrival data.

        Returns:
            list: A list of processed arrival data.
        """
        processed_arrivals = []

        for arrival in arrivals:
            processed_arrivals.append(self._format_arrival_fields(arrival))

        return processed_arrivals

    def _format_arrival_fields(self, arrival):
            """
            Formats the fields of an arrival.

            Args:
                arrival (dict): A dictionary containing the arrival data.

            Returns:
                dict: A dictionary containing the formatted arrival fields.

            Raises:
                None

            Examples:
                # Create an instance of the class
                template = Template()

                # Define the arrival data
                arrival_data = {
                    "firstName": "John",
                    "lastName": "Doe",
                    "checkInDate": "2022-01-01",
                    "roomNumber": "101"
                }

                # Format the arrival fields
                formatted_arrival = template.format_arrival_fields(arrival_data)

                # Print the formatted arrival fields
                print(formatted_arrival)
            """
            return_arrival = []

            for fieldname, field_data in self.fields.items():

                if field_data.get("key", True) and not arrival.get(fieldname):
                    continue

                Field = namedtuple("Field", ["name", "x", "y", "value", "font_size"], defaults=(self.font_size,))

                field = {}

                field["name"] = fieldname
                field["x"] = field_data.get("x", -1)
                field["y"] = field_data.get("y", -1)

                if field_data["type"] == "date":
                    field["value"] = datetime.fromisoformat(arrival[fieldname]).strftime(self.date_format)

                elif field_data["type"] == "name":
                    field["value"] = DataHelper.build_full_name(arrival.get("firstName"), arrival.get("lastName"), format=self.full_name)
                    field["font_size"] = DataHelper.resize_full_name(field["value"])
                else:
                    field["value"] = arrival.get(fieldname, "")

                return_arrival.append(Field(**field))

            return return_arrival
