# seeder.py

from sqlalchemy.orm import Session
from src.configuration.sql_config import get_db
from src.models.template_model import HtmlTemplate

def upload_templates():
    db: Session = next(get_db())

    templates = [
        {
            "name": "welcome",
            "subject": "Welcome to Our Service",
            "body": """
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        body { font-family: Arial, sans-serif; }
                        h1 { color: #4CAF50; }
                        .container { padding: 20px; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Welcome {{ name }}!</h1>
                        <p>Thank you for joining us. We’re excited to have you on board.</p>
                    </div>
                </body>
                </html>
            """
        },
        {
            "name": "reset_password_email",
            "subject": "Reset Your Password",
            "body": """
                <!DOCTYPE html>
                <html>
                <head>
                    <style>
                        body { font-family: Arial, sans-serif; }
                        h1 { color: #f44336; }
                        .container { padding: 20px; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Password Reset</h1>
                        <p>Click the link below to reset your password:</p>
                        <a href="{{ reset_link }}">Reset Password</a>
                    </div>
                </body>
                </html>
            """
        },
        {
            "name": "generate_invoice_email",
            "subject": "Generate Invoice",
            "body": """
                <!DOCTYPE html>
                <html>
                <head>    
                    <style>
                        body { font-family: Arial, sans-serif; }
                        h1 { color: #4CAF50; }
                        .container { padding: 20px; }
                        table { width: 100%; border-collapse: collapse; }
                        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                        th { background-color: #f2f2f2; }
                    </style>
                </head>
                <body>
                    <div class="container">
                        <h1>Invoice</h1>
                        <table>
                            <tr>
                                <th>Item</th>
                                <th>Quantity</th>
                                <th>Price</th>
                            </tr>
                            {% for data in items %}
                            <tr>
                                <td>{{ data.item }}</td>
                                <td>{{ data.quantity }}</td>
                                <td>{{ data.price }}</td>
                            </tr>
                            {% endfor %}
                        </table>
                    </div>
                </body>
                </html>
            """
        },
        {
            "name": "generate_invoice_pdf",
            "subject": "Test Subject",
            "body": """
                <html>
                    <head>
                        <style>
                            body { font-family: Arial, sans-serif; }
                            table { width: 100%; border-collapse: collapse; }
                            th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                            th { background-color: #f2f2f2; }
                        </style>
                    </head>
                    <body>
                        <h1>Invoice</h1>
                        <table>
                            <tr>
                                <th>Item</th>
                                <th>Quantity</th>
                                <th>Price</th>
                            </tr>
                            {% for data in items %}
                            <tr>
                                <td>{{ data.item }}</td>
                                <td>{{ data.quantity }}</td>
                                <td>{{ data.price }}</td>
                            </tr>
                            {% endfor %}
                        </table>
                    </body>
                </html>
            """
        }
    ]

    for tmpl in templates:
        existing = db.query(HtmlTemplate).filter_by(name=tmpl['name']).first()
        if not existing:
            db.add(HtmlTemplate(**tmpl))
            print(f"[+] Inserted template: {tmpl['name']}")
        else:
            print(f"[=] Template already exists: {tmpl['name']}")

    db.commit()
    db.close()
