import time
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
import csv
from tqdm import tqdm


class Bot(webdriver.Chrome):
    def __init__(self, driver_path, company_name='', company_industry='',
                 teardown=False):
        os.environ['PATH'] += driver_path
        self.company_name = company_name
        self.company_industry = company_industry
        self.teardown = teardown
        super(Bot, self).__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def waiting(self):
        time.sleep(15)
        crnt_btn = self.find_element(By.CLASS_NAME, 'ChatMessageSendButton_sendButton__4ZyI4').get_attribute('disabled')
        while crnt_btn is not None:
            crnt_btn = self.find_element(By.CLASS_NAME, 'ChatMessageSendButton_sendButton__4ZyI4').get_attribute(
                'disabled')
        time.sleep(15)

    def send_prompt(self, prompt):
        text_field = self.find_element(By.CLASS_NAME, 'GrowingTextArea_textArea__ZWQbP')
        text_field.click()
        text_field.send_keys(f'{prompt}')

        send = self.find_element(By.CLASS_NAME, 'ChatMessageSendButton_sendButton__4ZyI4')
        send.click()

        self.waiting()

    def timer(self, t):
        for _ in tqdm(range(t), desc="Seconds remaining", unit="seconds", ncols=80):
            time.sleep(1)

    def login(self):
        self.implicitly_wait(200)
        self.get('https://poe.com')

        print('Login Timer')
        self.timer(60)

        gpt = self.find_element(By.CSS_SELECTOR, 'a[href="/chat/2gch5w7b1p6z6fll4bg"]')
        gpt.click()

        self.timer(20)
        print('Login Completed')

    def prompt(self, position, info=''):
        self.implicitly_wait(200)
        if len(info) == 0:
            prompt = f"Imagine you are a hiring manager for a {self.company_industry} agency name {self.company_name}. " \
                     f"Your company is looking for a highly skilled and experienced {position} to join the team and drive online growth for clients. " \
                     "Write a job description that effectively communicates the job purpose, requirements, responsibilities, key performance indicators, qualifications, experience, skills and competencies for this position. " \
                     "Use persuasive language and emphasize the key aspects that make your company an attractive employer for top talent in the digital marketing field. " \
                     "Make sure to highlight the opportunities for professional growth and the exciting projects the candidate will be involved in. Be concise, engaging, and capture the essence of your company's values and vision. " \
                     "Create a separate section for each of the required items. "
        else:
            prompt = f"Imagine you are a hiring manager for a {self.company_industry} agency name {self.company_name}. " \
                     f"Your company is looking for a highly skilled and experienced {position} to join the team and drive online growth for clients. " \
                     "Write a job description that effectively communicates the job purpose, requirements, responsibilities, key performance indicators, qualifications, experience, skills and competencies for this position. " \
                     "Use persuasive language and emphasize the key aspects that make your company an attractive employer for top talent in the digital marketing field. " \
                     "Make sure to highlight the opportunities for professional growth and the exciting projects the candidate will be involved in. Be concise, engaging, and capture the essence of your company's values and vision. " \
                     f"Create a separate section for each of the required items. You can use the following information as an asset. {info}"

        self.send_prompt(prompt)

        job_description = self.find_elements(By.CLASS_NAME, 'Markdown_markdownContainer__Tz3HQ')[-1].get_attribute(
            'textContent').strip()

        file = open('Job Descriptions.csv', 'a', newline='')
        writer = csv.writer(file)
        writer.writerow([f'{position}', job_description])
        file.close()
