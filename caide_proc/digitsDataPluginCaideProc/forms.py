# Copyright (c) 2016-2017, NVIDIA CORPORATION.  All rights reserved.
from __future__ import absolute_import

import os

from flask.ext.wtf import Form
from wtforms import validators

from digits import utils
from digits.utils import subclass
from digits.utils.forms import validate_required_iff


@subclass
class DatasetForm(Form):
    """
    A form used to create an image processing dataset
    """

    def validate_folder_path(form, field):
        if not field.data:
            pass
        else:
            # make sure the filesystem path exists
            if not os.path.exists(field.data) or not os.path.isdir(field.data):
                raise validators.ValidationError(
                    'Folder does not exist or is not reachable')
            else:
                return True

    def validate_file_path(form, field):
        if not field.data:
            pass
        else:
            # make sure the filesystem path exists
            if not os.path.exists(field.data) and not os.path.isdir(field.data):
                raise validators.ValidationError(
                    'File does not exist or is not reachable')
            else:
                return True

    feature_file = utils.forms.StringField(
        u'Feature image list file (.txt)',
        validators=[
            validate_file_path
        ],
        tooltip="Indicate a file list full of images."
    )

    label_file = utils.forms.StringField(
        u'Label image list file (.txt)',
        validators=[
            validate_file_path
        ],
        tooltip="Indicate a file list full of images. For each image in the feature"
                " image file list there must be one corresponding image in the label"
                " image file list. The label image must have the same filename except"
                " for the extension, which may differ. Label images are expected"
                " to be single-channel images (paletted or grayscale), or RGB"
                " images, in which case the color/class mappings need to be"
                " specified through a separate text file."
    )

    folder_pct_val = utils.forms.IntegerField(
        u'% for validation',
        default=10,
        validators=[
            validators.NumberRange(min=0, max=100)
        ],
        tooltip="You can choose to set apart a certain percentage of images "
                "from the training images for the validation set."
    )

    has_val_folder = utils.forms.BooleanField('Separate validation images',
                                              default=False,
                                              )

    validation_feature_file = utils.forms.StringField(
        u'Validation feature image list file (.txt)',
        validators=[
          validate_file_path
        ],
        tooltip="Indicate a file list full of images."
    )

    validation_label_file = utils.forms.StringField(
        u'Validation label image list file (.txt)',
        validators=[
          validate_file_path
        ],
        tooltip="Indicate a file list full of images. For each image in the feature"
                " image file list there must be one corresponding image in the label"
                " image file list. The label image must have the same filename except"
                " for the extension, which may differ. Label images are expected"
                " to be single-channel images (paletted or grayscale), or RGB"
                " images, in which case the color/class mappings need to be"
                " specified through a separate text file."
    )

    channel_conversion = utils.forms.SelectField(
        'Channel conversion',
        choices=[
            ('RGB', 'RGB'),
            ('L', 'Grayscale'),
            ('none', 'None'),
        ],
        default='none',
        tooltip="Perform selected channel conversion."
    )
