from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    
    # Create PDF
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def generate_pdf_filename(assessment):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"fitness_plan_{assessment.id}_{timestamp}.pdf"