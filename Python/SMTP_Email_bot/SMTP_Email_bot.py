import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from contextlib import contextmanager
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from a .env file
load_dotenv()

@contextmanager
def smtp_connection(smtp_server, port, username, password):
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Start TLS for security
        server.login(username, password)
        yield server
    finally:
        server.quit()

def send_email_via_smtp(from_email, to_email, subject, body, attachments=None):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    if attachments:
        for attachment in attachments:
            with open(attachment, 'rb') as file:
                part = MIMEImage(file.read(), name=os.path.basename(attachment))
                msg.attach(part)

    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = int(os.getenv('SMTP_PORT'))
    smtp_username = os.getenv('SMTP_USERNAME')
    smtp_password = os.getenv('SMTP_PASSWORD')

    if not smtp_server or not smtp_username or not smtp_password:
        raise ValueError("SMTP configuration is incomplete")

    try:
        with smtp_connection(smtp_server, smtp_port, smtp_username, smtp_password) as server:
            server.send_message(msg)
        print('Email sent successfully!')
    except Exception as e:
        print(f'An error occurred while sending the email: {e}')
        raise

def get_most_recent_rtf_file(directory):
    rtf_files = [f for f in os.listdir(directory) if f.endswith('.rtf')]
    if not rtf_files:
        raise FileNotFoundError("No .rtf files found in the specified directory.")
    most_recent_rtf_file = max(rtf_files, key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    return os.path.join(directory, most_recent_rtf_file)

def parse_rtf_file(file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    email_details = {}
    for line in content:
        if line.startswith('FROM:'):
            email_details['FROM'] = line.split('FROM:')[1].strip()
        elif line.startswith('TO:'):
            email_details['TO'] = line.split('TO:')[1].strip()
        elif line.startswith('SUBJECT:'):
            email_details['SUBJECT'] = line.split('SUBJECT:')[1].strip()
        elif line.startswith('BODY:'):
            email_details['BODY'] = line.split('BODY:')[1].strip()
        elif line.startswith('ATTACHMENTS:'):
            email_details['ATTACHMENTS'] = [attachment.strip() for attachment in line.split('ATTACHMENTS:')[1].split(',') if attachment.strip()]
    return email_details

def display_email_details(email_details):
    print("\nParsed Email Details:")
    print(f"FROM: {email_details['FROM']}")
    print(f"TO: {email_details['TO']}")
    print(f"SUBJECT: {email_details['SUBJECT']}")
    print(f"BODY:\n{email_details['BODY']}")
    if 'ATTACHMENTS' in email_details:
        print("ATTACHMENTS:")
        for attachment in email_details['ATTACHMENTS']:
            print(f"- {attachment}")

def confirm_send_email():
    while True:
        confirmation = input("\nDo you want to send the email? (yes/no): ").lower()
        if confirmation in ['yes', 'no']:
            return confirmation == 'yes'
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def rename_rtf_file(original_path, to_email):
    directory, filename = os.path.split(original_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{timestamp}_{to_email}.rtf"
    new_path = os.path.join(directory, new_filename)
    os.rename(original_path, new_path)
    print(f"Renamed file to: {new_filename}")

if __name__ == '__main__':
    # Specify the directory where the script will search for the most recent .rtf file
    directory = '/path/to/your/directory'

    # Get the most recent .rtf file
    rtf_file = get_most_recent_rtf_file(directory)

    # Parse the .rtf file to extract email details
    email_details = parse_rtf_file(rtf_file)

    # Display the parsed email details
    display_email_details(email_details)

    # Ask for confirmation before sending the email
    if confirm_send_email():
        # Send the email using the extracted details
        send_email_via_smtp(email_details['FROM'], email_details['TO'], email_details['SUBJECT'], email_details['BODY'], attachments=email_details.get('ATTACHMENTS', []))
        
        # Rename the .rtf file after sending the email
        rename_rtf_file(rtf_file, email_details['TO'])
    else:
        print("Email not sent. Exiting...")