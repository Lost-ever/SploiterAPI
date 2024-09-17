from flask import Flask, send_from_directory

app = Flask("SPLOITER")

@app.route('/dexFiles/<path:filename>')
def serve_dex(filename):
    return send_from_directory('static/DexFiles', filename)

@app.route('/JarFiles/<path:filename>')
def serve_static(filename):
    return send_from_directory('static/JarFiles', filename)

@app.route('/SmaliFiles/<path:filename>')
def serve_static(filename):
    return send_from_directory('static/SmaliFiles', filename)

def handler(request):
    with app.app_context():
        return app.full_dispatch_request()