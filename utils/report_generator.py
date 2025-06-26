# utils/report_generator.py
from xhtml2pdf import pisa

def generate_html_report(summary_text):
    html = f"""
    <html>
    <head>
    <style>
        @page {{ size: A4; margin: 1in; }}
        body {{
            font-family: 'Helvetica Neue', sans-serif;
            font-size: 14pt;
            color: #333;
            line-height: 1.6;
        }}
        h1 {{
            font-size: 24pt;
            text-align: center;
            margin-bottom: 30px;
        }}
        h2 {{
            font-size: 18pt;
            margin-top: 25px;
            margin-bottom: 10px;
            color: #1a1a1a;
        }}
        ul {{
            margin-left: 20px;
        }}
        p, li {{
            margin-bottom: 10px;
        }}
        .footer {{
            margin-top: 40px;
            font-size: 12pt;
            text-align: center;
            color: #555;
        }}
    </style>
    </head>
    <body>
        <h1>Influencer Performance Summary</h1>
        <p>{summary_text.replace('**', '').replace('\n', '<br>')}</p>

        <div class="footer">
            <p><strong>Made by Khan Faisal</strong></p>
            <p>\ud83d\udccc <a href='https://khanfaisal.netlify.app'>https://khanfaisal.netlify.app</a></p>
        </div>
    </body>
    </html>
    """

    with open("influencer_report.pdf", "w+b") as result_file:
        pisa.CreatePDF(html, dest=result_file)
