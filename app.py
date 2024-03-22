from flask import Flask, render_template, request
from APIs.VTScan import vt_file_analysis, vt_scan_report
from APIs.HybridAnalysis import ha_file_report, ha_file_analysis

app = Flask("__main__")


@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename != '':
            file_data = file.read()
            vt_scan_result = vt_file_analysis(file_data)
            ha_scan_result = ha_file_analysis(file_data)
            vt_report_result = vt_scan_report(vt_scan_result['resource'])
            ha_report_result = ha_file_report(ha_scan_result['id'])
            return render_template('report.html', vt_scan=vt_scan_result, vt_report=vt_report_result, ha_report=ha_report_result, filename = file.filename)


    return render_template('home.html')




if __name__=="__main__":
    app.run(debug=True)