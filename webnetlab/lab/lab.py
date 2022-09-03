from pathlib import Path

from flask import Blueprint, redirect, url_for, current_app, render_template

from functions import lab_controls, graph


lab_bp = Blueprint("lab_bp", __name__, template_folder="templates", static_folder="static")


@lab_bp.get("/")
def lab_root():
    return redirect(url_for("list_labs"), 303)


@lab_bp.get("/list")
def list_labs():
    lab_table = {}
    lab_dir_list = lab_controls.scan_for_lab_folders(current_app.config.path_to_lab_files)
    for lab in lab_dir_list:
        lab_table[lab] = {}
        lab_details = lab_controls.parse_lab_specification(Path(current_app.config.path_to_lab_files) / lab / current_app.config.lab_spec_filename)
        try:
            lab_table[lab]["name"] = lab_details["name"]
        except KeyError:
            lab_table[lab]["name"] = "---"
        try:
            lab_table[lab]["author"] = lab_details["author"]
        except KeyError:
            lab_table[lab]["author"] = "---"
        try:
            lab_table[lab]["difficulty"] = lab_details["difficulty"]
        except KeyError:
            lab_table[lab]["difficulty"] = "---"
    return render_template("list_labs.html", lab_table=lab_table)


@lab_bp.get("/{lab_name}")
def open_lab_view(lab_name: str):
    lab_details = lab_controls.parse_lab_specification(Path(current_app.config.path_to_lab_files) / lab_name / current_app.config.lab_spec_filename)
    node_info = lab_controls.get_node_information(lab_name)
    return render_template("open_lab.html", lab_details=lab_details,node_info=node_info)


@lab_bp.post("/{lab_name}/deploy")
def deploy_lab_button(lab_name: str):
    path_to_clab_yaml = f"{current_app.config.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"
    try:
        lab_controls.deploy_lab(path_to_clab_yaml)
        return {"success": "lab is deployed"}, 200
    except Exception as e:
        return {"error": "something went wrong during the deployment process, {}".format(e)}, 503


@lab_bp.post("/{lab_name}/destroy")
def destroy_lab_button(lab_name: str):
    path_to_clab_yaml = f"{current_app.config.path_to_lab_files}{lab_name}/{lab_name}.clab.yml"
    try:
        lab_controls.destroy_lab(path_to_clab_yaml)
        return {"success": "lab is destroyed"}, 200
    except Exception as e:
        return {"error": "something went wrong during destruction process, {}".format(e)}, 503


@lab_bp.post("/status")
def check_lab_status():
    return lab_controls.check_status(), 200


@lab_bp.get("/{lab_name}/topology")
def get_lab_topology(lab_name: str):
    try:
        return graph.create_topology(lab_name), 200
    except Exception as e:
        return {"error": "something went wrong while trying to create lab, topology {}".format(e)}, 503
