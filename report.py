import os
import jinja2
import webbrowser
import statistics as st


def generate_report(blink_data, body_position_data):
    if blink_data:
        data = {
            'time': len(blink_data),
            'average_blink': round(st.mean(blink_data)),
            'upper_blink_ratio': max(blink_data),
            'lower_blink_ratio': min(blink_data),
            'blink_labels': list(range(1, len(blink_data)+1)),
            'blink_data': blink_data
        }

        jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
        template = jinja_env.get_template('layout.html')

        with open("template/report.html", "w") as file:
            file.write(template.render(data))


def show_last_report():
    url = os.path.join(os.path.dirname(__file__), 'template/report.html')
    webbrowser.open(url, new=2)


#generate_report([2,3,4,5,12,11], None)
#show_last_report()
