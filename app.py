from flask import Flask, render_template
from loguru import logger
app = Flask(__name__)

logger.add("/logs/logs.log", format="| Level={level} | Message={message}")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/log_info')
def log_info():
    #logger.add("./logs/logs.log")
    logger.info("Informação do registro INFO")
    return render_template("index.html")

@app.route('/log_trace')
def log_trace():
    logger.trace("Informação do registro TRACE")
    return render_template("index.html")

@app.route('/log_debug')
def log_debug():
    #logger.add("./logs/logs.log")
    logger.debug("Informação do registro DEBUG")
    return render_template("index.html")

@app.route('/log_success')
def log_success():
    #logger.add("./logs/logs.log")
    logger.success("Informação do registro SUCCESS")
    return render_template("index.html")

@app.route('/log_warn')
def log_warn():
    #logger.add("./logs/logs.log")
    logger.warning("Informação do registro WARNING")
    return render_template("index.html")

@app.route('/log_error')
def log_error():
    #logger.add("./logs.log")
    logger.error("Informação do registro ERROR")
    return render_template("index.html")

@app.route('/log_critical')
def log_critical():
    #logger.add("./logs.log")
    logger.critical("Informação do registro CRITICAL")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")