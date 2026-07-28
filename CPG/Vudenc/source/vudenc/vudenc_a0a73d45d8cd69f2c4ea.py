from flask import Blueprint, request, jsonify, redirect, url_for, render_template, flash, Response
from flask_login import login_required, current_user
from app.Data.operations import create_action, get_dataset_with_id
from app.Data.helpers import table_name_to_object
from app.Data.Transform.operations import restore_original, change_attribute_type, delete_rows, fill_null_with, fill_null_with_average, fill_null_with_median, rename_attribute, delete_attribute, one_hot_encode, normalize_attribute, discretize_width, discretize_eq_freq, find_replace, regex_find_replace, substring_find_replace
_transform = Blueprint('transform_bp', __name__, url_prefix='/data/transform')
@_transform.route('/rename_column', methods=['POST'])...
dataset = get_dataset_with_id(request.args.get('dataset_id'))
col = request.form['column']
new_name = request.form['new_name']
rename_attribute(dataset.working_copy, col, new_name)
flash('An unexpected error occured while renaming the column', 'danger')
flash('Column renamed successfully.', 'success')
create_action('Renamed column {0} to {1}'.format(col, new_name), dataset.id,
    current_user.id)
return redirect(request.referrer)
