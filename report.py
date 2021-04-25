import os
import jinja2
import webbrowser
import statistics as st

BLINKS_PER_MINUTE_RECOMMENDED = 20
BLINK_POSITIVE_MESSAGE = "Optimal, above that recommended by the WHO"
BLINK_WARNING_MESSAGE = "Below that recommended by the WHO"
DANGER_TEXT_COLOR_CLASS = "text-danger"
SUCCESS_TEXT_COLOR_CLASS = "text-success"


def get_blink_average_results(blink_average):
    percentage = ((blink_average/BLINKS_PER_MINUTE_RECOMMENDED)*100) - 100
    message = BLINK_WARNING_MESSAGE if blink_average < BLINKS_PER_MINUTE_RECOMMENDED else BLINK_POSITIVE_MESSAGE
    color = DANGER_TEXT_COLOR_CLASS if blink_average < BLINKS_PER_MINUTE_RECOMMENDED else SUCCESS_TEXT_COLOR_CLASS
    return percentage, message, color


def generate_report(blink_data, body_position_data):
    if blink_data and body_position_data:

        blink_average = round(st.mean(blink_data))
        blink_percentage, blink_message, blink_color = get_blink_average_results(blink_average)

        data = {
            'time': len(blink_data),
            'blink_average': blink_average,
            'blink_percentage': blink_percentage,
            'blink_message': blink_message,
            'blink_color': blink_color,
            'upper_blink_ratio': max(blink_data),
            'lower_blink_ratio': min(blink_data),
            'blink_labels': list(range(1, len(blink_data)+1)),
            'blink_data': blink_data,
            'body_position_labels': list(range(1, len(blink_data) + 1)),
            'body_position_data': body_position_data
        }

        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
        template = jinja_env.get_template('layout.html')

        with open("template/report.html", "w") as file:
            file.write(template.render(data))


def show_last_report():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    url = os.path.join(os.path.dirname(__file__), 'template/report.html')
    webbrowser.get(chrome_path).open(url, new=2)

