import os
import subprocess
from flask import Flask, render_template, request, redirect, url_for
from pygments import highlight
from pygments.lexers import YamlLexer
from pygments.formatters import HtmlFormatter

app = Flask(__name__)

K8S_CONFIG_DIR = "."  # Directory containing Kubernetes YAML files


def get_folders():

    """Gets a list of subdirectories in the K8S_CONFIG_DIR."""
    return [
        f
        for f in os.listdir(K8S_CONFIG_DIR)
        if os.path.isdir(os.path.join(K8S_CONFIG_DIR, f))
    ]


def get_files(folder):
    """Gets a list of YAML files in a specified folder."""
    folder_path = os.path.join(K8S_CONFIG_DIR, folder)
    return [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(".yaml")
    ]


def read_file(folder, filename):
    """Reads the content of a YAML file."""
    filepath = os.path.join(K8S_CONFIG_DIR, folder, filename)
    with open(filepath, "r") as f:
        return f.read()


def write_file(folder, filename, content):
    """Writes content to a YAML file."""
    filepath = os.path.join(K8S_CONFIG_DIR, folder, filename)
    with open(filepath, "w") as f:
        f.write(content)


def apply_file(folder, filename):
    """Applies a YAML file to Kubernetes using kubectl."""
    filepath = os.path.join(K8S_CONFIG_DIR, folder, filename)
    result = subprocess.run(
        ["kubectl", "apply", "-f", filepath], capture_output=True, text=True
    )
    return result.stdout, result.stderr


@app.route("/")
def index():
    """Displays the list of folders in the k8s_config directory."""
    folders = get_folders()
    return render_template("index.html", folders=folders)


@app.route("/<folder>")
def folder(folder):
    """Displays the list of files in a specified folder."""
    files = get_files(folder)
    return render_template("folder.html", folder=folder, files=files)


@app.route("/<folder>/<filename>")
def file(folder, filename):
    """Displays the content of a YAML file."""
    content = read_file(folder, filename)    
    formatter = HtmlFormatter(style="colorful")
    formatter_style = formatter.get_style_defs('.highlight')
    highlighted_content = highlight(content, YamlLexer(), formatter)
    return render_template("file.html", folder=folder, filename=filename, content=content, highlighted_content=highlighted_content, formatter_style=formatter_style)
    

@app.route("/<folder>/<filename>/edit", methods=["GET", "POST"])
def edit(folder, filename):
    """Edits the content of a YAML file."""
    if request.method == "POST":
        content = request.form["content"]
        write_file(folder, filename, content)
        return redirect(url_for("file", folder=folder, filename=filename))
    else:
        content = read_file(folder, filename)
        return render_template(
            "edit.html", folder=folder, filename=filename, content=content
        )


@app.route("/<folder>/<filename>/apply", methods=["POST"])
def apply(folder, filename):
    """Applies a YAML file to Kubernetes and returns the result."""
    stdout, stderr = apply_file(folder, filename)
    return render_template("apply.html", stdout=stdout, stderr=stderr)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")