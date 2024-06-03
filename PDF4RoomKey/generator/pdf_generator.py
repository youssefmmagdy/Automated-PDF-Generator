from datetime import datetime
from fpdf import FPDF
from PDF4RoomKey import DataFetcher, Authenticator, PDFTemplate 
from PDF4RoomKey.settings import BASE_API_URL

class PDFGenerator:
    def __init__(self, api_key=None, api_url=BASE_API_URL, template=None):
            """
            Initializes the PDFGenerator object.

            Args:
                api_key (str, optional): The API key for authentication. If not provided, a bearer token will be generated.
                api_url (str, optional): The base URL for the API. Defaults to BASE_API_URL.
                template (str, optional): The template for the PDF generation. Defaults to None.
            """
            # if api_key is None:
            #     self.api_key = Authenticator.generate_bearer_token()
            # else:
            self.api_key = api_key

            self.data_fetcher = DataFetcher(api_url, api_key)
            self.template = PDFTemplate(template)

    def generate_pdf(self, date, output_path: str | None = None):
        """
        Generates a PDF using the provided template and saves it to the specified output path.

        Args:
            date (str): The date for which the arrivals data will be fetched.
            output_path (str, optional): The path where the generated PDF will be saved. If not provided, the PDF will not be saved and will be returned instead.

        Returns:
            FPDF: The generated PDF object if output_path is not set, otherwise None.
        """

        # Get the data
        data = self.data_fetcher.get_arrivals(date)
        # Refactor the data using the template
        data = self.template.format_arrivals(data)
        # Generate the PDF
        pdf = self._generate_pdf(data)
        
        if output_path is not None:
            # Save the PDF
            pdf.output(output_path)
            return None
        else:
            return pdf

    def _generate_pdf(self, arrivals):
            """
            Generates a PDF document based on the provided arrivals.

            Args:
                arrivals (list): A list of arrivals containing the necessary data for generating the PDF.

            Returns:
                FPDF: The generated PDF document.
            """
            # Create a PDF
            fpdf = FPDF(self.template.orientation, self.template.unit, self.template.pdf_format)
            # Set the font
            fpdf.set_font(self.template.font, size=self.template.font_size)

            arrivals = self.template.format_arrivals(arrivals)

            # Add a separate page for every arrival
            for arrival in arrivals:
                # Add a page
                fpdf.add_page()
                # Add the data
                for field in arrival:
                    if field.x < 0 or field.y < 0:
                        continue
                    
                    value = field.value
                    x = field.x
                    fpdf.set_font_size(field.font_size)
                    if(value == 'true'):
                        value = 'X'
                        x = 112
                    if(value == 'false'):
                        value = 'X'
                        x = 132
                    
                    fpdf.text(x, field.y, value)
            
            # Return the PDF
            return fpdf
